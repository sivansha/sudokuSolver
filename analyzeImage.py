import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

imgPath = "./testData/sudoku1.jpg"

# read the sudoku image as a gray scale image.
img = cv.imread(imgPath)
imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# "If the image cannot be read... the function returns an empty matrix" https://docs.opencv.org/
if imgGray is None:
    print("Error: could not read image from {}".format(imgPath))

# blur image
imgBlur = cv.GaussianBlur(imgGray, (25, 25), 0)
# perform threshold
imgThreshold = cv.adaptiveThreshold(imgBlur, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 7, 3)
# invert the image
imgInverted = cv.bitwise_not(imgThreshold)
# dilate the image
kernel = np.ones((20, 20), np.uint8)
imgDilated = cv.dilate(imgInverted, kernel, iterations=1)

# plt.imshow(imgDilated, cmap="gray")
# plt.show()

# detect blob
params = cv.SimpleBlobDetector_Params()
params.minThreshold = 10
params.maxThreshold = 200
params.filterByCircularity = True
params.minCircularity = 0.1
detector = cv.SimpleBlobDetector_create(params)

keypoints = detector.detect(imgDilated)
im_with_keypoints = cv.drawKeypoints(img, keypoints, np.array([]), (0, 0, 255),cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv.imwrite("Keypoints.png", im_with_keypoints)
