raspistill -t 6000 -tl 1000 -o kimyoung_%02d_20_20_200_200.jpg -w 200 -h 200  
# raspistill -vf -hf -o cam2.jpg
# raspivid -o video.h264 -t 10000

# raspistill -o image.jpg -rot 180
# -v：调试信息查看。
# -w：图像宽度
# -h：图像高度
# -rot：图像旋转角度，只支持 0、90、180、270 度
# -o：图像输出地址，例如image.jpg，如果文件名为“-”，将输出发送至标准输出设备
# -t:获取图像前等待时间，默认为5000，即5秒
# -tl：多久执行一次图像抓取。
