from picamera2 import Picamera2, Preview

cam = Picamera2()
cam.start_preview(Preview.QT)

# input("enter to end preview")
# cam.stop_preview()