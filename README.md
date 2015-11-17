# blendToFbxExporterForUnity

Created by Krzysztof Żarczyński (@iamsed) on 16.11.15.
http://blog.kzarczynski.com/2015/11/wanted-to-use-unity-cloud-build-but-all-my-blender-models-disappeared-solution/

The script exports multiple files from Blender into fbx models. 
It searches the path recursively and creates .fbx files next to the .blend files, then it renames corresponding Unity *.blend.meta files to *.fbx.meta to keep editor references, then <b>it deletes the .blend files</b> (make your own backup somewhere outside of the project path).

This script uses custom version of Unity-BlenderToFBX.py that Unity uses internally for importing .blend files. It has been changed to allow passing arguments to it and to load the necessary .blend file.

You can find the original file at [Unity path]\Editor\Data\Tools\Unity-BlenderToFBX.py

You need Blender to be installed on your machine. 
You need to specify the following command line arguments: 
Blender's directory, path to args-Unity-BlenderToFBX.py, input directory (with blend files) 

# Sample usage:

blender --background --python "E:\blendToFbxExporterForUnity\blendToFbxExporter.py" -- "E:\blendToFbxExporterForUnity\args-Unity-BlenderToFBX.py" "E:\NewUnityProject\Assets"	

# it deletes the .blend files so make a backup