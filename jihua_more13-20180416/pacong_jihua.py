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
buyMoney = 20
# 获取到页面上的数据_LIST
def  get_info (url) :
    #  url ='http://www.shenjihua.cc/jihua/9574.html'
     res = requests.get (url)
     _LIST = []
     linkes =re.findall('<p>(.*?)</p>',res.text,re.S) 
     for  rank  in linkes:
          dd = dr.sub('',rank)
          splic_data =dd.split(' ')
          _LIST.append(splic_data)
        #  case {'buyHao': ['4', '5', '6', '3', '1'], 'buyBeishu': 4} 700005代表个位
    #  return {'buyHao':analysis(_LIST),'ge':'700005','buyBeishu':1} 个位平买
    #  return {'buyHao':analysis(_LIST),'ge':'700005','money':more4QI(_LIST)}
     b = {'buyHao':analysis(_LIST),'ge':'700005','money':more4QI(_LIST),'odds':'9.980'}
     bets = [{"name":int(x),"room_id":"0","lottery_id":"54","issue":'',"method_id":b['ge'],"bet_num":int(x),"odds":b['odds'],"bet_money":b['money'],"$$hashKey":"object:%d" % (300+i)} for (i,x) in enumerate(b['buyHao'])]
    #  bets[0]['issue'] ='1001011'
      
     return bets
# 解析把药买的号返回 这个是做平买方便
def analysis(myList):
    print(myList[0])
    willBuy_data = myList[0][4].split(':')
    print(willBuy_data)
    return  willBuy_data[-1].split(',')


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
     print('url===============',url)
     
     return get_info(url)














# if __name__ == '__main__':
#     print(get_links())
#     url ='http://www.shenjihua.cc/jihua/9457.html'
    # while True:
    #     pass
    #     try:
    #         get_links()
    #         time.sleep(10)
    #     except Exception as e:
    #         pass
    #         print(e)
    
   
  
