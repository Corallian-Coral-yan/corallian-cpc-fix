# Usage
The folder with the .cpc files to fix should be in the root folder of the project.
Run `python fix-cpc.py` and enter the folder name and absolute (full) path of the CPCE code file.

# Turning this into an executable file
This is so that we can distribute this to devices without Python installed (for the SHORE center)
1. Install PyInstaller:
   ```
   pip installer pyinstaller
   ```
   
3. Create the executable:
   ```
   pyinstaller --onefile fix-cpc.py
   ```
   
5. The executable file can be found in the `dist/` folder
