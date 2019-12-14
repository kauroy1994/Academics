# USAGE
# python train.py --dataset data/digits.csv --model models/svm.cpickle

# import the necessary packages
from sklearn.svm import LinearSVC
from pyimagesearch.hog import HOG
from pyimagesearch import dataset
import argparse
import cPickle
import os
import cv2
import numpy as np

scale = 2
canvas = np.zeros((300*scale, 300*scale, 3), dtype = "uint8")
for i in range(0,300):
   cv2.line(canvas,(i*scale,0),(i*scale,300*scale),(0,100,0))
cv2.putText(canvas,'training classifier...   ', (canvas.shape[1] - 600, canvas.shape[0] - 590), cv2.FONT_HERSHEY_SIMPLEX,0.5, (255, 255, 255), 2)
cv2.imshow('CONSOLE',canvas)
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required = True,
	help = "path to the dataset file")
ap.add_argument("-m", "--model", required = True,
	help = "path to where the model will be stored")
args = vars(ap.parse_args())

# load the dataset and initialize the data matrix
(digits, target) = dataset.load_digits(args["dataset"])
data = []

# initialize the HOG descriptor
hog = HOG(orientations = 18, pixelsPerCell = (10, 10),
	cellsPerBlock = (1, 1), normalize = True)

# loop over the images
for image in digits:
	# deskew the image, center it
	image = dataset.deskew(image, 20)
	image = dataset.center_extent(image, (20, 20))

	# describe the image and update the data matrix
	hist = hog.describe(image)
	data.append(hist)

# train the model
model = LinearSVC(random_state = 42)
model.fit(data, target)

# dump the model to file
f = open(args["model"], "w")
f.write(cPickle.dumps(model))
f.close()

cv2.putText(canvas,'Please select an image from the plates folder as filename:', (canvas.shape[1] - 600, canvas.shape[0] - 570), cv2.FONT_HERSHEY_SIMPLEX,0.5, (255, 255, 255), 2)
cv2.putText(canvas,'a. Car1Plate.jpg', (canvas.shape[1] - 600, canvas.shape[0] - 550), cv2.FONT_HERSHEY_SIMPLEX,0.5, (255, 255, 255), 2)
cv2.putText(canvas,'b. Car2Plate.jpg', (canvas.shape[1] - 600, canvas.shape[0] - 530), cv2.FONT_HERSHEY_SIMPLEX,0.5, (255, 255, 255), 2)
cv2.putText(canvas,'c. Car3Plate.jpg', (canvas.shape[1] - 600, canvas.shape[0] - 510), cv2.FONT_HERSHEY_SIMPLEX,0.5, (255, 255, 255), 2)
cv2.putText(canvas,'d. Car4Plate.jpg', (canvas.shape[1] - 600, canvas.shape[0] - 490), cv2.FONT_HERSHEY_SIMPLEX,0.5, (255, 255, 255), 2)
cv2.putText(canvas,'e. Car5Plate.jpg', (canvas.shape[1] - 600, canvas.shape[0] - 470), cv2.FONT_HERSHEY_SIMPLEX,0.5, (255, 255, 255), 2)
cv2.putText(canvas,'Enter a letter..', (canvas.shape[1] - 600, canvas.shape[0] - 450), cv2.FONT_HERSHEY_SIMPLEX,0.5, (255, 255, 255), 2)
cv2.imshow('CONSOLE',canvas)
k = cv2.waitKey(0)
if k == ord('a'):
   cv2.destroyAllWindows()
   os.system("/anaconda/bin/python classify.py --model models/svm.cpickle --image project/plates/Car1Plate.jpg")
elif k == ord('b'):
   cv2.destroyAllWindows()
   os.system("/anaconda/bin/python classify.py --model models/svm.cpickle --image project/plates/Car2Plate.jpg")
elif k == ord('c'):
   cv2.destroyAllWindows()
   os.system("/anaconda/bin/python classify.py --model models/svm.cpickle --image project/plates/Car3Plate.jpg")
elif k == ord('d'):
   cv2.destroyAllWindows()
   os.system("/anaconda/bin/python classify.py --model models/svm.cpickle --image project/plates/Car4Plate.jpg")
elif k == ord('e'):
   cv2.destroyAllWindows()
   os.system("/anaconda/bin/python classify.py --model models/svm.cpickle --image project/plates/Car5Plate.jpg")

