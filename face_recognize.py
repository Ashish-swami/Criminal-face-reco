
import cv2, sys, numpy, os

haar_file = '/Users/Ashish/Desktop/project/haarcascade_frontalface_default.xml'

# path to the main faces directory 
datasets = '/Users/Ashish/Desktop/project/datasets'

print('Training classifier...')

# Creating a list of images and a list with a unique id
(images, labels, names, id) = ([], [], {}, 0)
for (subdirs, dirs, files) in os.walk(datasets):
    for subdir in dirs:
        names[id] = subdir
        subjectpath = os.path.join(datasets, subdir)
        for filename in os.listdir(subjectpath):
            path = subjectpath + '/' + filename
            label = id
            images.append(cv2.imread(path, 0))
            labels.append(int(label))
        id += 1
(width, height) = (130, 100)


def rounded_rectangle(img, pt1, pt2, color, thickness, r, d):
    x1,y1 = pt1
    x2,y2 = pt2
 
    # Top left
    cv2.line(img, (x1 + r, y1), (x1 + r + d, y1), color, thickness)
    cv2.line(img, (x1, y1 + r), (x1, y1 + r + d), color, thickness)
    cv2.ellipse(img, (x1 + r, y1 + r), (r, r), 180, 0, 90, color, thickness)
 
    # Top right
    cv2.line(img, (x2 - r, y1), (x2 - r - d, y1), color, thickness)
    cv2.line(img, (x2, y1 + r), (x2, y1 + r + d), color, thickness)
    cv2.ellipse(img, (x2 - r, y1 + r), (r, r), 270, 0, 90, color, thickness)
 
    # Bottom left
    cv2.line(img, (x1 + r, y2), (x1 + r + d, y2), color, thickness)
    cv2.line(img, (x1, y2 - r), (x1, y2 - r - d), color, thickness)
    cv2.ellipse(img, (x1 + r, y2 - r), (r, r), 90, 0, 90, color, thickness)
 
    # Bottom right
    cv2.line(img, (x2 - r, y2), (x2 - r - d, y2), color, thickness)
    cv2.line(img, (x2, y2 - r), (x2, y2 - r - d), color, thickness)
    cv2.ellipse(img, (x2 - r, y2 - r), (r, r), 0, 0, 90, color, thickness)

# Create a numpy array from the lists above
(images, labels) = [numpy.array(lists) for lists in [images, labels]]

# OpenCV trains a model from the images using the Local Binary Patterns algorithm
model = cv2.face.LBPHFaceRecognizer_create()

# train the LBP algorithm on the images and labels we provided above
model.train(images, labels)

face_cascade = cv2.CascadeClassifier(haar_file)
webcam = cv2.VideoCapture(0)
print('Classifier trained!')
print('recognize faces...')
while True:
    (_, im) = webcam.read()
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    # detectinng faces using the haar_cacade file
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        # colour = bgr format
	# drawing a rectangle around the face and resizing/ grayscaling it
	
        face = gray[y:y + h, x:x + w]
        face_resize = cv2.resize(face, (width, height))
        # try to recognize the face(s) using the resized faces made above
        prediction = model.predict(face_resize)
        rounded_rectangle(im, (x, y), (x + w, y + h), (0, 255, 255), 2, 15, 30)
        # if face is recognized, display the corresponding name
        if prediction[1] < 74:
            cv2.putText(im,'Crimminal Detected',(x + 5, (y + 25) + h), cv2.FONT_HERSHEY_PLAIN,1.5,(65,65, 255), 2)
            # print the confidence level with the person's name to standard output
            confidence = (prediction[1]) if prediction[1] <= 100.0 else 100.0
            
        else:
            cv2.putText(im,'Not Crimminal',(x + 5, (y + 25) + h), cv2.FONT_HERSHEY_PLAIN,1.5,(20, 185, 20), 2)
            #print("predicted person: Unknown")

    cv2.imshow('OpenCV Face Recognition -  esc to close', im)
    key = cv2.waitKey(10)
    # esc to quit 
    if key == 27:
        break
