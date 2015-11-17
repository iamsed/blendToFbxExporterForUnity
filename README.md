# blendToFbxExporterForUnity

Created by Krzysztof Żarczyński (@iamsed) on 16.11.15.
http://blog.kzarczynski.com/

The script exports multiple files from Blender into fbx models. 
It searches the path recursively and creates .fbx files next to the .blend files, then it renames corresponding Unity *.blend.meta files to *.fbx.meta to keep editor references, then <b>it deletes the .blend files</b> (back them up somewhere on your own).

This script uses custom version of Unity-BlenderToFBX.py that Unity uses internally for importing .blend files. It has been changed to allow passing arguments to it and to load the necessary .blend file.

You need Blender to be installed on your machine. 
You need to specify the following command line arguments: 
Blender's directory, path to args-Unity-BlenderToFBX.py, input directory (with blend files) 

# Sample usage:

blender --background --python "E:\Code\blendToFbxExporterForUnity\blendToFbxExporter.py" -- "E:\Code\blendToFbxExporterForUnity\args-Unity-BlenderToFBX.py" "E:\Code\sandbox\NewUnityProject\Assets"