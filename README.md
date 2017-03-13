# raspi_keeper
assitant with face recoginiton and speech recognition 

  进入rasp_voice目录下，共有三个文件夹include、libs、samples。
  
  * include:包含语音识别用到的一些头文件，如错误码的含义以及语义识别和与语义识别的主要函数定义等，
  
  * libs:包含讯飞提供语音识别的库，里面的x64、x86分别是针对64位和32位的Linux操作系统，而RaspberryPi则是面向树莓派的库文件。
  
  * sample/schh:该目录下则是工程的主要程序文件，schh.c为主程序，目录下有许多wav文件，除部分属于my_train.py人脸密码识别程序外都是主程序中调用讯飞的文字转语音功能生成的，具体音频内容可在主程序中修改。
  <br>
  ## 整体运行说明
  <li>编译</li>
  <pre><code>git clone https://github.com/KiAlexander/raspi_keeper</code></pre>
  <pre><code>cd rasp_voice/samples/schh</code></pre>
  <pre><code>source make.sh</code></pre>
  <li>运行</li>
  <pre><code>./schh</code></pre>
