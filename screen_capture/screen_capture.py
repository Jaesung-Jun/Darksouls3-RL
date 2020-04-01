import mss
import mss.tools
import time
import cv2
import numpy
import pygetwindow as gw

"""
with mss() as sct:
    for _ in range(100):
        sct.shot()
"""
def getDS3Window():
    #DARK SOULS III
    DS3 = gw.getWindowsWithTitle('DARK SOULS III')
    if DS3 == None:
        DS3_window = DS3[0]
        return DS3_window.top, DS3_window.left, DS3_window.width, DS3_window.height
    else:
        return 0, 0, 0, 0
def screenRecord(monitor_number):
    with mss.mss() as sct:
        # Part of the screen to capture
        while "Screen capturing":
            top, left, width, height = getDS3Window()
            if top == 0 and left == 0 and width == 0 and height == 0:
                print("Can't Find DS3 Window")
                cv2.destroyAllWindows()
                break
            monitor = {
                "top": top+40,
                "left": left+40,
                "width": width-50,
                "height": height-50,
                "mon": monitor_number
            }
            last_time = time.time()
            # Get raw pixels from the screen, save it to a Numpy array
            img = numpy.array(sct.grab(monitor))
            
            #img = cv2.bitwise_not(img)

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
screenRecord(1)