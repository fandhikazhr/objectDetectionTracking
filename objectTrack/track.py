import cv2

cap = cv2.VideoCapture("object.mp4")

tracked = cv2.TrackerMOSSE_create()
# tracked = cv2.TrackerCSRT_create() # slow fps but precision
success, img = cap.read()
tracker = cv2.selectROI("Track", img, False)
tracked.init(img,tracker)

def startTrack(img, tracker):
    x, y, w, h = int(tracker[0]),int(tracker[1]),int(tracker[2]),int(tracker[3])
    cv2.rectangle(img, (x,y), ((x + w),(y+h)), (0,0,255), 3, 1)
    cv2.putText(img, "Tracking", (75,75), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,255,0), 3)
