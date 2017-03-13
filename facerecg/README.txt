opencv:

$ sudo apt-get install python-pip
$ sudo apt-get install python-dev
$ sudo pip install picamera

$ sudo apt-get update
$ sudo apt-get upgrade
$ sudo pip install build-essential cmake pkg-config python-dev libgtk2.0-dev libgtk2.0 zlib1g-dev libpng-dev libjpeg-dev libtiff-dev libjasper-dev libavcodec-dev swig unzip

$ wget http://downloads.sourceforge.net/project/opencvlibrary/opencv-unix/2.4.9/opencv-2.4.9.zip
$ unzip opencv-2.4.9.zip

$ cd opencv-2.4.9
$ cmake -DCMAKE_BUILD_TYPE=RELEASE -DCMAKE_INSTALL_PREFIX=/usr/local -DBUILD_PERF_TESTS=OFF -DBUILD_opencv_gpu=OFF -DBUILD_opencv_ocl=OFF

make

sudo make install

$ python
>>> import cv2
>>> cv2.__version__
'2.4.9'


	
simplecv:

$ sudo apt-get install ipython python-opencv python-scipy python-numpy python-pygame python-setuptools python-pip

$ sudo pip install https://github.com/sightmachine/SimpleCV/zipball/develop

如果运行SimpleCV提示缺少相应的组件，也可以通过pip指令进行安装，如笔者在运行时提示缺少svgwirte。
$ sudo pip install svgwrite