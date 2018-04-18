#!/usr/bin/env python3
# -*- coding: utf-8


import time
import re
import requests
import math


def is_timebuy():
	now = time.localtime()
	h = now.tm_hour
	m = now.tm_min
	#s = now.tm_sec

	if h>=22 and h<=23 or h<2:
		# 5min 
		if m%5>=2 and m%5<=3:
			return True
			
	elif h>9 and h<22:
		if m%10>=2 and m%10<=4:
			return True
			
	else:
		pass
		
	return False
	
	
def current_qi():
	#计算当前开的期数
	now = time.localtime()
	h = now.tm_hour
	m = now.tm_min
	#s = now.tm_sec

	qi = 1
	if h<2:
		qi = math.floor(m/5) + h * 12
	elif h>9 and h<22:
		qi = math.floor(m/10) + (h-10) * 6 + 24
	elif h>=22 and h<=23:
		qi = math.floor(m/5) + (h-22) * 12 + 24 + 72
		
	return qi + 1
	
	
if __name__ == '__main__':
	#当前已开哪期
	print(current_qi())
	
	while True:
		try:
			isbuy = is_timebuy()
			if isbuy:
				print('开始买入', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
				r = requests.get('http://www.aapk10.com/Pro/Ajax.php?FunctionNum=2&ObjName=Right1&Runer=1')
				if r.ok:
					pass
					s = r.text
					
					p = re.findall(r'void\(0\);">(.*?)<\/a>', s)
					if p:
						#0点3分时，没有刷出要购买的数据
						p = re.findall(r'\$\("\#NumWill"\)\.html\(\'(.*?)\'\)', s)
						if p:
							p = p[0]
							print(p)
							a, b, c = p.split(' ')
							i = int(a[:3])
							j = int(b[9:][:-1])
							#print(i,j)
							#if c[-1]=='错':
							#	touzhu = pow(2, j-i+1) * 5
							#	print('投注金额', touzhu)
							
							touzhu = pow(2, j-i)
							print([(x, touzhu) for x in b[3:8]])
							
							#购买成功后
							time.sleep(60)
					
			else:
				pass
				#print('时间未到，不买')
				
			time.sleep(10)
		except Exception as e:
			pass
			#print(e)
			#break