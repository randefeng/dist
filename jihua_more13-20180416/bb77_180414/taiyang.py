
# get_links()调用
from bs4 import  BeautifulSoup

import requests
import re 
import time 
#设置表头
headers={  
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
}

info_lists =[]
dr = re.compile(r'<[^>]+>',re.S)
buyMoney = 1
# 获取到页面上的数据_LIST
def  get_info () :
     print('loadUal=====https://www.888888e.com==========')
     url ='https://www.888888e.com/api.php?type='
     res = requests.get (url, headers=headers)
     _LIST = []
     linkes =re.findall('<b>(.*?)</b>',res.text,re.S) 
     linkes_data =re.findall('【(.*?)】',str(linkes),re.S) 
     buydata = list(linkes_data[0])
     aa =buydata
     return  BUYHAOMA(aa,aa) 

    #  bets[0]['issue'] ='1001011'

# 下注的参数
def  BUYHAOMA(buyNumber,money):
    # buyNumber =['0', '3', '4', '5', '7']
    # money=1
    print('buyNumber=================',buyNumber)
    # print('money=================',money)
    orders=[]
    for  i  in  buyNumber :
        obj = {'odds':'9.99','play':'B5','code':'cqssc'}
        obj['money']='' # 钱
        obj['num']='第五球 '+str(i) # 第几个那个号
        obj['content']=i # 那个号
        obj['title']='第五球 '+str(i) # 第几个那个号
        orders.append(obj) # 拼接数组
    return   {
        'buyParms': orders,
        'will_buyhao':buyNumber
    }

if __name__ == '__main__':
    print(get_info())
    
#     url ='http://www.shenjihua.cc/jihua/9457.html'
    # while True:
    #     pass
    #     try:
    #         print(1)
    #         time.sleep(10)
    #         print(22)
    #     except Exception as e:
    #         pass
    #         print(e)
    
   
