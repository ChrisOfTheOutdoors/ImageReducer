Image Reducer
This is a Python script that allows you to compress and resize one or more image files, reducing their file size without reducing the quality of the images very much. The compressed images are saved in WebP format, which can reduce the file size even further than other image formats like JPEG or PNG.

Usage
Run the imageReducer.py file using Python 3.10 or later.
A file explorer window will open, allowing you to select one or more image files to compress. You can select multiple files by holding down the Ctrl or Shift key while clicking on the files.
Click the "Open" button to select the image files.
The program will compress each image file by resizing it to have a maximum width of 1920 pixels, keeping the aspect ratio, and then save it in WebP format with a suffix "_compressed.webp" added to the original filename.
The compressed images will be saved in a new folder named "Compressed Images-DD-MM-YYYY HH-MM" in the same directory as the selected image files.
Requirements
Python 3.10 or later
tkinter module (included with Python)
Pillow module (can be installed using pip install pillow)
Notes
The program will automatically resize images with a width greater than 1920 pixels while keeping the aspect ratio. Images with a width less than or equal to 1920 pixels will not be resized.
The program will use a default compression quality of 80 for the compressed images, but you can change this value by modifying the quality variable in the code.
The program uses the Image.LANCZOS filter to resize the image. This filter is recommended by Pillow for downsampling images and produces high-quality results with good performance.
The program will create a new folder for each run with the current date and time as the folder name. The compressed images will be saved in this folder.
The program will overwrite existing files with the same name in the same directory without warning.
The program will print a message indicating that the file was compressed successfully and the path to the compressed image file for each file compressed.

Limitations
The program only supports compressing image files. Other file types will not be processed.
The program does not provide a progress bar or other indication of the compression progress. For large image files or a large number of image files, the compression process may take some time.
The program does not provide an option to select the output image format. The images will always be saved in WebP format with a ".webp" file extension.
Troubleshooting
If you encounter any errors while running the program, make sure that you have installed Python 3.10 or later and the required modules (tkinter and Pillow). You can install the Pillow module using the pip install pillow command in your terminal or command prompt.
If the program is unable to find or open the image files you selected, make sure that the files exist and that you have permission to access them. The program may also have difficulty opening certain image file formats or corrupted files.

License
This program is released under the MIT License. You can find the full license text in the LICENSE file in the root directory of the program.

Acknowledgements
This program was created by Chris Edmonds using Python and the Pillow library. The program was inspired by similar image compression tools and scripts available online. Thanks to the developers of Python, tkinter, and Pillow for their work on these tools and libraries.