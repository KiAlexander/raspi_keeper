#编译64位可执行文件
make clean;make RaspberryPi=1
#设置libmsc.so库搜索路径
export LD_LIBRARY_PATH=~/rasp_voice/libs/RaspberryPi/
sudo modprobe snd_pcm_oss
