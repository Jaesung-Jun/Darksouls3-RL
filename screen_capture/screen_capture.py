import mss
import mss.tools
import time
import cv2
import numpy

"""
with mss() as sct:
    for _ in range(100):
        sct.shot()
"""

def screen_record(top, left, width, height, monitor_number):
    with mss.mss() as sct:
        # Part of the screen to capture
        monitor = {
            "top": top,
            "left": left,
            "width": width,
            "height": height,
            "mon": monitor_number
        }

        while "Screen capturing":
            last_time = time.time()
            # Get raw pixels from the screen, save it to a Numpy array
            img = numpy.array(sct.grab(monitor))
            
            img = cv2.bitwise_not(img)

            cv2.imshow("OpenCV/Numpy normal", img)
            # Display the picture in grayscale
            # cv2.imshow('OpenCV/Numpy grayscale',
            #            cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY))
            print("fps: {}".format(1 / (time.time() - last_time)))
            # Press "q" to quit
            if cv2.waitKey(25) & 0xFF == ord("q"):
                cv2.destroyAllWindows()
                break

#test code
screen_record(40, 0, 300, 300, 1)