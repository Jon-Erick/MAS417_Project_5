# Image download and Grayscape
#package needed
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
#from stl import mesh

#download BULL image, test to see it works
im1 = Image.open("Chicago-Bulls-Emblem.jpg")
#plt.imshow(im1)
#plt.show()

#download Bear image, test to see it works
im2 = Image.open("Bear-Emblem.jpg")
#plt.imshow(im2)
#plt.show()

#grayscale images
gray_Bull = Image.open('Chicago-Bulls-Emblem.jpg').convert('L')
#plt.imshow(gray_Bull)
#plt.show()

gray_Bear = Image.open('Bear-Emblem.jpg').convert('L')
#plt.imshow(gray_Bear)
#plt.show()