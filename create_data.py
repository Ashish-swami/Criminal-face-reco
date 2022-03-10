#Creating database

import cv2, sys, numpy, os
haar_file = '/Users/Ashish/Desktop/project/haarcascade_frontalface_default.xml'
  
# All the faces data will be

datasets = '/Users/Ashish/Desktop/project/datasets'
  
 
sub_data = '/Users/Ashish/Desktop/project/datasets/ashish'    
  
path = os.path.join(datasets, sub_data)
if not os.path.isdir(path):
    os.mkdir(path)
  
# defining the size of images 
(width, height) = (130, 100)    
  
#'0' is used for my webcam 

face_cascade = cv2.CascadeClassifier('/Users/Ashish/Desktop/project/haarcascade_frontalface_default.xml')
webcam = cv2.VideoCapture(0) 
  
# The program loops until it has 30 images of the face.
count = 1
while count < 30: 
    (_, im) = webcam.read()
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(im, (x, y), (x + w, y + h), (255, 0, 0), 2)
        face = gray[y:y + h, x:x + w]
        face_resize = cv2.resize(face, (width, height))
        cv2.imwrite('%s/%s.jpg' % (path, count), face_resize)
    count += 1
      
    cv2.imshow('OpenCV', im)
    key = cv2.waitKey(10)
    if key == 27:
        break
