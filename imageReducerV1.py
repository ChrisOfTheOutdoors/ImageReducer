from tkinter import filedialog
from tkinter import *
from tkinter import ttk
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
        im = im.resize((w, h), Image.LANCZOS)

        # Convert the image to WebP format and compress it
        im.save(outfile, 'WebP', quality=quality)

def compress_images(file_paths):
    # Create a progress bar widget
    progress = ttk.Progressbar(root, orient="horizontal", length=200, mode="determinate")
    progress.grid(row=2, column=0, columnspan=2, pady=10)

    # Disable the Open button while processing
    open_button.config(state=DISABLED)

    # Compress each image file
    quality = 80
    now = datetime.datetime.now()
    base_dir = os.path.dirname(file_paths[0])
    os.chdir(base_dir)  # Change the current working directory to the directory that contains the selected image files
    folder_name = 'Compressed Images-' + now.strftime('%m-%d-%Y %H-%M')
    os.mkdir(folder_name)
    for i, file_path in enumerate(file_paths):
        # Update the progress bar
        progress["value"] = int((i+1)/len(file_paths)*100)
        progress.update()

        # Check if the file type is supported
        if not file_path.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp')):
            continue

        outfile = os.path.join(folder_name, os.path.splitext(os.path.basename(file_path))[0] + '_compressed.webp')
        compress_image(file_path, outfile, quality)
        print('File compressed successfully: ' + outfile)

    # Enable the Open button after processing
    open_button.config(state=NORMAL)

    # Update the progress bar to show completion
    progress["value"] = 100
    progress["mode"] = "indeterminate"
    progress["maximum"] = 1
    progress.start()

    # Set the status label to "Complete"
    status_label.config(text="Complete")

    # Wait for 1.4 seconds before closing the window
    root.after(1400, root.destroy)

def select_files():
    file_paths = filedialog.askopenfilenames(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp")])
    if file_paths:
        status_label.config(text="Processing")
        root.after(100, lambda: compress_images(file_paths))

# Create the main window
root = Tk()
root.title("Image Reducer")

# Create the UI widgets
open_button = Button(root, text="Open", command=select_files)
open_button.grid(row=0, column=0, padx=10, pady=10)

status_label = Label(root, text="")
status_label.grid(row=0, column=1)

# Start the event loop
root.mainloop()
