# Image download and Grayscape
#package needed
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
from stl import mesh

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

#create surface with 1000 x 5000 with N triangles
max_size = (500, 500)
max_height = 10
min_height = 0

#height = 0 for minPix
#height=maxHeight for maxPix

###############################################################
#Create the Bull STL file
gray_Bull.thumbnail(max_size)

imageNp1 = np.array(gray_Bull)
maxPix = imageNp1.max()
minPix = imageNp1.min()

#print(imageNp1)
(ncols, nrows) = gray_Bull.size

verticesBull = np.zeros((nrows, ncols, 3))

for x in range(0, ncols):
    for y in range(0, nrows):
        pixelIntensity1 = imageNp1[y][x]
        z = (pixelIntensity1 * max_height) / 229

        #print(imageNp1[y][x])
        verticesBull[y][x] = (x, y, z)

facesBull = []

for x in range(0, ncols - 1):
    for y in range(0, nrows - 1):
        #create face 1
        vertice1Bull = verticesBull[y][x]
        vertice2Bull = verticesBull[y + 1][x]
        vertice3Bull = verticesBull[y + 1][x + 1]

        face1Bull = np.array([vertice1Bull, vertice2Bull, vertice3Bull])

        #create face 2
        vertice1Bull = verticesBull[y][x]
        vertice2Bull = verticesBull[y][x + 1]
        vertice3Bull = verticesBull[y + 1][x + 1]

        face2Bull = np.array([vertice1Bull, vertice2Bull, vertice3Bull])

        facesBull.append(face1Bull)
        facesBull.append(face2Bull)

print(f"number of faces: {len(facesBull)}")
facesNpBull = np.array(facesBull)

# Create the mesh for Bull
surface = mesh.Mesh(np.zeros(facesNpBull.shape[0], dtype=mesh.Mesh.dtype))
for i, f in enumerate(facesBull):
    for j in range(3):
        surface.vectors[i][j] = facesNpBull[i][j]
# Write the mesh to file "cube.stl"
surface.save('Bull.stl')
print(surface)