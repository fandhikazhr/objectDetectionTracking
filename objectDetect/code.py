import cv2

cap = cv2.VideoCapture("sampleVideo/highway.mp4")

objectDetect = cv2.createBackgroundSubtractorMOG2()

while True:

    success, frame = cap.read()
    height, width, _ = frame.shape
    
    masking = objectDetect.apply(frame)
    _, masking = cv2.threshold(masking, 254, 255, cv2.THRESH_BINARY)
    countours, _ = cv2.findContours(masking, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for count in countours:
        area = cv2.contourArea(count)
        if area > 5000:
            x, y, w, h = cv2.boundingRect(count)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
    
    cv2.imshow("Mask", masking)
    cv2.imshow("Video", frame)
    key = cv2.waitKey(30)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
