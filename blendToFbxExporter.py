#
# blendToFbxExporter.py
#
# Created by Krzysztof Żarczyński (@iamsed) on 16.11.15.
# http://blog.kzarczynski.com/
# Copyright (c) 2015 Krzysztof Żarczyński. All rights reserved.
#	
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
# http://en.wikipedia.org/wiki/MIT_License
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
    print("\nusage: <path to Blender> --background --python <path to blendToDaeExporter.py> -- <path to args-Unity-BlenderToFBX.py>  <path to the project (.blend files)>")
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
        outfilename = infile.replace('blend', 'fbx')
        if os.path.isfile(outfilename):
            alreadyHaveFBX.append(infile)
        else:
            status = subprocess.call(pathToBlender + ' --background --python ' + pathToBlenderToFBX + '  -- "' + infile + '" "' + outfilename + '"');
            os.remove(infile)
            processedFiles.append(infile)
        
    configfiles = [os.path.join(dirpath, f) 
    for dirpath, dirnames, files in os.walk(path) 
    for f in fnmatch.filter(files, '*.blend.meta')]
    for infile in configfiles:
        outfilename = infile.replace('blend', 'fbx')
        if not os.path.isfile(outfilename):
            os.rename(infile, outfilename)

    print("Processed files:")
    print(len(processedFiles))
    print("Skipped files (.fbx already exists at the locaton):")
    print(len(alreadyHaveFBX))
    for infile in alreadyHaveFBX:
        print(infile)

