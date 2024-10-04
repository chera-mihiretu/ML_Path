import tkinter as tk
import mss 
from PIL import Image, ImageDraw
from PIL_tutor.main import convertToPixels
root = tk.Tk()


root.title('Digit Recgonition')

size = (400,400)




def drawDigit(event):
    x, y = event.x, event.y

    radius = 7
    canvas.create_oval(x - radius, y - radius, x + radius, y+radius, fill='black')

def guessNumber():
    
    image = Image.new("RGB", (size[0], size[1]), "white")
    draw = ImageDraw.Draw(image)

    
    for item in canvas.find_all():
        coords = canvas.coords(item)
        if coords:  
            draw.ellipse(coords, fill='black')
    image = image.resize((28, 28))
    # TODO: Here you will guess and display the number
def drawNumber(number):

    # Draw the number on the canvas at coordinates (100, 100)
    second_canvas.create_text(100, 100, text=number, font=("Helvetica", 48), fill="black")

# first Canvas
canvas = tk.Canvas(root, width=size[0], height=size[1], bg='white')
canvas.pack()

# the button
button = tk.Button(root, text='Guess Number', command=guessNumber)
button.pack()

# Second Canvas for drawing the guessed number
second_canvas = tk.Canvas(root, width=size[0]//2, height=size[1]//2, bg='white')

second_canvas.pack()

# adding infomration about the second canva
label = tk.Label(root, text="Here You will see guessed number!", font=("Arial", 16), fg="black")
label.pack(pady=20) 

# Binding the first canvas with mouse
canvas.bind('<B1-Motion>', drawDigit)




if __name__ == '__main__':
    root.mainloop()