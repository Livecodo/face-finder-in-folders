face-finder-in-folders

A Python tool to find a specific person's face in a folder of images. Given a reference photo, it scans directories (recursively) and saves images containing matching faces using the face_recognition library and OpenCV for facial detection and comparison.

FEATURES
=====================
- Detect faces in images using facial encodings
- Match images against a known reference face
- Recursively scan folders and subfolders
- Save matched results in a separate folder
- Console logs with face match distance and progress

EDIT PATHS
=====================
Before running the script, edit:
- your_image_path: path to your known/reference face image
- photos_folder: path to the folder containing images to search

RECOMMENDED PYTHON VERSION
=====================
Use Python 3.10.x for best compatibility with face_recognition and dlib.

INSTALLATION
=====================
Install required Python packages:
pip install face_recognition opencv-python dlib

WINDOWS SETUP FOR dlib (REQUIRED)
=====================
Install Visual C++ Build Tools from:
https://visualstudio.microsoft.com/visual-cpp-build-tools/

During setup, ensure the following components are selected:

✔ MSVC v143 - VS 2022 C++ x64/x86 build tools
   → Needed to compile C++ modules like dlib

✔ Windows 11 SDK (10.0.22000.0 or later)
   → Required header files and libraries

✔ C++ CMake tools for Windows
   → Optional but useful for building native modules

✔ C++ ATL for x86/x64
   → Additional C++ libraries that dlib may depend on

USAGE
=====================
1. Download or clone the script
2. Modify the paths for your image and folder
3. Run:
   python face_finder.py
4. All matched images will be saved in the "found_faces" folder

END
=====================
