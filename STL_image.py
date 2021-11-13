# Required packages
from PIL import Image
import numpy as np
from stl import mesh

# Import the output percentage change from the new_api_scipt to use as the input in BullOrBear
# from new_api_script import d




# Return Bull or Bear
# Choosing which image to process
# Input is the output from the API-script
def bullOrBear(d):
    if d > 0:
        return 'Bull'
    else:
        return 'Bear'


# Return greyscale of image
# Input is the image choice from bullOrBear
def greyScaleImage(input):
    if input == 'Bull':
        image = Image.open('Chicago-Bulls-Emblem.jpg').convert('L')
        return image
    else:
        image = Image.open("Bear-Emblem.jpg").convert('L')
        return image


# return xyz matrix to process "vertice","col" and "row"
# Create a xyz matrix for image
# Input is the greyscale image
def createImageMatrix(imageInput, percentage):
    # create surface with 1000 x 5000 with N triangles
    max_size = (500, 500)
    # Dynamically changing height of image from the trend
    max_height = abs(percentage)
    min_height = 0

    # Thumbnail rescales image to a workable size
    imageInput.thumbnail(max_size)

    # Creates a NumPy array to process the image
    imageNP = np.array(imageInput)
    maxPix = imageNP.max()
    minPix = imageNP.min()

    # Define size of matrix to process
    (col, row) = imageInput.size

    # Create a 3x3 matrix with zeroes
    vertice = np.zeros((row, col, 3))

    for x in range(0, col):
        for y in range(0, row):
            pixelIntensity = imageNP[y][x]
            z = (pixelIntensity * max_height) / 229

            vertice[y][x] = (x, y, z)

    return [vertice, col, row]


# Return square vertice to build the xyz image
# Creates triangles
# Inputs are vertice, col and row generated in createImageMatrix
def matrixProcessTriangles(verticeInput, colInput, rowInput):
    faces = []
    for x in range(0, colInput - 1):
        for y in range(0, rowInput - 1):
            # Create Face 1 triangle
            vertice1 = verticeInput[y][x]
            vertice2 = verticeInput[y + 1][x]
            vertice3 = verticeInput[y + 1][x + 1]

            face1 = np.array([vertice1, vertice2, vertice3])

            # Create Face 2 triangle
            vertice1 = verticeInput[y][x]
            vertice2 = verticeInput[y + 1][x]
            vertice3 = verticeInput[y +1][x + 1]

            face2 = np.array([vertice1, vertice2, vertice3])

            faces.append(face1)
            faces.append(face2)

    # NumPy array with the created square face to build the image. triangle + triangle
    facesNP = np.array(faces)
    return [facesNP, faces]


# Return meshed image as STL-file
# inputs are facesNP and faces from the matrixProcessTriangles functions
# CREATE STL FILE
def createSTLMesh(facesNPInput, facesInput):
    surface = mesh.Mesh(np.zeros(facesNPInput.shape[0], dtype = mesh.Mesh.dtype))
    for i, f in enumerate(facesInput):
        for j in range(3):
            surface.vectors[i][j] = facesNPInput[i][j]

    # Write the mesh to file "cube.stl"
    surface.save('image.stl')
    return print("Saved STL-file as image.stl successfully")

#########################
####### TESTING #########
#########################
'''
aaa = bullOrBear(-2)
print(aaa)
bbb = greyScaleImage(aaa)
print(bbb)
ccc = createImageMatrix(bbb)
# print(ccc)
ddd = matrixProcessTriangles(ccc[0], ccc[1], ccc[2])
# print(ddd)
eee = createSTLMesh(ddd[0], ddd[1])
'''