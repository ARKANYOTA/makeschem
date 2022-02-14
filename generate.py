#!/usr/bin/env python
import cv2
import sys
from PIL import Image
import numpy as np
from math import sqrt

def dome():
    taille = 91
    center = 43.5
    rayon = 43
    plusoumoins = 43
    f = open("a.scdef", "w")
    for x in range(taille):
        for y in range(taille):
            for z in range(taille):
                if (rayon**2)-plusoumoins <round((x-center)**2+(y)**2+(z-center)**2, 2)<=(rayon**2)+plusoumoins:
                    f.write(f"{x} {y} {z} blue_stained_glass\n")
    f.close()


minecraft_color_nuance = {
    "black": (0, 0, 0),
    "blue": (0, 0, 255),
    "brown": (102, 51, 0),
    "cyan": (0, 255, 255),
    "gray": (128, 128, 128),
    "green": (0, 128, 0),
    "light_blue": (0, 255, 255),
    "light_gray": (211, 211, 211),
    "lime": (0, 255, 0),
    "magenta": (255, 0, 255),
    "orange": (255, 128, 0),
    "pink": (255, 153, 204),
    "purple": (128, 0, 128),
    "red": (255, 0, 0),
    "white": (255, 255, 255),
    "yellow": (255, 255, 0),
}

def closest_color(r, g, b, _):
    color_diffs = []
    for colorname, color in minecraft_color_nuance.items():
        cr, cg, cb = color
        color_diff = sqrt(abs(r - cr)**2 + abs(g - cg)**2 + abs(b - cb)**2)
        color_diffs.append((color_diff, color))
    return min(color_diffs)[1]


def maped():
    image_path = "a.png"
    image_verif = "averif.png"
    size = 8*16
    image = Image.open(image_path)
    image_array = np.array(image)
    data = np.zeros((size, size, 3), dtype=np.uint8)  # verif
    f = open("a.scdef", "w")
    for x in range(8*16):
        for z in range(8*16):
            the_color_a_mettre = closest_color(*image_array[x,z])
            the_colorname_a_mettre = list(minecraft_color_nuance.keys())[list(minecraft_color_nuance.values()).index(the_color_a_mettre)]
            f.write(f"{x} 0 {z} {the_colorname_a_mettre}_carpet\n")
            data[x,z] = the_color_a_mettre
    f.close()
    img = Image.fromarray(data, 'RGB')
    img.save(image_verif)
    img.show()




if __name__ == "__main__":
    if "dome" in sys.argv:
        dome()
    elif "map" in sys.argv:
        maped()

    else:
        print("Usage:")
        print("python generate.py dome")
        print("python generate.py map")
