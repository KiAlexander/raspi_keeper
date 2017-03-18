# <img src="https://github.com/KiAlexander/raspi_keeper/blob/master/logo.png" width="50" >raspi_keeper
a kind of raspberrypi assitant with face recoginiton and speech recognition 
<p>我是智能家居小助手小派，能够帮助您解决生活烦恼，天气预报、音乐播放、家居控制、各式各样的问题对于小派来说全都不在话下(<a href="https://www.youtube.com/watch?v=1NzAqEg7Ylk">演示视频）</a></p>
<table><tr>
<td><img src="https://github.com/KiAlexander/raspi_keeper/blob/master/left.png" width="275" ></td>
<td><img src="https://github.com/KiAlexander/raspi_keeper/blob/master/front.png" width="275"></td>
<td><img src="https://github.com/KiAlexander/raspi_keeper/blob/master/right.png" width="275"></td>
</tr></table>
  <h1>工程说明</h1>
  <p>该项目为在北京邮电大学大三时搞得大学生创新项目，使用了树莓派调用讯飞语音库，完成具有一定功能的语音智能管家系统，程序写的比较差，以后水平上去了在回头优化代码</p>
  <p>由于第一次接触树莓派，所以附下<a href="http://www.jianshu.com/p/06c000e46c48">树莓派的首次使用</a></p>
  <pre><code>$ sudo raspi-config</code></pre>
  <pre><code>$ sudo nano /etc/apt/sources.list</code></pre>
  <pre><code>$ deb http://mirror.sysu.edu.cn/raspbian/raspbian/ jessie main contrib non-free</code></pre>
  <pre><code>$ deb-src http://mirror.sysu.edu.cn/raspbian/raspbian/ jessie main contrib non-free</code></pre>
  <pre><code>$ sudo apt-get update</code></pre>
  <pre><code>$ sudo apt-get upgrade</code></pre>
  <pre><code>$ sudo apt-get dist-upgrade</code></pre>
  <pre><code>$ sudo rpi-upgrade</code></pre>
  <pre><code>$ sudo apt-get install vim</code></pre>
  <pre><code>$ sudo apt-get install libasound2-dev</code></pre>
  <pre><code>$ sudo apt-get install omxplayer</code></pre>
  <li>建议安装samba方便文件操作</li>
  1. 如果出现错误提示，则需要先执行sudo apt-get update，再重新执行sudo apt-get install samba
安装完成后，这里只是安装了samba服务，一些基本工具还没有安装，所以还需要安装samba支撑工具：
sudo apt-get install samba-common-bin
（注意：这一步非常重要，这个要是不安装会导致像smbpasswd这样的工具没有被安装，后面就无法增加samba用户了）
  <pre><code>$ sudo apt-get install samba</code></pre>
  2. 配置/etc/samba/smb.conf
  <pre><code>$ sudo vi /etc/samba/smb.conf</code></pre>
  <p>修改[homes]段为如下：</p>
  <pre><code>[homes]
   comment = Home Directories
   browseable = yes
# By default, the home directories are exported read-only. Change the
# next parameter to 'no' if you want to be able to write to them.
   read only = no
# File creation mask is set to 0700 for security reasons. If you want to
# create files with group=rw permissions, set next parameter to 0775.
   create mask = 0755
# Directory creation mask is set to 0700 for security reasons. If you want to
# create dirs. with group=rw permissions, set next parameter to 0775.
   directory mask = 0755</code></pre>
  3. 增加samba用户
  <pre><code>$ sudo smbpasswd -a pi</code></pre>
  <li>安装SimpleCv</li>
  <pre><code>$ sudo apt-get install ipython python-opencv python-scipy python-numpy python-pygame python-setuptools python-pip</code></pre>
 <pre><code>$ sudo pip install https://github.com/sightmachine/SimpleCV/zipball/develop</code></pre>
  如果运行SimpleCV提示缺少相应的组件，也可以通过pip指令进行安装，如笔者在运行时提示缺少svgwirte。
  <pre><code>$ sudo pip install svgwrite</code></pre>
  
  <h2>所使用的硬件材料</h2>
  * <a href="https://item.jd.com/11092662549.html">树莓派3B</a>&nbsp 建议购买套餐，比较实惠
  
  * <a href="https://item.jd.com/2218383.html">sd卡8g</a> 具体大小看个人需要，一般8g基本够用，个人喜欢自己从<a href="https://www.raspberrypi.org/downloads/raspbian/">树莓派官网</a> 下镜像，比较有趣些
  
  * <a href="https://detail.tmall.com/item.htm?id=538717145623&spm=a1z09.2.0.0.zAW2zC&_u=d21a79v850d2">树莓派7寸触摸屏</a> 建议买套餐加个配套外科，更方便些 
  
  * <a href="https://item.taobao.com/item.htm?spm=a1z09.2.0.0.zAW2zC&id=530162749946&_u=d21a79v83a30">树莓派摄像头</a> 用的是官方摄像头，没有选用usb摄像头是因为怕买了然后不兼容树莓派就很麻烦了
  
  * <a href="https://item.taobao.com/item.htm?id=41256373030&price=11.8-13.8&sourceType=item&sourceType=item&suid=217a9c98-4019-4652-8d75-163bca7e3dc9&ut_sk=1.V7Z%2BsWCmDo4DACoA7EeXwPsc_12278902_1489408552971.TaoPassword-QQ.1&cpp=1&shareurl=true&spm=a313p.22.17t.27675671052&short_name=h.3Qrrfn&cv=xUBQOGHT6d&sm=98d51a&app=chrome">usb免驱麦克风</a> 经检测这一款可以兼容树莓派，树莓派上录音略有杂音但不影响识别
  
  * <a href="https://item.taobao.com/item.htm?id=45048032864&price=35&sourceType=item&sourceType=item&suid=0f6dc158-6dc9-4b66-b8c2-ea05f9009798&ut_sk=1.V7Z%2BsWCmDo4DACoA7EeXwPsc_12278902_1489408552971.TaoPassword-QQ.1&cpp=1&shareurl=true&spm=a313p.22.2em.27674317489&short_name=h.3QJcIe&cv=S14fOGJiED&sm=7de044&app=chrome">树莓派音响</a> 要是有更好的选择可以选其他的，这款造型还不是很让人满意
  
  * 网线一根(前期由于没有买树莓派，采取的是笔记本直连的方式）
  
  * <a href="https://detail.tmall.com/item.htm?id=41254925223&ut_sk=1.VtRk0r44a2MDAJoiipElLqRs_21380790_1489406389682.TaoPassword-QQ.1&sourceType=item&price=16.2&origin_price=17.5&suid=6CAF4CBB-A005-4748-9265-93736B3578EF&cpp=1&shareurl=true&spm=a313p.22.1mq.27668117160&short_name=h.3Qih0c&cv=0n2jOtxddr&sm=9871ce&app=chrome">四路继电器</a> 几路的话看自己需要把
  
  * <a href="https://detail.tmall.com/item.htm?id=41209915421&ut_sk=1.VtRk0r44a2MDAJoiipElLqRs_21380790_1489406389682.TaoPassword-QQ.1&sourceType=item&price=46.08&origin_price=48.5&suid=4C5B6D86-280D-4E8E-9B1E-FCC8A7EBCDD5&cpp=1&shareurl=true&spm=a313p.22.2rx.27667847521&short_name=h.3Q7B7U&cv=t0O9OtwoL3&sm=abc1fb&app=chrome">烟雾传感器</a>
  
  * <a href="https://detail.tmall.com/item.htm?id=41248630584&ut_sk=1.VtRk0r44a2MDAJoiipElLqRs_21380790_1489406389682.TaoPassword-QQ.1&sourceType=item&price=4.2&origin_price=6.5&suid=C08EF15C-6D1E-4E61-830F-C6070040A35C&cpp=1&shareurl=true&spm=a313p.22.2x0.27667925560&short_name=h.3Q7Vzq&cv=pykMOtvnUW&sm=45be0d&app=chrome">温湿度模块</a>
  
  * <a href="https://detail.tmall.com/item.htm?id=39020143157&spm=a1z09.2.0.0.GEQKhT&_u=d21a79v8626a">木质别墅</a> 只是为了不让造型看起来那么丑
  
  * <a href="https://detail.tmall.com/item.htm?id=41230531417&ut_sk=1.VtRk0r44a2MDAJoiipElLqRs_21380790_1489832889787.TaoPassword-QQ.1&sourceType=item&price=2.09&origin_price=2.2&suid=6E0EA0B0-93BB-45D7-A9A9-81BB976F1B86&cpp=1&shareurl=true&spm=a313p.22.355.28507524265&short_name=h.eYeXP4&cv=js3iNOKbRU&sm=37dfbd&app=chrome">光敏二极管</a> 光敏二极管模块对环境光强最敏感，一般用来检测周围环境的亮度和光强，在大多数场合可以与光敏电阻传感器模块通用，二者区别在于，光敏二极管模块方向性较好，可以感知固定方向的光源
  
  <h2>目录说明</h2>
  进入rasp_voice目录下，共有三个文件夹include、libs、samples。
  
  * include:包含语音识别用到的一些头文件，如错误码的含义以及语义识别和与语义识别的主要函数定义等，
  
  * libs:包含讯飞提供语音识别的库，里面的x64、x86分别是针对64位和32位的Linux操作系统，而RaspberryPi则是面向树莓派的库文件。
  
  * sample/schh:该目录下则是工程的主要程序文件，schh.c为主程序，目录下有许多wav文件，除部分属于my_train.py人脸密码识别程序外都是主程序中调用讯飞的文字转语音功能生成的，具体音频内容可在主程序中修改。
  <h2>整体运行说明</h2>
  编译 
  <pre><code>$ git clone https://github.com/KiAlexander/raspi_keeper</code></pre>
  <pre><code>$ cd rasp_voice/samples/schh</code></pre>
  <pre><code>$ source make.sh</code></pre>
  运行
  <pre><code>$ ./schh</code></pre>
 
  <h2>硬件控制</h2>
  具体引脚设置参考相应文件代码中的定义
  <h3>灯控</h3>
  可用led小灯模拟，也可以用继电器接台灯控制开和关
  <h4>开灯</h4>
  <pre><code>$ python ledopen.py</code></pre>
  <h4>关灯</h4>
  <pre><code>$ python ledclose.py</code></pre>
  
  <h3>烟雾传感</h3>
  实时监测，为方便语音合成故报警音频在schh.c。所有在运行schh文件前，需要先开启一个终端运行smoke.py
  <pre><code>$ python smoke.py</code></pre>
  
  <h3> 用人脸作为识别密码</h3>
  my_train.py为使用simpeCV来进行拍取测试者脸型，训练成特定脸型密码，识别率较好。可单独测试。首次运行，路径下若没有任何jpg文件会拍摄一张包含人脸的照片作为伺候运行的识别密码
  <pre><code>$ python my_train.py</code></pre>
  
  <h3> 测周围温湿度</h3>
  结合讯飞文字转语音功能,调用wiringpi进行GPIO控制
  <p>编译</p>
  <pre><code>$ source make.sh</code></pre>
  <p>运行</p>
  <pre><code>$ ./temperature</code></pre>
  
  <h2>GUI界面</h2>
  为方面树莓派触摸屏操作，使用Tkinter编写了button界面,分别控制，开灯关灯，查温湿度，音乐控制等功能 
  <pre><code>$ python button.py</code></pre>
  
  
