import tkinter as tk
from PIL import Image, ImageDraw
from PIL_tutor.main import convertToPixels
import numpy as np
from model_setup import *
import threading 
from image_processor import *
from concurrent.futures import ThreadPoolExecutor
from collections import deque
MAIN_CANVA_SIZE = (400,400)
PAINT_RADIUS = 14

class MyApplication(tk.Tk):
    def __init__(self, title):
        super().__init__()  
        self.title(title)
        
        self.setUpCanvas()

        self.bind('<B1-Motion>', self.drawDigit)
        self.model = MyModel()
       
        
        self.frame_refresh = 0
        self.image_processor = ImageProcessor()
        #self.main_canva.bind("<ButtonRelease-1>", self.stopThePool)
        self.my_thread_pool = ThreadPoolExecutor(max_workers=2)
        self.on_going_task = deque()


    def uploadImage(self):
        try:
            image = self.image_processor.uploadImage()  # Assume this returns a PIL Image object
            photo = ImageTk.PhotoImage(image)

            # Store a reference to avoid garbage collection
            self.photo_reference = photo  
            
            # Clear any previous images on the canvas
            self.main_canva.delete('all')  # Clear the canvas before adding a new image

            # Add the image to the canvas
            self.main_canva.create_image(200, 200, image=self.photo_reference)  # Center the image in the canvas
            self.main_canva.update()


            result = self.getTheMatrixFromImage(image)

            self.setPredictionByMatrix(result)
            
        except FileExistsError as e:
            print

    def setUpCanvas(self):
        #! Adding The Canvas
        self.main_canva = tk.Canvas(self, width=MAIN_CANVA_SIZE[0], height=MAIN_CANVA_SIZE[1], bg='white')
        self.second_canva = tk.Canvas(self, width=MAIN_CANVA_SIZE[0]//2, height=MAIN_CANVA_SIZE[1]//2, bg='white')
        
        #! Adding the Buttons
        self.predictNumberButton = tk.Button(self, text='Predict Number', bg='blue', fg='white', command=self.predictNumber)

        self.frameOfButtons = tk.Frame(self)
        self.clearCanvas = tk.Button(self.frameOfButtons, text='Clear', bg='blue', fg='white', command=self.clear)
        self.useCamer = tk.Button(self.frameOfButtons, text='Use Camera', bg='blue', fg='white', command=self.cameraUse)
        self.uploadImage = tk.Button(self.frameOfButtons, text='Upload Image', bg='blue', fg='white', command=self.uploadImage)
        

        # Adding the Labels
        self.info = tk.Label(self, text="Here You will see guessed number!", font=("Arial", 12), fg="black",)
        # Label for percentage
        self.percent_label = tk.Label(self, text="", font=("Arial", 14), fg="black")
        


        #! Ordering the Olacement
        self.main_canva.pack(padx=10, pady=10)


        self.predictNumberButton.pack(padx=10,pady=10, expand=True, fill=tk.BOTH)
        self.uploadImage.pack(padx=10, pady=10, side=tk.LEFT)

        self.clearCanvas.pack(padx=10, pady=10, side=tk.LEFT)
        self.useCamer.pack(padx=10, pady=10, side=tk.RIGHT)
        self.frameOfButtons.pack()
        self.second_canva.pack()

        self.info.pack(pady=10)
        self.percent_label.pack()



    def drawDigit(self, event):
        x, y = event.x, event.y

        radius = PAINT_RADIUS
        self.main_canva.create_oval(x - radius, y - radius, x + radius, y+radius, fill='black')
        self.realTimePrediction()
        

    def getTheMatrixFromCanvas(self):
        image = Image.new("RGB", (MAIN_CANVA_SIZE[0], MAIN_CANVA_SIZE[1]), "white")
        draw = ImageDraw.Draw(image)

        
        for item in self.main_canva.find_all():
            coords = self.main_canva.coords(item)
            if coords:  
                draw.ellipse(coords, fill='black')
        image = image.resize((28, 28))
        
        return self.requiredData(image)
    def getTheMatrixFromImage(self, image):
        image = image.resize((28, 28))
        
        return self.requiredData(image)
    def requiredData(self, image):
        data_matrix = convertToPixels(image.getdata())

        # desirable data
        final_data = np.array(data_matrix)

        final_data = final_data.reshape(1, 28, 28, 1)

        return final_data
    
    def drawPredictedNumberAndPrediction(self, number, percent):
        self.second_canva.create_text(100, 100, text=number, font=("Helvetica", 48), fill="black")
        self.percent_label.config(text=f"Predicted Digit: {number} with Confidence: {percent:.2f}%")
        
    def predictNumber(self):
        result = self.getTheMatrixFromCanvas()
        self.setPredictionByMatrix(result)


    

    def setPredictionByMatrix(self, result):
        value, percent = self.model.predictNumber(result)

        self.second_canva.delete('all')
        self.drawPredictedNumberAndPrediction(value, percent)
        


    def clear(self):
        self.main_canva.delete('all')

    def realTimePrediction(self):
        if self.on_going_task and self.on_going_task[0].done():
            self.on_going_task.popleft()
        if len(self.on_going_task) < 2:
            self.on_going_task.append(self.my_thread_pool.submit(self.predictNumber))
    
    def cameraUse(self):
        self.image_processor.openCamera()
    


    

if __name__ == '__main__':
    application = MyApplication("Number Prediction")
    application.mainloop()
