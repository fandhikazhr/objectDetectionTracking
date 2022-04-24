import cv2

cap = cv2.VideoCapture("highway.mp4")

objectDetect = cv2.createBackgroundSubtractorMOG2()

while True:

    success, frame = cap.read()
    height, width, _ = frame.shape
