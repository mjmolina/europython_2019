import os
import sys
import numpy as np
from skimage import io
from skimage.color import rgb2gray
from itertools import groupby

poem = """
Red Touch Yellow, Kills a Fellow
Red Touch Black, Venom Lack
"""
#print(poem)

def get_gray_from_rgb(rgb):
    return "{:.5f}".format(rgb2gray(np.array([[rgb]], dtype=np.uint8))[0][0])

base_colors = {get_gray_from_rgb([255, 0, 0]): "red",
               get_gray_from_rgb([255, 255, 0]): "yellow",
               get_gray_from_rgb([0, 0, 0]): "black"}

def would_i_die(colors):
    snake_len = len(colors)
    for i in range(snake_len-1):
        a = colors[i]
        b = colors[i+1]
        if (a == "red" and b == "yellow") or (a == "yellow" and b == "red"):
            return "\nPoisonous!\n\n> RUUUUUUUUUUUUUUUUUUUUUN! :("
        elif (a == "red" and b == "black") or (a == "black" and b == "red"):
            return "\nNOT Poisonous\n\n> You will be OK :)"
    return "I don't know"

filename = sys.argv[1]
if not os.path.isfile(filename):
    sys.exit(-1)

print(f"Analyzing image '{filename}'...")

img = io.imread(filename)
img_gray = rgb2gray(img)
h, w, c = img.shape

# Get middle pixel line
y = img_gray[int(h/2), :]

# Remove consecutive repeated
y = ["{:.5f}".format(i[0]) for i in groupby(y)]

# Get color names from values
colors = [base_colors[i] for i in y]

print(would_i_die(colors))
