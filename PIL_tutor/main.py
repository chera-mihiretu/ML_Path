from PIL import Image 
import os

image = Image.open('PIL_tutor/test.png')

left, top, right, bottom = 0,0,28,28

cropped_image = image.crop((left, top, right, bottom))
image = image.resize((28,28))
pixels = list(image.getdata())

answer = [[0 for _ in range(28)] for __ in range(28)]
for i in range(28):
    for j in range(28):
        r,g,b,a = pixels[i * 28 + j]
        gray = 0.29892 + r + 0.5870 * g + 0.1140 * b
        answer[i][j] = 1 if gray < 128 else 0

print(*answer, sep='\n')