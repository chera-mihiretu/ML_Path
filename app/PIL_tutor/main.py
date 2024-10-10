import os
from typing import *


def convertToPixels(oneDimensionImagePixel:List[int], width:int=28, height:int=28, threshold:int=187) -> List[List[int]]:
   
    answer = [[0 for _ in range(width)] for __ in range(height)]
    for row in range(width):
        for col in range(height):
            gray = oneDimensionImagePixel[row * width + col]
            if isinstance(oneDimensionImagePixel[row * width + col], list):
                r,g,b,*a  = oneDimensionImagePixel[row * width + col]
                gray = 0.29892 + r + 0.5870 * g + 0.1140 * b
                answer[row][col] = 1 if gray < threshold else 0
            else:
                answer[row][col] = 1 if (255 - gray) < threshold else 0
            
    return answer

