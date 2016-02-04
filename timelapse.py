import time
import picamera

VIDEO_DAYS = 5
FRAMES_PER_HOUR = 1
FRAMES = FRAMES_PER_HOUR * 24 * VIDEO_DAYS

def capture_frame(frame):
    with picamera.PiCamera() as cam:
        time.sleep(2)
        cam.capture('/home/pi/Desktop/frame%03d.jpg' % frame)

#Capture the images
    for frame in range(FRAMES):
        #Note the time before the capture
        start = time.time()
        capture_frame(frame)
        #Wait for the next capture, take into account time taken to capture image
        time.sleep(
            int(60 * 60 / FRAMES_PER_HOUR) - (time.time() - start)
            )
