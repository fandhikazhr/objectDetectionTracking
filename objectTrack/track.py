import cv2

cap = cv2.VideoCapture("object.mp4")

tracked = cv2.TrackerMOSSE_create()
# tracked = cv2.TrackerCSRT_create() # slow fps but precision
success, img = cap.read()
tracker = cv2.selectROI("Track", img, False)
tracked.init(img,tracker)
