### AP_scan
扫描附近WiFi信息
- 使用```pywifi```第三方库
- ```python3```环境
- ```.interfaces()[0]```获取本机的无线网卡，我在我的linux双系统上使用的时候，出现了一个很奇怪的网卡，需要选择第二个，也就是把代码改为```.interfaces()[1]```,但是在我的windows下面直接使用[0]就可以
- 另外在linux下安装pywifi模块的时候，要注意看看wpa_supplicant是否配置好，查看目录```/usr/run/wpa_suppplicamt```
