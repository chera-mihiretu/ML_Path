import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk


class ImageProcessor:
    def openCamer(self):
        pass

    def uploadImage(self):
        file_path = filedialog.askopenfilename()

        if file_path:
            if file_path.split('.')[-1] not in {'png', 'jpg'}:
                raise FileExistsError('Not and Image')
            else:
                image = Image.open(file_path)
                image = image.resize((400, 400))  
                
                return image
        else:
            raise FileExistsError('There is something wrong with the file')
