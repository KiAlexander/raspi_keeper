###############################################################################
#                                                                             #
# file:    2_phone.py                                                         #
#                                                                             #
# authors: Andre Heil  - avh34                                                #
#          Jingyao Ren - jr386                                                #
#                                                                             #
# date:    December 1st 2015                                                  #
#                                                                             #
# brief:   This demonstrates OpenCV's capabilities to detect not just faces   #
#          but other objects as well. In this case a standard black phone can #
#          be detected. With the proper cascade file this program can be used #
#          to detect whichever object.                                        #
#                                                                             #
###############################################################################


### Imports ###################################################################

from picamera.array import PiRGBArray
from picamera import PiCamera

import time
import cv2
import os
import pygame


### Setup #####################################################################

os.putenv('SDL_FBDEV', '/dev/fb1')

# Setup the camera
camera = PiCamera()
camera.resolution = ( 320, 240 )
camera.framerate = 40
rawCapture = PiRGBArray( camera, size=( 320, 240 ) )

# Load the cascade files for detecting faces and phones
face_cascade = cv2.CascadeClassifier( '/home/pi/opencv-2.4.9/data/lbpcascades/lbpcascade_frontalface.xml' )
phone_cascade = cv2.CascadeClassifier( 'cascade.xml' )

t_start = time.time()
fps = 0


### Main ######################################################################

# Capture frames from the camera
for frame in camera.capture_continuous( rawCapture, format="bgr", use_video_port=True ):

    image = frame.array

    # Look for faces and phones in the image using the loaded cascade file
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    faces  = face_cascade.detectMultiScale(gray)
    phones = phone_cascade.detectMultiScale(gray)

    # Draw a rectangle around every face
    for (x,y,w,h) in faces:
        cv2.rectangle( image, ( x, y ), ( x + w, y + h ), ( 255, 255, 0 ), 2 )
        cv2.putText( image, "Face No." + str( len( faces ) ), ( x, y ), cv2.FONT_HERSHEY_SIMPLEX, 0.5, ( 0, 0, 255 ), 2 )

    # Draw a rectangle around every phone
    for (x,y,w,h) in phones:
        cv2.rectangle( image, ( x, y ), ( x + w, y + h ), ( 255, 0, 0 ), 2 )
        cv2.putText( image, "iPhone", ( x, y ), cv2.FONT_HERSHEY_SIMPLEX, 0.5, ( 0, 255, 255 ), 2 )

    # Calculate and show the FPS
    fps = fps + 1
    sfps = fps / ( time.time() - t_start )
    cv2.putText( image, "FPS : " + str( int( sfps ) ), ( 10, 10 ), cv2.FONT_HERSHEY_SIMPLEX, 0.5, ( 0, 0, 255 ), 2 )

    cv2.imshow( "Frame", image )
    cv2.waitKey( 1 )

    # Clear the stream in preparation for the next frame
    rawCapture.truncate( 0 )