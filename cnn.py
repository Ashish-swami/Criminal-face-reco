import tensorflow as tf
import tflearn
import cv2 import Rectangle

from matplotlib.patches import Rectangle
     
from matplotlib import pyplot
from mtcnn.mtcnn import MTCNN

# loading image from file
filename = '/Users/Ashish/Desktop/project/test1.jpeg'
pixels = pyplot.imread(filename)

# creating the detector
detector = MTCNN()

# detecting faces in the image

faces = detector.detect_faces(pixels)
for face in faces:
	print(face)


  fro result in result_list:

  
     # cretin th cordnts
     x, y, width, height = result['box']

     # creating the shape
     rect = Rectangle((x, y), width, height, color='red')


# drawing the rect on imagge

def draw_image(filename, result_list):

    
	data = pyplot.imread(filename)
	
	# plot the image
	pyplot.imshow(data)
	
	
	# plot each box
	for result in result_list:

		
		x, y, width, height = result['box']
		
		
		rect = Rectangle((x, y), width, height, color='red')

	    
		
	# show the plot
	pyplot.show()

            
# the folder where images are 
TrainingImagePath="/Users/Ashish/Desktop/project/datasets"



 def training(       ):

