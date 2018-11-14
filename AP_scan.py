#！/usr/bin/python3
# -*- coding:utf-8 -*-
# spwpun
import time
import pywifi
from pywifi import const

'''
扫描并显示当前的无线AP信息
'''
def getAPInfo():
	wifi = pywifi.PyWiFi()
	iface = wifi.interfaces()[0]
	iface.disconnect()
	iface.scan()
	time.sleep(3)
	bsses = iface.scan_results()#这里bsses是list，list中的每一项是pywifi的Profile类型
	return bsses

'''
测试当前无线网卡是否连接
'''
def iface_status():
	wifi = pywifi.PyWiFi()
	iface = wifi.interfaces()[0]
	if iface.status() == const.IFACE_CONNECTED:
		print("网络已连接...")
	else:
		print("网络未连接...")

if __name__ == "__main__":
	iface_status()
	bsses = []
	bsses = getAPInfo()
	for bss in bsses:
		name = bss.ssid.encode("raw_unicode_escape").decode("utf-8")#这里是为了解决中文乱码的问题，在win下可以，在linux下仍然不行
		print("MAC:%s SIGNAL:%ddBm WIFI:%s"%(bss.bssid[:-1],bss.signal,name))