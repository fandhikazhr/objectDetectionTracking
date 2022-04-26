# objectDetectionTracking
Learn about object detection and tracking with python script 👀
- Some Reference

On `track.py`script, we use the cv2.TrackerMOSSE_create() and cv2.TrackerCSRT_create() functions. In the latest version of opencv-contrib-python we will not find that function, so we need to downgrade our version of opencv-contrib-python to version 3.4.13.47.

I found this solution in here : https://stackoverflow.com/questions/65645900/failed-to-use-cv2-trackermosse-create-and-other-methods-in-opencv-python

```
pip install --user opencv-contrib-python==3.4.13.47
```

# Preview

![objectDetect](https://user-images.githubusercontent.com/99522867/165229017-6279a02b-5e14-4949-8dec-4583d85514c5.gif)
