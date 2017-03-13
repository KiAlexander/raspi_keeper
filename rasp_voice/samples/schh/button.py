# -*- coding:utf-8 -*- 
# file: Tkinterroot.py 
# 
from Tkinter import *
import os
import threading

#定义Button的回调函数
def helloButton():
    execfile("./bbb.py")
    
def start_button():
    t =threading.Thread(target=voice_thread)
    t.start()
    
def voice_thread():
    #os.popen('~/xunfei_voice/samples/schh/schh')
    os.system('./schh')

def stop_button():
    os.system('ps -ef|grep schh|grep -v grep|cut -c 9-15|xargs kill -s 9')

def ledopen():
	os.system('python ledopen.py')

def ledclose():
	os.system('python ledclose.py')

def temperature_humidity():
	os.system('./temperature/temperature')
        os.system('ps -ef|grep omxplayer|grep -v grep|cut -c 9-15|xargs kill -s 9')
def music():
    t =threading.Thread(target=music_thread)
    t.start()
    
def music_thread():
    os.system('omxplayer bupt.mp3')

def stop_music():
    os.system('ps -ef|grep omxplayer|grep -v grep|cut -c 9-15|xargs kill -s 9')

root =Tk()

#buttons
# bt=Button(root,text = 'Hello Button',command = helloButton)

btn1 = Button(root,text = '开始程序',command = start_button).pack()
btn2 = Button(root,text = '结束程序',command = stop_button).pack()

#control
btn3 = Button(root,text = '开灯',command = ledopen).pack()
btn4 = Button(root,text = '关灯',command = ledclose).pack()
btn5 = Button(root,text = '温湿度',command = temperature_humidity).pack()
btn6 = Button(root,text = '播放音乐',command = music).pack()
btn7 = Button(root,text = '停止播放',command = stop_music).pack()

root.mainloop()
