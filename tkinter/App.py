import tkinter as tk
from PIL import Image, ImageDraw
from PIL_tutor.main import convertToPixels
import numpy as np
from model_setup import *
from concurrent.futures import ThreadPoolExecutor
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
    def drawImage(self, event):
        pass
    def setUpCanvas(self):
        #! Adding The Canvas
        self.main_canva = tk.Canvas(self, width=MAIN_CANVA_SIZE[0], height=MAIN_CANVA_SIZE[1], bg='white')
        self.second_canva = tk.Canvas(self, width=MAIN_CANVA_SIZE[0]//2, height=MAIN_CANVA_SIZE[1]//2, bg='white')
        
        #! Adding the Buttons
        self.predictNumberButton = tk.Button(self, text='Predict Number', bg='blue', fg='white', command=self.predictNumber)

        self.frameOfButtons = tk.Frame(self)
        self.clearCanvas = tk.Button(self.frameOfButtons, text='Clear', bg='blue', fg='white', command=self.clear)
        self.useCamer = tk.Button(self.frameOfButtons, text='Use Camera', bg='blue', fg='white')
        self.uploadImage = tk.Button(self.frameOfButtons, text='Upload Image', bg='blue', fg='white')
        

        # Adding the Labels
        self.info = tk.Label(self, text="Here You will see guessed number!", font=("Arial", 12), fg="black",)
        # Label for percentage
        self.percent_label = tk.Label(self, text="", font=("Arial", 14), fg="black")
        


        #! Ordering the Olacement
        self.main_canva.pack(padx=10, pady=10)


        self.predictNumberButton.pack(padx=10,pady=10)
        self.clearCanvas.pack(padx=10, pady=10, side=tk.LEFT)

        self.uploadImage.pack(padx=10, pady=10, side=tk.LEFT)
        self.useCamer.pack(padx=10, pady=10, side=tk.RIGHT)
        self.frameOfButtons.pack()
        self.second_canva.pack()

        self.info.pack(pady=10)
        self.percent_label.pack()


    def drawDigit(self, event):
        x, y = event.x, event.y

        radius = PAINT_RADIUS
        self.main_canva.create_oval(x - radius, y - radius, x + radius, y+radius, fill='black')
        
        if self.frame_refresh > 60:
            self.predictNumber()
            self.frame_refresh = 0
        self.frame_refresh += 1

    def getTheMatrixFromCanvas(self):
        image = Image.new("RGB", (MAIN_CANVA_SIZE[0], MAIN_CANVA_SIZE[1]), "white")
        draw = ImageDraw.Draw(image)

        
        for item in self.main_canva.find_all():
            coords = self.main_canva.coords(item)
            if coords:  
                draw.ellipse(coords, fill='black')
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

        value, percent = self.model.predictNumber(result)

        self.second_canva.delete('all')
        self.drawPredictedNumberAndPrediction(value, percent)
        


    def clear(self):
        self.main_canva.delete('all')




    

if __name__ == '__main__':
    application = MyApplication("Number Prediction")
    application.mainloop()
