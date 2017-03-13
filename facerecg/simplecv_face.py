#!/usr/bin/python2.7
 
# Programma test Haar Features
 
import picamera
from SimpleCV import Image
import time
 
with picamera.PiCamera() as camera:
    camera.resolution = (640, 480)
    camera.start_preview()
    time.sleep(10)
    camera.capture('foto.jpg')
    foto=Image("foto.jpg")
 
    print(foto.listHaarFeatures())
    trovati=foto.findHaarFeatures('face.xml')
    if trovati:
       for trovato in trovati:
           print "Found all coordinate : " + str(trovato.coordinates())
           trovato.draw() 
    else:
       print "No found" 
    camera.stop_preview()
    foto.save('foto1.jpg') 
    foto.show()
    time.sleep(10)