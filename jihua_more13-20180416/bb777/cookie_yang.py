#/usr/bin/env python3
# -*- coding: utf-8 -*-

''' 模拟下单
http://cn.python-requests.org/zh_CN/latest/user/quickstart.html
http://cn.python-requests.org/zh_CN/latest/user/advanced.html
操作cookie
https://stackoverflow.com/questions/13030095/how-to-save-requests-python-cookies-to-a-file

2018.02.02 '''

__author__ = 'swYang'

import requests
# import time
import os
# from urllib.parse import urlparse
# from contextlib import closing
# import re
# import json


import pickle
def save_cookies(requests_cookiejar, filename):
	with open(filename, 'wb') as f:
		pickle.dump(requests_cookiejar, f)

def load_cookies(filename):
	with open(filename, 'rb') as f:
		return pickle.load(f)



# import cookielib
import http.cookiejar
def save_cookies_lwp(cookiejar, filename):
	lwp_cookiejar = http.cookiejar.LWPCookieJar()
	for c in cookiejar:
		args = dict(vars(c).items())
		args['rest'] = args['_rest']
		del args['_rest']
		c = http.cookiejar.Cookie(**args)
		lwp_cookiejar.set_cookie(c)
	lwp_cookiejar.save(filename, ignore_discard=True)

def load_cookies_from_lwp(filename):
	if not os.path.isfile(filename):
		return None
	lwp_cookiejar = http.cookiejar.LWPCookieJar()
	lwp_cookiejar.load(filename, ignore_discard=True)
	return lwp_cookiejar

if __name__ == '__main__':
	headers = {'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1'}
	url = 'http://www.baidu.com/'
	filename = 'z0.txt'
	#save human-readable
	#r = requests.get(url, headers=headers)
	#save_cookies_lwp(r.cookies, filename)
	#print(r.cookies)
	#print(r.request.headers)

	#you can pass a LWPCookieJar directly to requests
	#r = requests.get(url, cookies=load_cookies_from_lwp(filename), headers=headers)
	#print(r.cookies)
	#print(r.request.headers)


	#save cookies
	#r = requests.get(url, headers=headers)
	#save_cookies(r.cookies, filename)
	#print(r.cookies)
	#print(r.request.headers)

	#load cookies and do a request
	r = requests.get(url, cookies=load_cookies(filename), headers=headers)
	print(r.cookies)
	print()
	print(r.request.headers)