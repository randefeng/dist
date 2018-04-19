
# get_links()调用
from bs4 import  BeautifulSoup

import requests
import re 
import time 
#设置表头
headers={  
    'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
}

info_lists =[]
dr = re.compile(r'<[^>]+>',re.S)
buyMoney = 1
# 获取到页面上的数据_LIST
def  get_info (url) :
     url ='http://www.shenjihua.cc/jihua/11955.html'
     print('url===用============',url)
     res = requests.get (url)
     _LIST = []
     linkes =re.findall('<p>(.*?)</p>',res.text,re.S) 
     for  rank  in linkes:
          dd = dr.sub('',rank)
          splic_data =dd.split(' ')

         
          _LIST.append(splic_data)
     aa =_LIST
     return  BUYHAOMA(analysis(aa),beishu(aa)) 

    #  bets[0]['issue'] ='1001011'
# 解析把药买的号返回 这个是做平买方便
def analysis(myList):
    willBuy_data = myList[0][3].split('：')
      
    
    info_lis = willBuy_data[-1].split(',')
    info_lis_new =[]
    for  k  in  info_lis:
        info_lis_new.append(int(k))
    return  info_lis_new
# 解析把药买的号返回 这个是做平买方便
def beishu(aa):
    # print('aa=========',aa)
    num =0
    if aa[1][-1]=='挂':
        print(aa[1])
        num =num+1
        print(num)
        if aa[2][-1]=='挂':
            num=num+1
            if aa[3][-1]=='挂':
                num=num+1
                if aa[4][-1]=='挂':
                    num=num+1
                    if aa[5][-1]=='挂':
                        num=num+1
                        if aa[5][-1]=='挂':
                           num=num+1
    return num
    # return  willBuy_data[-1].split(',')

# 最多追4次,根据数据返回要买多少倍
def more4QI(myList):
    # 是否中了
    isWinning = myList[1][-1]
    isWinning2 = myList[2][-1]
    starQihao = int(myList[0][0][0:3])
    endQihao  = int(myList[0][5][0:3])
    # buyToubei =endQihao
    isbeiTou =0
    if isWinning =='中':
        isbeiTou= 0
    else:
        isbeiTou= 2
    if isWinning2!='中':
        isbeiTou=0

    beilvNum = endQihao-starQihao 
    buyBeilvNum = pow(2, beilvNum) * buyMoney
    return  buyBeilvNum
    
    willBuy_data = myList[0][4].split(':')
    # print(willBuy_data)
    return  willBuy_data[-1].split(',')

# 获取网站的第一个计划
def  get_links():     
     web_data = requests.get('http://www.shenjihua.cc/jihua-catid-8-areaid-2-jhms-5.html',headers =headers)
     soup =BeautifulSoup(web_data.text,'lxml')
     linkes = soup.select('body > div > div > ul > li:nth-of-type(1) > a')
     print(linkes[1].get('href'))
     url =linkes[1].get('href')
    #  print('url===============',url)
     return get_info(url)

# 下注的参数
def  BUYHAOMA(buyNumber,money):
    # buyNumber =['0', '3', '4', '5', '7']
    # money=1
    print('buyNumber=================',buyNumber)
    # print('money=================',money)
    orders=[]
    for  i  in  buyNumber :
        obj = {'odds':'9.99','title':'单号', 'play':'B1','code':'bjpk10'}
        obj['money']=pow(2,money)*buyMoney # 钱
        obj['num']='冠军 '+str(int(i)) # 第几个那个号
        obj['content']=int(i) # 那个号
        obj['check']='true' # 那个号
        orders.append(obj) # 拼接数组
    return   {
        'buyParms': orders,
        'will_buyhao':buyNumber
    }

if __name__ == '__main__':
    print(get_links())
    
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
    
   
