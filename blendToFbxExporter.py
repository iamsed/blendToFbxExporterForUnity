#
# blendToFbxExporter.py
#
# Created by Krzysztof Żarczyński (@iamsed) on 16.11.15.
# http://blog.kzarczynski.com/
# Copyright (c) 2015 Krzysztof Żarczyński. All rights reserved.
#	

#
# The script exports multiple files from Blender into fbx models. 
# It searches the path recursively and creates .fbx files next to the .blend files,
# then it renames corresponding Unity *.blend.meta files to *.fbx.meta to keep editor references,
# !!! then it deletes the .blend files !!!
# You need Blender to be installed on your machine. 
# You need to specify the following command line arguments: 
# Blender's directory, path to args-Unity-BlenderToFBX.py, input directory (with blend files) 
#

import os
import os.path
import sys
import glob
import bpy
import fnmatch
import subprocess

if len(sys.argv) != 7:
    print("\nusage: <path to Blender> --background --python <path to blendToFBXExporter.py> -- <path to args-Unity-BlenderToFBX.py>  <path to the project (.blend files)>")
else:
    pathToBlender = sys.argv[0]
    pathToBlenderToFBX = sys.argv[5]
    path = sys.argv[6]
    alreadyHaveFBX = []
    processedFiles = []
    configfiles = [os.path.join(dirpath, f) 
    for dirpath, dirnames, files in os.walk(path) 
    for f in fnmatch.filter(files, '*.blend')]
    for infile in configfiles:
        outfilename = infile.replace('.blend', '.fbx')
        if os.path.isfile(outfilename):
            alreadyHaveFBX.append(infile)
        else:
            proc = ("{pathToBlender} --background --python {pathToBlenderToFBX} -- {infile} {outfile}").format(
                pathToBlender=pathToBlender,
                pathToBlenderToFBX=pathToBlenderToFBX,
                infile=infile,
                outfile=outfilename
            )
            status = subprocess.call(proc, shell=True)
            os.remove(infile)
            processedFiles.append(infile)
        
    configfiles = [os.path.join(dirpath, f) 
    for dirpath, dirnames, files in os.walk(path) 
    for f in fnmatch.filter(files, '*.blend.meta')]
    for infile in configfiles:
        outfilename = infile.replace('.blend', '.fbx')
        if not os.path.isfile(outfilename):
            os.rename(infile, outfilename)

    print("Processed files:")
    print(len(processedFiles))
    print("Skipped files (.fbx already exists at the locaton):")
    print(len(alreadyHaveFBX))
    for infile in alreadyHaveFBX:
        print(infile)

