from picamera import PiCamera, Color
from time import sleep

camera = PiCamera()

# #1 simply camera
# camera.start_preview()
# sleep(10)
# camera.stop_preview()

# #2 rotation 0 90 180 270 degree
# camera.rotation = 180
# camera.start_preview()
# sleep(10)
# camera.stop_preview()

# #3transparancy alpha between 0 to 255
# camera.start_preview(alpha=200)
# sleep(10)
# camera.stop_preview()

#4 capture
camera.start_preview()
sleep(5)
camera.capture('/home/pi/image.jpg')
camera.stop_preview()

# #5 constantly capture
# camera.start_preview()
# for i in range(5):
#     sleep(5)
#     camera.capture('/home/pi/image%s.jpg' % i)
# camera.stop_preview()

# #6 record
# camera.start_preview()
# camera.start_recording('/home/pi/video.h264')
# sleep(10)
# camera.stop_recording()
# camera.stop_preview()

# #7 jpg size still photo 2582x1944 min 64x64  video 1920x1080
# camera.resolution = (2592, 1944)
# camera.framerate = 15
# camera.start_preview()
# sleep(5)
# camera.capture('/home/pi/max.jpg')
# camera.stop_preview()

# #8 annotate
# camera.start_preview()
# camera.annotate_text = "Hello world!"
# sleep(5)
# camera.capture('/home/pi/text.jpg')
# camera.stop_preview()

# #9 brightness
# camera.start_preview()
# camera.brightness = 70
# sleep(5)
# camera.capture('/home/pi/bright.jpg')
# camera.stop_preview()

# #10 change brightness
# camera.start_preview()
# for i in range(100):
#     camera.annotate_text = "Brightness: %s" % i
#     camera.brightness = i
#     sleep(0.1)
# camera.stop_preview()

# #11 change contrast
# camera.start_preview()
# # camera.annotate_text_size = 50 #Valid sizes are 6 to 160. The default is 32.
# for i in range(100):
#     camera.annotate_text = "Contrast: %s" % i
#     camera.contrast = i
#     sleep(0.1)
# camera.stop_preview()

# #12 ground
# camera.start_preview()
# camera.annotate_background = Color('blue')
# camera.annotate_foreground = Color('yellow')
# camera.annotate_text = " Hello world "
# sleep(5)
# camera.stop_preview()

# #13 colorswap
# camera.start_preview()
# camera.image_effect = 'colorswap'
# sleep(5)
# camera.capture('/home/pi/colorswap.jpg')
# camera.stop_preview()

# #14 various image effects
# camera.start_preview()
# for effect in camera.IMAGE_EFFECTS:
#     camera.image_effect = effect
#     camera.annotate_text = "Effect: %s" % effect
#     sleep(5)
# camera.stop_preview()

# #15 set the auto white balance to a preset mode to 
# #apply a particular effect. The options are: 
# 	# off, auto, sunlight, cloudy, shade, tungsten, fluorescent, 
# 	# incandescent, flash, and horizon. The default is auto.
# camera.start_preview()
# camera.awb_mode = 'sunlight'
# sleep(5)
# camera.capture('/home/pi/sunlight.jpg')
# camera.stop_preview()

# #16 set the exposure to a preset mode to apply a particular 
# # effect. The options are: off, auto, night, nightpreview, 
# # backlight, spotlight, sports, snow, beach, verylong, 
# # fixedfps, antishake, and fireworks. The default is auto
# camera.start_preview()
# camera.exposure_mode = 'beach'
# sleep(5)
# camera.capture('/home/pi/beach.jpg')
# camera.stop_preview()