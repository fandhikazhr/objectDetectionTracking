import cv2

cap = cv2.VideoCapture("sampleVideo/highway.mp4")

objectDetect = cv2.createBackgroundSubtractorMOG2()

while True:

    success, frame = cap.read()
    height, width, _ = frame.shape
    
    masking = objectDetect.apply(frame)
    _, masking = cv2.threshold(masking, 254, 255, cv2.THRESH_BINARY)
    countours, _ = cv2.findContours(masking, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
