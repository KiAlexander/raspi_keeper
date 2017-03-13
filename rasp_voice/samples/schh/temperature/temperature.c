#include <wiringPi.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h> 
#include <unistd.h>

#include "qtts.h"
#include "msp_cmn.h"
#include "msp_errors.h"

#define BUFFER_SIZE 4096
#define FRAME_LEN   640 
#define HINTS_SIZE  100

//不同的声卡有着不同的播放参数，这些参数可以使用file命令获得

#define Sample_Size 16 //there're two kinds of bits,8 bits and 16 bits

#define Sample_Rate 16000 //sampling rate

#define MAX_TIME 85
#define DHT11PIN 3
#define ATTEMPTS 5                 //retry 5 times when no response
int dht11_val[5]={0,0,0,0,0};
 
/* wav音频头部格式 */
typedef struct _wave_pcm_hdr
{
    char            riff[4];                // = "RIFF"
    int     size_8;                 // = FileSize - 8
    char            wave[4];                // = "WAVE"
    char            fmt[4];                 // = "fmt "
    int     fmt_size;       // = 下一个结构体的大小 : 16

    short int       format_tag;             // = PCM : 1
    short int       channels;               // = 通道数 : 1
    int     samples_per_sec;        // = 采样率 : 8000 | 6000 | 11025 | 16000
    int     avg_bytes_per_sec;      // = 每秒字节数 : samples_per_sec * bits_per_sample / 8
    short int       block_align;            // = 每采样点字节数 : wBitsPerSample / 8
    short int       bits_per_sample;        // = 量化比特数: 8 | 16

    char            data[4];                // = "data";
    int     data_size;              // = 纯数据长度 : FileSize - 44 
} wave_pcm_hdr;

/* 默认wav音频头部数据 */
wave_pcm_hdr default_wav_hdr = 
{
    { 'R', 'I', 'F', 'F' },
    0,
    {'W', 'A', 'V', 'E'},
    {'f', 'm', 't', ' '},
    16,
    1,
    1,
    16000,
    32000,
    2,
    16,
    {'d', 'a', 't', 'a'},
    0  
};
/* 文本合成 */
int text_to_speech(const char* src_text, const char* des_path, const char* params)
{
    int          ret          = -1;
    FILE*        fp           = NULL;
    const char*  sessionID    = NULL;
    unsigned int audio_len    = 0;
    wave_pcm_hdr wav_hdr      = default_wav_hdr;
    int          synth_status = MSP_TTS_FLAG_STILL_HAVE_DATA;

    if (NULL == src_text || NULL == des_path)
    {
        printf("params is error!\n");
        return ret;
    }
    fp = fopen(des_path, "wb");
    if (NULL == fp)
    {
        printf("open %s error.\n", des_path);
        return ret;
    }
    /* 开始合成 */
    sessionID = QTTSSessionBegin(params, &ret);
    if (MSP_SUCCESS != ret)
    {
        printf("QTTSSessionBegin failed, error code: %d.\n", ret);
        fclose(fp);
        return ret;
    }
    ret = QTTSTextPut(sessionID, src_text, (unsigned int)strlen(src_text), NULL);
    if (MSP_SUCCESS != ret)
    {
        printf("QTTSTextPut failed, error code: %d.\n",ret);
        QTTSSessionEnd(sessionID, "TextPutError");
        fclose(fp);
        return ret;
    }
    printf("正在合成 ...\n");
    fwrite(&wav_hdr, sizeof(wav_hdr) ,1, fp); //添加wav音频头，使用采样率为16000
    while (1) 
    {
        /* 获取合成音频 */
        const void* data = QTTSAudioGet(sessionID, &audio_len, &synth_status, &ret);
        if (MSP_SUCCESS != ret)
            break;
        if (NULL != data)
        {
            fwrite(data, audio_len, 1, fp);
            wav_hdr.data_size += audio_len; //计算data_size大小
        }
        if (MSP_TTS_FLAG_DATA_END == synth_status)
            break;
        printf(">");
        usleep(150*1000); //防止频繁占用CPU
    }//合成状态synth_status取值请参阅《讯飞语音云API文档》
    printf("\n");
    if (MSP_SUCCESS != ret)
    {
        printf("QTTSAudioGet failed, error code: %d.\n",ret);
        QTTSSessionEnd(sessionID, "AudioGetError");
        fclose(fp);
        return ret;
    }
    /* 修正wav文件头数据的大小 */
    wav_hdr.size_8 += wav_hdr.data_size + (sizeof(wav_hdr) - 8);
    
    /* 将修正过的数据写回文件头部,音频文件为wav格式 */
    fseek(fp, 4, 0);
    fwrite(&wav_hdr.size_8,sizeof(wav_hdr.size_8), 1, fp); //写入size_8的值
    fseek(fp, 40, 0); //将文件指针偏移到存储data_size值的位置
    fwrite(&wav_hdr.data_size,sizeof(wav_hdr.data_size), 1, fp); //写入data_size的值
    fclose(fp);
    fp = NULL;
    /* 合成完毕 */
    ret = QTTSSessionEnd(sessionID, "Normal");
    if (MSP_SUCCESS != ret)
    {
        printf("QTTSSessionEnd failed, error code: %d.\n",ret);
    }

    return ret;
}

int dht11_read_val(){
    uint8_t lststate=HIGH;         //last state
    uint8_t counter=0;
    uint8_t j=0,i;
    for(i=0;i<5;i++)
        dht11_val[i]=0;
       
    //host send start signal    
    pinMode(DHT11PIN,OUTPUT); 
    digitalWrite(DHT11PIN,HIGH); 
    printf(" %d.\n",digitalRead(DHT11PIN));

    delay(100);
    digitalWrite(DHT11PIN,LOW);    //set to low at least 18ms 
    delay(18);
    digitalWrite(DHT11PIN,HIGH);   //set to high 20-40us
    delayMicroseconds(40);
    
    //start recieve dht response
    pinMode(DHT11PIN,INPUT);       //set pin to input
    for(i=0;i<MAX_TIME;i++)         
    {
        counter=0;
        while(digitalRead(DHT11PIN)==lststate){     //read pin state to see if dht responsed. if dht always high for 255 + 1 times, break this while circle
            counter++;
            delayMicroseconds(1);
            if(counter==255)
                break;
        }
        lststate=digitalRead(DHT11PIN);             //read current state and store as last state. 
        if(counter==255)                            //if dht always high for 255 + 1 times, break this for circle
            break;
        // top 3 transistions are ignored, maybe aim to wait for dht finish response signal
        if((i>=4)&&(i%2==0)){
            dht11_val[j/8]<<=1;                     //write 1 bit to 0 by moving left (auto add 0)
            if(counter>16)                          //long mean 1
                dht11_val[j/8]|=1;                  //write 1 bit to 1 
            j++;
        }
    }
    // verify checksum and print the verified data
    if((j>=40)&&(dht11_val[4]==((dht11_val[0]+dht11_val[1]+dht11_val[2]+dht11_val[3])& 0xFF))){
        printf("RH:%d.%d %%,TEMP:%d.%d \n",dht11_val[0],dht11_val[1],dht11_val[2],dht11_val[3]);
        return 1;
    }
    else
        return 0;
}

int main(void)
{
    int         ret                  = MSP_SUCCESS;
    const char* login_params         = "appid = 57c2c563, work_dir = .";//登录参数,appid与msc库绑定,请勿随意改动

    const char* session_begin_params = "voice_name = yefang, text_encoding = utf8, sample_rate = 16000, speed = 50, volume = 50, pitch = 50, rdn = 2";
    const char* filename             = "my_temperature.wav"; //合成的语音文件名称
   
    ret = MSPLogin(NULL, NULL, login_params);//第一个参数是用户名，第二个参数是密码，第三个参数是登录参数，用户名和密码可在http://open.voicecloud.cn注册获取
    if (MSP_SUCCESS != ret)
    {
        printf("MSPLogin failed, error code: %d.\n", ret);
        goto exit ;//登录失败，退出登录
    }


    //pinMode(DHT11PIN,INPUT); 

    int attempts=ATTEMPTS;
    if(wiringPiSetup()==-1)
       exit(1);
    while(attempts)
    {                        //you have 5 times to retry
        int success = dht11_read_val();     //get result including printing out
        if (success) {                      //if get result, quit program; if not, retry 5 times then quit
            break;
        }
        attempts--;
        delay(1000);
    }
    printf("开始测温湿度。。。\n");
    
    char _answer_[BUFFER_SIZE];
    sprintf(_answer_,"您周围环境的湿度是百分之%d，温度是%d摄氏度\n",dht11_val[0],dht11_val[2]);
    printf("%d\n",attempts);
    printf("%s\n",_answer_);

    printf("开始合成 ...\n");
        
    ret = text_to_speech(_answer_, filename, session_begin_params);
    if (MSP_SUCCESS != ret)
    {
         printf("text_to_speech failed, error code: %d.\n", ret);
    }
    printf("合成完毕\n");

    system("omxplayer --no-osd -no-keys my_temperature.wav"); 
exit:
    MSPLogout(); //退出登录

    return 0;
}
