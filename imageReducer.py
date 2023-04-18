from tkinter import filedialog
from tkinter import *
from PIL import Image
import os
import datetime

def compress_image(infile, outfile, quality):
    with Image.open(infile) as im:
        # Resize the image to have a maximum width of 1920px and keep the aspect ratio
        w, h = im.size
        if w > 1920:
            h = int(h * 1920 / w)
            w = 1920
        im = im.resize((w, h), Image.ANTIALIAS)

        # Convert the image to WebP format and compress it
        im.save(outfile, 'WebP', quality=quality)

root = Tk()
root.withdraw()

file_paths = filedialog.askopenfilenames()

if file_paths:
    quality = 80
    now = datetime.datetime.now()
    base_dir = os.path.dirname(file_paths[0])
    folder_name = os.path.join(base_dir, 'Compressed Images-' + now.strftime('%m-%d-%Y %H:%M'))
    os.mkdir(folder_name)
    for file_path in file_paths:
        outfile = os.path.join(folder_name, os.path.splitext(os.path.basename(file_path))[0] + '_compressed.webp')
        compress_image(file_path, outfile, quality)
        print('File compressed successfully: ' + outfile)
