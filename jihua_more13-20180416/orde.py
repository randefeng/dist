#/usr/bin/env python3
# -*- coding: utf-8 -*-

''' 模拟下单
http://cn.python-requests.org/zh_CN/latest/user/quickstart.html
http://cn.python-requests.org/zh_CN/latest/user/advanced.html
操作cookie
https://stackoverflow.com/questions/13030095/how-to-save-requests-python-cookies-to-a-file

linux下后台运行
nohup python3 -u order.py > out.log 2>&1 &

2018.02.02 '''

__author__ = 'swYang'

import requests
import time
import os
import sys
from urllib.parse import urlparse, parse_qs, quote, unquote
from contextlib import closing
import re
import pickle
import json
import cookie_yang
from PIL import Image
from io import BytesIO
import random
import when
import execjs
import platform

import pacong_jihua
import df_jihua_13
# 模拟浏览器user-agent
headers = dict()
headers['user-agent'] = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11'

headers3 = dict()
headers3['user-agent'] = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11'


# 默认的超时时间
TIMEOUT = 5

# 规定最大重试次数
MAXRETRYCOUNT = 5

URL = 'https://pg.kangddoscdn.com'


meimaine = True
balance = 0
YICITOU = 1
BEISHU = 9.85
WINMONEY = int(40 * (YICITOU * BEISHU - YICITOU * 5))

def take_action():	
	global meimaine
	global balance
	
	if not meimaine:
		if time.localtime().tm_min%5 ==0 or time.localtime().tm_min%5==1:
			# 整点后回复
			meimaine = True
			
	if time.localtime().tm_hour>=3 and (time.localtime().tm_hour<=9 and time.localtime().tm_min<=50):
		print('休息中', time.strftime('%Y-%m-%d %H:%M:%S'))
		return
	# take action
	# captcha  = 'z0.jpg'
	filename = 'z0.txt'
	filename3 = 'z3.txt'
	s = requests.Session()
    
	if cookie_yang.load_cookies_from_lwp(filename):
		s.cookies=cookie_yang.load_cookies_from_lwp(filename)
    


	
	if headers:
		s.headers=headers


	url = URL + '/#/tab/account'
	r = s.get(url)
	# print(r.cookies)
	# print()
	# print(r.request.headers)

	# print(s.cookies)

	#查询是否已登录
	url = URL + '/controller/user/get/get_user_info/172272?version=1.0.0'# + str(random.random() * 10000)
	payload = {}
	r = s.post(url, data=payload, headers={"Accept":"*/*","X-Requested-With":"XMLHttpRequest"})
	# print(r.cookies)
	# print()
	# print(r.request.headers)
	#print(r.content)
	#sys.exit(0)
	# print(r.text)
	# open('z0.html', 'w').write(r.text)
	#print(r.json())
	#sys.exit(0)

	# print(s.cookies)

	#print(r.json()['success'])
	
	print(11111111111111111111111)
	if r.json()['success']:
		print('当前在线', time.strftime('%Y-%m-%d %H:%M:%S'))
		print('当前账户资金：', r.json()['data']['money'])
		if balance == 0:
			balance = float(r.json()['data']['money'])
		else:
			if float(r.json()['data']['money']) - balance >= WINMONEY:
				print('今日目标已达成！！！')
				sys.exit(0)

		#sys.exit(0)
		#查询是否已登录
		#url = 'https://xccp456.com/xinCaiCPLoginWeb/app/playHoldem?' + str(random.random() * 10000)
		#payload = {"product":"LOTTERY_IG","type":"2","line":"2"}
		#r = s.post(url, data=json.dumps(payload), headers={"Accept":"application/json, text/javascript, */*; q=0.01","X-Requested-With":"XMLHttpRequest","Content-Type":"application/json","Referer":"https://xccp456.com/xinCaiCPLoginWeb/app/home?l=0","Origin":"https://xccp456.com"})
		# print(r.cookies)
		# print()
		# print(r.request.headers)
		# print(r.content)
		# print(r.text)
		# open('z0.html', 'w').write(r.text)
		# print(r.json())

		# print(s.cookies)
		#print(r.json()['success'])
		#if r.json()['success']:
		if True:
			
			#filename2 = 'z1.txt'
			#s2 = requests.Session()

			#if cookie_yang.load_cookies_from_lwp(filename2):
			#	s2.cookies=cookie_yang.load_cookies_from_lwp(filename2)

			#if headers:
			#	s2.headers=headers


			#url = r.json()['link']
			# 这边有个坑，访问这个url会返回一个网页，加点参数后 location.href
			#url += '&mobileVersion=new'
			#print('url', url)
			#sessionId = parse_qs(urlparse(url).query)['code'][0]
			#print('sessionId', sessionId)
			#url_count = 0
			#while True:
			#	try:
			#		r = s2.get(url)
			#		#r = s2.get(url)
			#		#print('r.url', r.url)
			#		#print('111', r.cookies)
			#		# print()
			#		#print('222', r.request.headers)

			#		#print('333', s2.cookies)
			#		cookie_yang.save_cookies_lwp(s2.cookies, filename2)
			#		#print('--------------')
			#		#print(r.text)
			#		#print('--------------')
			#		break
			#	except Exception as e:
			#		pass
			#		print(e)
			#		url_count += 1
			#		if url_count > 8:
			#			break
			#		time.sleep(0.4)

			##查询结果
			#last_url = url
			#netloc = urlparse(url).netloc
			
			isbuy = when.is_timebuy()
			if True:
				while True:
					url = URL + '/controller/lottery?version=1.0.0'
					payload = {"command":"lottery_request_transmit_v2","param": '{"room_id":"0","lottery_id":"54","method_ids":"700005,700010","command_id":602}'}
					r = s.post(url, data=payload, headers={"Accept":"*/*","X-Requested-With":"XMLHttpRequest","Content-Type":"application/x-www-form-urlencoded; charset=UTF-8"})#,"Origin":"https://ssc.kigfan.com"})
					# print(r.cookies)
					# print()
					#print(r.request.headers)
					#print(r.content)
					#print(r.text)
					#print(r.json())
					#print(r.status_code)
					if r.status_code == 200:
						#open('z0.html', 'w').write(r.text)
						# print(r.json())
						#print(r.json()['sessionId'])
						
						# print(s2.cookies)

						try:
							#print(r.json()['data']['700005'][0])
							#print(r.json()['odds']['BALL_1']['SMALL'])
							BIG_PEILV = r.json()['data']['700005']['1']
							SMA_PEILV = r.json()['data']['700010']['1']
							print(BIG_PEILV)

							# cq shishicai 
							# r = requests.get('http://caipiao.163.com/t/awardlist.html?gameEn=ssc&pageNums=30&pageNo=1&cache=', headers=headers)
							# if r.status_code == 200:
							# 	a = r.json()['list']
							# 	t = time.strftime('%Y%m%d')[2:]
							# 	a = list(filter(lambda x:x['period'].startswith(t), a))
								
							# 	print(a)

							
							# sys.exit(0)

							while True:
								try:
									print('尝试买入第', when.current_qi(), '期', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
									isbuy = when.is_timebuy()
									if isbuy and meimaine:
										print('开始买入', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
										s3 = requests.Session()
										
										if cookie_yang.load_cookies_from_lwp(filename3):
											s3.cookies=cookie_yang.load_cookies_from_lwp(filename3)

										if headers:
											s3.headers=headers3
											
										r = s3.get('http://www.aapk10.com/Pro/Ajax.php?FunctionNum=2&ObjName=Right1&Runer=1')#, headers={'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36', 'host':'www.aapk10.com'})
										if r.ok:
											pass
											ss = r.text
											
											if ss.find("var url='';") > -1:
												ss2 = ss.replace('<html><body><script language="javascript">', 'function get_url(){').replace(';window.location=url;</script></body></html>', 'return url;}')
												ss3 = execjs.compile(ss2)
												new_url = ss3.call('get_url')
												print('http://www.aapk10.com' + new_url)
												r = s3.get('http://www.aapk10.com' + new_url)#, headers={'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36', 'host':'www.aapk10.com'})
												print(r.request.headers)
												print(r.headers)
												print(s3.cookies)
												ss = r.text
												print(ss)
												
											cookie_yang.save_cookies_lwp(s3.cookies, filename3)
											
											p = re.findall(r'void\(0\);">(.*?)<\/a>', ss)
											if True:#p:
												#0点3分时，没有刷出要购买的数据
												p = re.findall(r'\$\("\#NumWill"\)\.html\(\'(.*?)\'\)', ss)
												
												print('p==========',p)
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
													
													touzhu = pow(2, j-i) * YICITOU
													current_qi = when.current_qi() 
													issue = "%s%03d" % (time.strftime('%Y%m%d'), current_qi)

													# 从写B
													# b =pacong_jihua.get_links()
													# print('===1=========',b)

													# 从写bets
													# bets = [{"name":int(x),"room_id":"0","lottery_id":"54","issue":issue,"method_id":"700005","bet_num":int(x),"odds":str(BIG_PEILV),"bet_money":2,"$$hashKey":"object:%d" % (300+i)} for (i,x) in enumerate(b)] 
													# bets = pacong_jihua.get_links()
													try:
														bets = df_jihua_13.get_url()
													except Exception as e:
														print('计划出错==========================',e)	
														# return
													for index, item in enumerate(bets):
														bets[index]['issue'] = issue
													
													print('============',bets)
													#{"bet_info":[{"name":0,"room_id":"0","lottery_id":"54","issue":"20180307102","method_id":"700005","bet_num":0,"odds":"9.980","bet_money":1,"$$hashKey":"object:572"},{"name":3,"room_id":"0","lottery_id":"54","issue":"20180307102","method_id":"700005","bet_num":3,"odds":"9.980","bet_money":1,"$$hashKey":"object:573"},{"name":4,"room_id":"0","lottery_id":"54","issue":"20180307102","method_id":"700005","bet_num":4,"odds":"9.980","bet_money":1,"$$hashKey":"object:574"},{"name":5,"room_id":"0","lottery_id":"54","issue":"20180307102","method_id":"700005","bet_num":5,"odds":"9.980","bet_money":1,"$$hashKey":"object:575"},{"name":7,"room_id":"0","lottery_id":"54","issue":"20180307102","method_id":"700005","bet_num":7,"odds":"9.980","bet_money":1,"$$hashKey":"object:576"}],"command_id":601}
													bets = json.dumps({"bet_info":bets,"command_id":601})
													
													# print('模拟下单成功')
													# return
													
													# 真实下单
													url = URL + '/controller/lottery?version=1.0.0'
													payload = {"command":"lottery_logon_request_transmit_v2","param":""}
													# [["SMALL","BALL_1","1",1.98]]
													# [["BIG","BALL_1","5",1.98]]
													payload["param"] = bets
													r = s.post(url, data=payload, headers={"Accept":"*/*","X-Requested-With":"XMLHttpRequest","Content-Type":"application/x-www-form-urlencoded; charset=UTF-8"})#,"Origin":"https://ssc.kigfan.com"})
													# print(r.cookies)
													# print()
													#print(r.request.headers)
													# print(r.content)
													# print(r.text)
													# open('z0.html', 'w').write(r.text)
													print(r.json())
													print(r.json()['success'])
													print(r.json()['data']['success_count'])
													# print(s2.cookies)

													print('下单成功')
													
													meimaine = False
													
													#购买成功后
													time.sleep(30)
											
									else:
										pass
										#print('时间未到，不买')
										
									time.sleep(3)
									break
								except Exception as e:
									pass
									print(e)
									#break

							return
							
							#下注
							#last_url = url
							url = 'https://ssc.kigfan.com/lotteryweb/WebClientAgent'
							payload = {"command":"BET","sessionId": sessionId,"oddsAdapt":"true","bets":"","gameType":"SSC","timestamps":str(int(time.time()*1000)),"hasPlayerInfo":"true"}
							# [["SMALL","BALL_1","1",1.98]]
							# [["BIG","BALL_1","5",1.98]]
							payload["bets"] = '[["BIG","BALL_5","5",'+ BIG_PEILV +']]'
							r = s2.post(url, data=payload, headers={"Accept":"*/*","X-Requested-With":"XMLHttpRequest","Content-Type":"application/x-www-form-urlencoded","Referer": last_url,"Origin":"https://ssc.kigfan.com"})
							# print(r.cookies)
							# print()
							print(r.request.headers)
							# print(r.content)
							# print(r.text)
							# open('z0.html', 'w').write(r.text)
							print(r.json())
							print(r.json()['sessionId'])
							# print(s2.cookies)

							print('下单成功')

							break
						except KeyError as e:
							# pass
							time.sleep(10)



	else:
		print('已掉线', time.strftime('%Y-%m-%d %H:%M:%S'))

		if platform.system() == 'Linux':
			pass
			sys.exit(0)
		# 重新登录
		#url = 'https://xccp456.com/xinCaiCPLoginWeb/app/checkCode/image'
		#r = s.get(url)
		# print(r.cookies)
		# print()
		# print(r.request.headers)
		# with open(captcha, 'wb') as f:
		# 	f.write(r.content)
		#im = Image.open(BytesIO(r.content))
		#im.show()

		#captcha_txt = input('enter img captcha:')
		#if captcha_txt == '':
		#	print('未输入有效验证码，退出')
		#	sys.exit(0)

		url = URL + '/login?version=1.0.0'# + str(random.random() * 10000)
		payload = {
			"user_name":"defeng","password":"defeng701","url":quote('手机客户端')
		}
		r = s.post(url, data=payload, headers={"Accept":"*/*","X-Requested-With":"XMLHttpRequest","Content-Type":"application/x-www-form-urlencoded; charset=UTF-8"})
		# print(r.cookies)
		# print()
		# print(r.request.headers)
		# print(r.content)
		# print(r.text)
		# open('z0.html', 'w').write(r.text)
		# print(r.json())

		# print(s.cookies)
		print(r.json()['success'])
		if r.json()['success']:
			print('登录成功')
			cookie_yang.save_cookies_lwp(s.cookies, filename)
			time.sleep(5)
			take_action()
		else:
			print(r.json()['message'])

if __name__ == '__main__':
	#获取ping值，取最快IP
	r = requests.post('https://pg.kangddoscdn.com/api/line', headers=headers)
	if r.ok:
		try:
			print(r.json())
			URL = r.json()[1]
		except Exception as e:
			pass
			
	URL = 'https://pg11t.com'
	print('当前采用路线：', URL)
	
	#sys.exit(0)
	while True:
		pass
		try:
			take_action()
			time.sleep(30)
		except Exception as e:
			pass
			print(e)