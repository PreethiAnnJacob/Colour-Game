# Colour-Game
Python implementation for Colour Game where continuously coloured texts are shown like 'Green' in Yellow colour. Type the font colour of each texts until you are timed out.



https://github.com/PreethiAnnJacob/Colour-Game/assets/25536510/faf1b6ff-580f-4398-9699-6bceecd5c890





https://github.com/PreethiAnnJacob/Colour-Game/blob/main/ColourGame.mp4 

github.com/PreethiAnnJacob/Colour-Game/blob/main/ColourGame.mp4

ColourGame.py - Shows the python code  
ColourGame.exe - EXE file made using PyInstaller.
ColourGame.mp4 - Demo

Adding icon to the Tkinter window:  
1. PNG and JPG is just showing a file icon  
2. SO converted the image to ICO format using an online converter  
3. Used iconbitmap("icon.ico")  

Installing PyInstaller:  
1. Error with "pip3 install pyinstaller"  
WARNING: pip is configured with locations that require TLS/SSL, however the ssl module in Python is not available.  
2. Saw a fix that told to download run the exe file from "https://slproweb.com/products/Win32OpenSSL.html" to update the DLL files. But didn't work.  
3. Saw another fix: "For Windows 10 if you want use pip in normal cmd, not only in Anaconda prompt. you need add 3 environment paths. like the followings:   
D:\Anaconda3   
D:\Anaconda3\Scripts  
D:\Anaconda3\Library\bin   
most people only add D:\Anaconda3\Scripts"  
It worked.  
4. pip3 install pyinstaller.  

Converting to EXE:  
1. Need PyInstaller  

Using PyInstaller:  
1. Run command "pyinstaller.exe --onefile --windowed --icon=icon.ico ColourGame.py"  
2. Error:  
Failed to execute script 'ColourGame' due to unhandled exception: bitmap "icon.ico" is not defined.  
Traceback (most recent call last):  
  File "ColourGame.py", line 49, in <module>  
  File "tkinter\__init__.py", line 2071, in wm_iconbitmap  
_tkinter.TclError: bitmap "icon.ico" not defined  
Fix: Using absolute path.
4. Used both: Seems working with both. Absolute path needed if wm_iconbitmap is used. With iconbitmap() absolute path is not necessary  
root.iconbitmap(r"F:\I am trying to get better\13.11.2023 Colour Game - Python\icon.ico")  
root.wm_iconbitmap(r"F:\I am trying to get better\13.11.2023 Colour Game - Python\icon.ico")  
5. Worked with both pyinstaller.exe --onefile --windowed --icon=icon.ico ColourGame.py" as well as "pyinstaller.exe --onefile --windowed ColourGame.py"  
6. Two folders: build,dist and ColourGame.spec is created
7. exe file found in dist folder.
