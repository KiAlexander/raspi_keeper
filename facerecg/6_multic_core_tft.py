###############################################################################
#                                                                             #
# file:    6_multic_core_tft.py                                               #
#                                                                             #
# authors: Andre Heil  - avh34                                                #
#          Jingyao Ren - jr386                                                #
#                                                                             #
# date:    December 1st 2015                                                  #
#                                                                             #
# brief:   This is similar to the 4_multi_core.py except now we're displaying #
#          the output on the piTFT screen rather than on the monitor.         #
#                                                                             #
###############################################################################


### Imports ###################################################################

from picamera.array import PiRGBArray
from picamera import PiCamera
from functools import partial

import multiprocessing as mp
import cv2
import os
import time
import pigpio
import pygame
import sys


### Setup #####################################################################

os.putenv( 'SDL_FBDEV', '/dev/fb1' )
os.putenv( 'SDL_MOUSEDRV', 'TSLIB' )
os.putenv( 'SDL_MOUSEDEV', '/dev/input/touchscreen' )

resX = 320
resY = 240

cx = resX / 2
cy = resY / 2

pygame.init()
lcd = pygame.display.set_mode( ( 320, 240 ) )
pygame.mouse.set_visible( False )

panX = 19.2
panY = 19.2

pi = pigpio.pi()
pi.set_mode(  4, pigpio.OUTPUT )
pi.set_PWM_frequency(  4, 50   )
pi.set_PWM_dutycycle(  4, panX )

pi.set_mode( 17, pigpio.OUTPUT )
pi.set_PWM_frequency( 17, 50   )
pi.set_PWM_dutycycle( 17, panY )

# Setup the camera
camera = PiCamera()
camera.resolution = ( resX, resY )
camera.framerate = 60

# Use this as our output
rawCapture = PiRGBArray( camera, size=( resX, resY ) )

# The face cascade file to be used
face_cascade = cv2.CascadeClassifier( '/home/pi/opencv-2.4.9/data/lbpcascades/lbpcascade_frontalface.xml' )

font = pygame.font.SysFont( "monospace", 15 )
t_start = time.time()
fps = 0


### Helper Functions ##########################################################

def get_faces( img ):

    gray = cv2.cvtColor( img, cv2.COLOR_BGR2GRAY )
    faces = face_cascade.detectMultiScale( gray )

    return faces, img

def draw_frame( img, faces ):

    global panX
    global panY
    global fps
    global time_t

    # Draw a rectangle around every face
    for ( x, y, w, h ) in faces:
        cv2.rectangle( img, ( x, y ),( x + w, y + h ), ( 200, 255, 0 ), 2 )
        cv2.putText( img, "Face No." + str( len( faces ) ), ( x, y ), cv2.FONT_HERSHEY_SIMPLEX, 0.5, ( 0, 0, 255 ), 2 )

        if ( len ( faces ) == 1 ):
            tx = x + w/2
            ty = y + h/2

            if   ( cx - tx >  20 and panX <= 25 ):
                panX += .1
                pi.set_PWM_dutycycle(  4, panX )
            elif ( cx - tx < -20 and panX >= 12 ):
                panX -= .1
                pi.set_PWM_dutycycle(  4, panX )

            if   ( cy - ty >  20 and panY >= 12 ):
                panY -= .1
                pi.set_PWM_dutycycle( 17, panY )
            elif ( cy - ty < -20 and panY <= 25 ):
                panY += .1
                pi.set_PWM_dutycycle( 17, panY )

    # Calculate and show the FPS
    fps = fps + 1
    sfps = fps / (time.time() - t_start)
    lfps = font.render( "FPS: " + str( sfps ), 1, ( 255, 0, 0 ) )

    # Have to write the image to a temporary file so it can be used by pygame
    cv2.imwrite( 'tmp.jpg', img )
    img = pygame.image.load( 'tmp.jpg' )

    lcd.blit(  img, ( 0, 0 ) )
    lcd.blit( lfps, ( 0, 0 ) )
    pygame.display.update()


### Main ######################################################################

if __name__ == '__main__':

    pool = mp.Pool( processes=4 )
    fcount = 0

    camera.capture( rawCapture, format="bgr" )

    r1 = pool.apply_async( get_faces, [ rawCapture.array ] )
    r2 = pool.apply_async( get_faces, [ rawCapture.array ] )
    r3 = pool.apply_async( get_faces, [ rawCapture.array ] )
    r4 = pool.apply_async( get_faces, [ rawCapture.array ] )

    f1, i1 = r1.get()
    f2, i2 = r2.get()
    f3, i3 = r3.get()
    f4, i4 = r4.get()

    rawCapture.truncate( 0 )

    for frame in camera.capture_continuous( rawCapture, format="bgr", use_video_port=True ):
        image = frame.array

        if   fcount == 1:
            r1 = pool.apply_async( get_faces, [ image ] )
            f2, i2 = r2.get()
            draw_frame( i2, f2 )

        elif fcount == 2:
            r2 = pool.apply_async( get_faces, [ image ] )
            f3, i3 = r3.get()
            draw_frame( i3, f3 )

        elif fcount == 3:
            r3 = pool.apply_async( get_faces, [ image ] )
            f4, i4 = r4.get()
            draw_frame( i4, f4 )

        elif fcount == 4:
            r4 = pool.apply_async( get_faces, [ image ] )
            f1, i1 = r1.get()
            draw_frame( i1, f1 )

            fcount = 0

        fcount += 1

        rawCapture.truncate( 0 )

        for event in pygame.event.get():
            if ( event.type is pygame.MOUSEBUTTONDOWN ):
                pi.stop()
                pygame.quit()
                pool.close()
                sys.exit()