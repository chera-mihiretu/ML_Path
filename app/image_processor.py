import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageOps
import cv2


class ImageProcessor:
    def __init__(self):
        self.esc_key = 27
       
    def openCamera(self):
        self.camera_obj = cv2.VideoCapture(0)
        self.width = self.camera_obj.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.camera_obj.get(cv2.CAP_PROP_FRAME_HEIGHT)
        count = 0
        while True:
            ret, frame = self.camera_obj.read()  
            if not ret:  
                print("Error: Could not read frame.")
                break
            frame = cv2.flip(frame, 1)
            frame_copy = frame.copy()  

            needed_box = (400,400)

            needed_box_pos = ((int(self.width//2 - needed_box[0]//2), 
                               int(self.height)//2 - needed_box[1]//2)),\
                               (int(self.width)//2 + needed_box[0]//2,
                               int(self.height)//2 + needed_box[1]//2)
            
            cropped_image = frame[needed_box_pos[0][1]:needed_box_pos[1][1], needed_box_pos[0][0]:needed_box_pos[1][0]]
            cropped_image = cv2.flip(cropped_image, 1)
            image_gray = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2GRAY)
           
            cv2.imshow('Cropped', image_gray)
            
            cv2.imshow('Input', frame_copy)  
            count += 1
            
            if count > 10:
                
                count = 0
                
                yield cropped_image
                
            
            
            if cv2.waitKey(1) & 0xFF == self.esc_key:  
                break


        
        cv2.destroyAllWindows()

    def uploadImage(self):
        file_path = filedialog.askopenfilename()

        if file_path:
            if file_path.split('.')[-1] not in {'png', 'jpg'}:
                raise FileExistsError('Not and Image')
            else:
                image = cv2.imread(file_path)
                
                
                return image
        else:
            raise FileExistsError('There is something wrong with the file')
        
    def addWhitePadding(self, image):
        padding = 50
        image_with_padding = ImageOps.expand(image, border=padding, fill='white')
        copy_image = image_with_padding.copy()
        return copy_image
    def toPilImage(self, image):
        opencv_image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Convert the NumPy array (OpenCV image) to a PIL image
        pil_image = Image.fromarray(opencv_image_rgb)

        return pil_image
    

# if __name__ == '__main__':
#     app = ImageProcessor()
#     app.openCamera()