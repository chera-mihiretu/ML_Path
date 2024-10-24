import tkinter as tk
from PIL import Image, ImageDraw
from app.PIL_tutor import convertToPixels
import numpy as np
from app.model_setup import *
import threading 
from app.image_processor import *
from concurrent.futures import ThreadPoolExecutor
from collections import deque
MAIN_CANVA_SIZE = (400,400)
PAINT_RADIUS = 14
from app.water_shade import SeparateImages
from matplotlib import pyplot as plt

class MyApplication(tk.Tk):
    def __init__(self, title):
        super().__init__()  
        self.multi_digit = False
        self.splitter = SeparateImages()
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
            pil_image = self.image_processor.toPilImage(image)
            pil_image = pil_image.resize((400,400))
            photo = ImageTk.PhotoImage(pil_image)

            # Store a reference to avoid garbage collection
            self.photo_reference = photo  
            
            # Clear any previous images on the canvas
            self.main_canva.delete('all')  # Clear the canvas before adding a new image

            # Add the image to the canvas
            self.main_canva.create_image(200, 200, image=self.photo_reference)  # Center the image in the canvas
            self.main_canva.update()


            value,percent = None, None
            if self.multi_digit:
                value, percent = self.multiDigit(image)
            else:
                value, percent = self.predictFromImage(image)
            self.drawValueAndPercent(value, percent)
            
        except FileExistsError as e:
            print

    # This is for predicting from image
    def predictFromImage(self, image):
        
        result = self.getTheMatrixFromImage(image)
        return self.setPredictionByMatrix(result)

    # toggle multi digit 
    def toggle(self):
        # Toggle the state between ON and OFF
        self.multi_digit = not self.multi_digit
        
        if self.multi_digit:
            self.toggle_button.config(text="ON", bg="green")
        else:
            self.toggle_button.config(text="OFF", bg="red")
        

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
        # Toggle button 
        self.toggle_button = tk.Button(self, text="OFF", command=self.toggle, bg="red")


        #! Ordering the Olacement
        self.main_canva.pack(padx=10, pady=10)


        self.predictNumberButton.pack(padx=10,pady=10, expand=True, fill=tk.BOTH)
        self.uploadImage.pack(padx=10, pady=10, side=tk.LEFT)

        self.clearCanvas.pack(padx=10, pady=10, side=tk.LEFT)
        self.useCamer.pack(padx=10, pady=10, side=tk.RIGHT)
        self.frameOfButtons.pack()
        # toggle button title
        self.status_label = tk.Label(self, text="Set Multi Digit Recgonition", font=("Arial", 14))
        self.status_label.pack(padx=20)

        self.toggle_button.pack(padx=20)
        self.second_canva.pack(pady=10)

        self.info.pack(pady=10)
        self.percent_label.pack()


    # drawing the image

    def drawDigit(self, event):
        x, y = event.x, event.y

        radius = PAINT_RADIUS
        self.main_canva.create_oval(x - radius, y - radius, x + radius, y+radius, fill='black')
        self.realTimePrediction()
        

    # get tuhe image from the canvas
    def getTheMatrixFromCanvas(self):
        image = Image.new("RGB", (MAIN_CANVA_SIZE[0], MAIN_CANVA_SIZE[1]), "white")
        draw = ImageDraw.Draw(image)

        
        for item in self.main_canva.find_all():
            coords = self.main_canva.coords(item)
            if coords:  
                draw.ellipse(coords, fill='black')
        image = image.resize((28, 28))
        
        return self.requiredData(image)
    
    # this is to get the matrix format by 28x28 from the image passed as an argument then fed into 
    # Predict by image
    def getTheMatrixFromImage(self, image):
        image = image.resize((28, 28))
        return self.requiredData(image)
    

    # Convert the image into gray and 28 x 28 image this is needed data
    def requiredData(self, image):
        data_matrix = convertToPixels(image.getdata())

        # desirable data
        final_data = np.array(data_matrix)

        final_data = final_data.reshape(1, 28, 28, 1)

        return final_data
    

    # This function is called by the drawValueAndPercent function
    def drawPredictedNumberAndPrediction(self, number, percent):
        
        self.second_canva.create_text(100, 100, text=number, font=("Helvetica", 30), fill="black")
        self.percent_label.config(text=f"Predicted Digit: {number} with Confidence: {percent:.2f}%")
        
    
    # This is the one that get the image from the canvas and feed it the model
    def predictNumber(self):
        
        result = self.getTheMatrixFromCanvas()
        value = percent = None
        if self.multi_digit:
            value, percent = self.multiDigit(result)
        else:
            value, percent = self.setPredictionByMatrix(result)

        self.drawValueAndPercent(value, percent)


    
    # This predixt the image by sending the image of 28x28 to the model
    def setPredictionByMatrix(self, result):
        value, percent = self.model.predictNumber(result)
        
        return (value, percent)
        
        


    # Clear the Canvas
    def clear(self):
        self.main_canva.delete('all')


    # Real time prediction uses Thread pool and deque
    # The thread pool only accepts if the current running thread is less than two
    # other wise it will not place on the thread pool waiting list
    def realTimePrediction(self, image = []):
        
        
        if self.on_going_task and self.on_going_task[0].done():
            
            self.on_going_task.popleft()
        
        if len(self.on_going_task) < 2:
            if not image:
                self.on_going_task.append(self.my_thread_pool.submit(self.predictNumber))
            else:
                
                self.on_going_task.append(self.my_thread_pool.submit(self.predictFromImage, image))


    # This is the thread in which the camera runs
    def cameraUse(self):
        thread = threading.Thread(target=self.startCamera)
        thread.start()
        


    # Start the camera 
    # It is stream like function while the called self.image_processor.operCamera is not completed
    # but it still will return the value without terminating the called function 
    def startCamera(self):
        for image in self.image_processor.openCamera():
            image = Image.fromarray(image)
            self.realTimePrediction(image)

            

            
    
    # multiple image extracter 
    # Extracts multiple numbers from the same image and feed it to the model
    def multiDigit(self, image):
        digits = self.splitter.splitNumbers(image)
        total = 0
        av_percent = 0
        count = 0
        for i in digits:

            
            my_image = self.image_processor.toPilImage(i)
            add_padding = self.image_processor.addWhitePadding(my_image)
            value, percent = self.predictFromImage(add_padding)

            total *= 10
            total += value
            av_percent += percent
            count += 1
        percent = av_percent / count
        return (total, percent)
            





    # draw the image on the canvas
    def drawValueAndPercent(self, value, percent):
        self.second_canva.delete('all')
        self.drawPredictedNumberAndPrediction(value, percent)

    

if __name__ == '__main__':
    application = MyApplication("Number Prediction")
    application.mainloop()
