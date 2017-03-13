# raspi_keeper
assitant with face recoginiton and speech recognition 

  <h1>工程说明</h1>
  <li>该项目为在北京邮电大学大三时搞得大学生创新项目，使用了树莓派调用讯飞语音库，完成具有一点功能的语音智能管家系统，程序写的比较差，以后水平上去了在回头优化代码</li>
  <h2>所使用的硬件材料</h2>
  * 树莓派3B 建议购买套餐，比较实惠<a href="https://item.jd.com/11092662549.html">https://item.jd.com/11092662549.html</a>
  * sd卡8g  
  <h2>目录说明</h2>
  进入rasp_voice目录下，共有三个文件夹include、libs、samples。
  
  * include:包含语音识别用到的一些头文件，如错误码的含义以及语义识别和与语义识别的主要函数定义等，
  
  * libs:包含讯飞提供语音识别的库，里面的x64、x86分别是针对64位和32位的Linux操作系统，而RaspberryPi则是面向树莓派的库文件。
  
  * sample/schh:该目录下则是工程的主要程序文件，schh.c为主程序，目录下有许多wav文件，除部分属于my_train.py人脸密码识别程序外都是主程序中调用讯飞的文字转语音功能生成的，具体音频内容可在主程序中修改。
  <br>
  <h2>整体运行说明</h2>
  <li>编译</li>
  <pre><code>git clone https://github.com/KiAlexander/raspi_keeper</code></pre>
  <pre><code>cd rasp_voice/samples/schh</code></pre>
  <pre><code>source make.sh</code></pre>
  <li>运行</li>
  <pre><code>./schh</code></pre>
  <br>
  
  <h2>硬件控制</h2>
  
  <h3>灯控</h3>
  <li>可用led小灯模拟，也可以用继电器接台灯控制开和关</li> 
  <h4>开灯</h4>
  <pre><code>python ledopen.py</code></pre>
  <h4>关灯</h4>
  <pre><code>python ledclose.py</code></pre>
  <br>
  
  <h3>烟雾传感</h3>
  <li>实时监测，为方便语音合成故报警音频在schh.c。所有在运行schh文件前，需要先开启一个终端运行smoke.py</li> 
  <pre><code>python smoke.py</code></pre>
  <br>
  
  <h3> 用人脸作为识别密码</h3>
  <li>my_train.py为使用simpeCV来进行拍取测试者脸型，训练成特定脸型密码，识别率较好。可单独测试。首次运行，路径下若没有任何jpg文件会拍摄一张包含人脸的照片作为伺候运行的识别密码</li> 
  <pre><code>python my_train.py</code></pre>
  
  <h3> 测周围温湿度</h3>
  <li>结合讯飞文字转语音功能,调用wiringpi进行GPIO控制</li> 
   <li>编译</li>
  <pre><code>source make.sh</code></pre>
   <li>运行</li>
  <pre><code>./temperature</code></pre>
  
  <br>
  <h2>GUI界面</h2>
  <li>为方面树莓派触摸屏操作，使用Tkinter编写了button界面,分别控制，开灯关灯，查温湿度，音乐控制等功能</li> 
  <pre><code>python button.py</code></pre>
  
  
