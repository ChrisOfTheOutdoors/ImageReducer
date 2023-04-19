Image Reducer
Image Reducer is a Python program that allows you to reduce the file size of 
multiple images at once without significantly reducing their quality. The 
program works by resizing the images to have a maximum width of 1920 pixels 
and keeping the aspect ratio, then converting them to the WebP format and 
compressing them.

The program also includes the following features:

The ability to select only image files with the extensions ".jpg", ".jpeg",
".png", and ".bmp" for processing. Any other file types selected in the file
dialog will be ignored. A visible progress bar with the word "Processing" 
that is displayed while the program is running and switches to "Complete" 
when the program completes. The progress bar shows the percentage of images 
processed and updates in real-time as each image is compressed. Once all images
have been processed, the progress bar switches to an indeterminate mode to indicate 
that processing is complete. The status label is also updated to display "Complete". 
Finally, the program waits for 1.4 seconds before automatically closing the window.

Usage
To use Image Reducer:

Double-click on the imageReducer.exe file to launch the program.
Click the "Open" button to select one or more image files to process. Only image 
files with the extensions ".jpg", ".jpeg", ".png", and ".bmp" will be processed.
Once image processing begins, a progress bar with the word "Processing" will appear 
on the UI. As each image is compressed, the progress bar will update to show the 
percentage of images processed. When all images have been processed, the progress 
bar will switch to an indeterminate mode to indicate that processing is complete, 
and the status label will change to display "Complete". The program will then wait 
for 1.4 seconds before automatically closing the window.

Requirements
Image Reducer requires Python 3.10 and the following packages to run from the terminal:
(Note: Running the program from the .exe only requires that you have an operating system
capable of running .exe's)

tkinter
PIL
Build


To build a standalone executable using PyInstaller:
css
Copy code
pyinstaller --onefile imageReducer.py
The standalone executable will be created in the dist folder.

Notes
If you are running the standalone executable, make sure that you have downloaded the 
correct version for your operating system (32-bit or 64-bit). If the program is not 
working as expected, try running it from the command line using Python to see if any 
error messages are printed to the console. This can help you identify and fix any 
issues with the program. If you are having trouble creating a standalone executable 
with PyInstaller, try using a different packaging tool like cx_Freeze or PyOxidizer, 
or consult the PyInstaller documentation or community forums for help. If you want to 
modify the program's behavior, you can edit the imageReducer.py file using a text 
editor or Python IDE. Some possible modifications include changing the maximum image 
width, adjusting the image compression quality, or adding support for additional file 
types. If you want to distribute the program to others, you can share the standalone 
executable file with them, along with any additional instructions or documentation. 
Make sure to include any necessary license or attribution information for the packages 
used by the program.
