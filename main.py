import glob
from PIL import Image
import sys

# This is the file dir
filedir = sys.argv[1]

degree = -270

try:
    degree = sys.argv[2]
    print(f"Rotate all images to {degree} degree")
except:
    print("No degree specified. Defaulting to -270")

# Extension of the files
extension = 'jpg'

try:
    extension = sys.argv[3]
    print(f"Using .{extension} as the extension") 
except:
    print("No extension passed. Defualting to .jpg")

imageList = []

# Load all the images
for file in glob.glob(f'{filedir}*.{extension}'):
    imageList.append(Image.open(file))

# Rotate all images to the specified degree
for image in imageList:
    filename:str =(image.filename)
    new_image = image.rotate(-270,expand=True)
    new_image.save(filename)
