import requests
import re 
import time 

import json 
import  df_jihua_13
import shenjihua 
import cookie_yang


# # 下注的参数
# def  BUYHAOMA(buyNumber,money):
#     buyNumber =['0', '3', '4', '5', '7']
#     money=1
#     orders=[]
#     for  i  in  buyNumber :
#         obj = {'odds':'9.99','play':'B5','code':'cqssc'}
#         obj['money']=money # 钱
#         obj['num']='第五球 '+str(i) # 第几个那个号
#         obj['content']=i # 那个号
#         obj['title']='第五球 '+str(i) # 第几个那个号
#         orders.append(obj) # 拼接数组
#     return  orders    
# df_jihua_13.get_url


# # 获取当前下注的期
def now_oder_qihao():
    url ='http://by189.cn/Mobile/Ajax/mobileAllData?lottery_code=all'
    res = requests.get(url,headers=headers)
    # print(res.json()['lottery']['cqssc']['next_phase'])
    qihao_now = res.json()['lottery']['cqssc']['next_phase']
    return qihao_now
    

 

# def is_timebuy():
# 	now = time.localtime()
# 	h = now.tm_hour
# 	m = now.tm_min
# 	#s = now.tm_sec

# 	if h>=22 and h<=23 or h<2:
# 		# 5min 
# 		if m%5>2 and m%5<=3:
            
# 			return True
			
# 	elif h>9 and h<22:
# 		if m%10==2:
# 			return True
			
# 	else:
#          print('休息')
# 	return False
	
# if  __name__ =='__main__':
#     while True:
#         pass
#         try:
#             print(is_timebuy())
#             if is_timebuy():
#                 placeOrder()
#             else:
#                 print('等待')
#                 print('当前时间', time.strftime('%Y-%m-%d %H:%M:%S'))
#                 pass    
#             time.sleep(60)
#         except Exception as e:
#             print(e)    
# 登陆headers_bets
headers={
    'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
}
headers_bets =headers
urls ='http://main.by189.cn/do_login'
params={
    'username': 'defeng001',
    'password': 'defeng701'
}
ss =requests.Session()
html = ss.post(urls,data=params,headers=headers)

JSON_data_History= json.loads(html.text)
filename='cookes.txt'
cookie_yang.save_cookies_lwp(ss.cookies, filename)
print(cookie_yang.load_cookies_from_lwp(filename))
if cookie_yang.load_cookies_from_lwp(filename):
    ss.cookies=cookie_yang.load_cookies_from_lwp(filename)
urls_bets = 'http://main.by189.cn/bets'
# 提交的参数
params_bets={
    'code':'cqssc',
    'drawNumber':now_oder_qihao(),
}
# 拿到数据决定买什么的参数
orders = df_jihua_13.get_url()
# 二次拼接成接口需要的形式
for idnex, item in   enumerate(orders):
    for  kk in item:
        listData = 'orders'+'['+str(idnex)+']'+'['+kk+']'# 拼接出来key
        params_bets[listData]=item[kk] 


params_bets1 =params_bets   # 下单数据    

html = ss.post(urls_bets,data=params_bets1,headers=headers_bets)
JSON_data_History= json.loads(html.text)
if JSON_data_History['status']==1:
    print('下单成功=============='+JSON_data_History['money'])
else:
    print('失败了================'+JSON_data_History['info'])
# time.sleep(120)    
time.sleep(60)    
     
    