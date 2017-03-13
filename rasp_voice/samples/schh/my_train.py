#!/usr/bin/python
#encoding:utf-8  
 
import picamera
import time
import os
from SimpleCV import Color, Image, np
#import wiringpi as wiringpi
 
# pin_base = 65
# i2c_addr = 0x20
 
quality = 400     # Parameter "quality" for funzione findKeypointMatch
minMatch = 0.3    # Parameter "minDist" for funzione findKeypointMatch
 
try:
    password = Image("password.jpg")
except:
    password = None
 
mode = "unsaved"
saved = False
minDist = 0.25

success_flag = True
time_number = 0
 
# wiringpi.wiringPiSetup()
# wiringpi.mcp23017Setup(pin_base,i2c_addr)
# wiringpi.pinMode(65, 1)         # imposta GPA0 come output  
# wiringpi.digitalWrite(65, 0)    # imposta GPA0 a 0 (0V, off)
# wiringpi.pinMode(72, 1)         # imposta GPA7 come output  
# wiringpi.digitalWrite(72, 0)    # imposta GPA7 a 0 (0V, off)

with picamera.PiCamera() as camera:
    
 print "\n请输入脸型密码\n"
 os.system('omxplayer --no-osd -no-keys password.wav')

 while success_flag:
    camera.start_preview()
    time.sleep(5)
    camera.capture('pifacepw.jpg')
    image=Image("pifacepw.jpg")
    camera.stop_preview()
    faces = image.findHaarFeatures("face.xml") # recognize your face through the file HaarCFeatures "face"
    if faces:
        if not password:
            faces.draw()
            face = faces[-1]
            password = face.crop().save("password.jpg")
            print "已更新脸型密码库"
            break
        else:
            faces.draw()
            face = faces[-1]
            template = face.crop()
            template.save("passwordmatch.jpg")
            keypoints = password.findKeypointMatch(template,quality,minDist,minMatch)
            if keypoints:
                print "\n识别正确,欢迎回来\n"

                os.system('omxplayer --no-osd -no-keys correct.wav')
                
                # wiringpi.digitalWrite(65, 1)  
                # wiringpi.digitalWrite(72, 0)

                # domanda = raw_input("Want the last photo as password? Y/N").strip()
                # if domanda == "Y":
                #     image = cam.getImage().scale(320, 240)
                #     faces = image.findHaarFeatures("face.xml")
                #     tryit = 1
                #     while not tryit == 10 or not faces:
                #         image = cam.getImage().scale(320, 240)
                #         faces = image.findHaarFeatures("face.xml")
                #         tryit += 1
                #     if not faces:
                #         "No face found."
                #         break
                #     else:
                #         faces.draw()
                #         face = faces[-1]
                #         password = face.crop().save("password.jpg")
                #         face.crop().show()
                #         print "Saved successfully"
                #         print "Terminate the program"

                #         time.sleep(1)
                #         break
                # else:
                #     print "OK..."
                #     break

                break
                     
            else:
                print "\n识别失败,警报警报警报\n"
                os.system('omxplayer --no-osd -no-keys fail.wav')

                # time.sleep(3)

                time_number += 1

                if time_number == 3:
                    print "\n识别无效，小派拒绝服务\n"
                    os.system('omxplayer --no-osd -no-keys termination.wav')
                    # os.system('pkill -u pi')
                    break
                else:
                    continue

                # wiringpi.digitalWrite(65, 0)  
                # wiringpi.digitalWrite(72, 1)
                # break
    else:
        if time_number == 3:
            print "\n识别无效，小派拒绝服务\n"
            os.system('omxplayer --no-osd -no-keys termination.wav')
            # os.system('pkill -u pi')
            break
        else:
            time_number += 1
            print "小派没看清你的脸，请重新输入脸型密码\n"
            os.system('omxplayer --no-osd -no-keys face_again.wav')
            continue