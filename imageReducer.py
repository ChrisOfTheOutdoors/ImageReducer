# Import necessary modules
from tkinter import filedialog
from tkinter import *
from PIL import Image
import os
import datetime

# Define a function to compress the image
def compress_image(infile, outfile, quality):
    with Image.open(infile) as im:
        # Resize the image to have a maximum width of 1920px and keep the aspect ratio
        w, h = im.size
        if w > 1920:
            h = int(h * 1920 / w)
            w = 1920
        im = im.resize((w, h), Image.LANCZOS)

        # Convert the image to WebP format and compress it
        im.save(outfile, 'WebP', quality=quality)

# Create a Tkinter root window and hide it
root = Tk()
root.withdraw()

# Open a file explorer window to select image files to compress
file_paths = filedialog.askopenfilenames()

# Check if any image files were selected
if file_paths:
    # Set the quality of the compressed images
    quality = 80

    # Get the current date and time
    now = datetime.datetime.now()

    # Get the base directory of the selected image files
    base_dir = os.path.dirname(file_paths[0])

    # Change the current working directory to the base directory
    os.chdir(base_dir)

    # Create a new folder with the current date and time for the compressed images
    folder_name = 'Compressed Images-' + now.strftime('%m-%d-%Y %H-%M')
    os.mkdir(folder_name)

    # Loop through each selected image file and compress it
    for file_path in file_paths:
        # Set the output file path to the compressed image in WebP format
        outfile = os.path.join(folder_name, os.path.splitext(os.path.basename(file_path))[0] + '_compressed.webp')

        # Compress the image and save it to the output file path
        compress_image(file_path, outfile, quality)

        # Print a message indicating that the file was compressed successfully and the path to the compressed image file
        print('File compressed successfully: ' + outfile)
