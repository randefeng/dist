# https://www.cai2008.com/
# https://www.cai2008.com/m/html/caiyou.html
from bs4 import  BeautifulSoup

import requests
import re 
import time 
import datetime
#设置表头
#设置表头
headers={
    'cookie': '__cfduid=dadb29a65e7d80ccf70a8cc9db818d4ec1521523737; safedog-flow-item=BA08553654C2536340EFFCD6137AB3F0',  
    'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
}
allshenglv =[]
_willBuy_money=2
# 如果不倍投就改 toubei
def formtTOUZHU(toubei):
    # toubei=-100
    if toubei ==1:
        return 2
    elif toubei==2:
        return 1
    elif toubei==3:
        return 0    
    else:
        return 0
        pass   
def formtNum(aa):
    # %字符串无法计算
    new_list = []
    for i in aa :
        new_i = i.replace('%','')
        new_list.append(int(new_i))
        # max(formtNum(allshenglv))
    return str(max(new_list))+'%'


    

    


    #  第二种
_global_dict_url =''    
def  get_url():
    #  在吧最高的去BUY
     _global_dict_url =tow_jihua()
     if _global_dict_url:
        time.sleep(1)
        #  _global_dict_url = 'https://www.cai2008.com/m/html/houyi.html'
        print('loadUal===== ==========',_global_dict_url)
        res = requests.get (_global_dict_url,headers =headers)
        res.encoding = "utf-8"
        if res.status_code ==200:
            dangqiangQIHAO = re.findall('<div class="list_ftbox" id="jihua_now">(.*?)<br>(.*?)<em>(.*?)</em>(.*?)<em>(.*?)</em>(.*?)<em>(.*?)</em></div>',res.text,re.S) 
            linkes =re.findall('<li>(.*?)</li>',res.text,re.S) 
            #  jihua_star = linkes[-1][0:3]
            #  获取要买的号码
            print('linkes',linkes)
            buyhaoma =linkes[-1]
            
            buyhaoma1 = re.findall('【(.*?)】',buyhaoma,re.S)
            _list_willBuyqihao =[]
            print('计划---------------------------',buyhaoma1)
            print('人地址---------------------------',_global_dict_url)
            #  buyhaoma1 = ['23478']
            for  k  in buyhaoma1[0]:
                _list_willBuyqihao.append(k)
            #  获取投注倍数
            jihua_end =linkes[-1][4:7]
            str_qihao =dangqiangQIHAO[0][0]
            qihao = re.findall('第(.*?)期',str_qihao,re.S) 
            
            now_qihao =qihao[0][-3:]
            toubei = int(jihua_end)-int(now_qihao) 
            #  money_yizhu = pow(2,formtTOUZHU(toubei) )*_willBuy_money
            will_buyhao =_list_willBuyqihao
            #  bets = [{"name":int(x),"room_id":"0","lottery_id":"54","issue":'',"method_id":"700005","bet_num":int(x),"odds":'9.980',"bet_money":money_yizhu,"$$hashKey":"object:%d" % (300+i)} for (i,x) in enumerate(will_buyhao)] 
            return {'buyParms':BUYHAOMA(will_buyhao,''),'will_buyhao':will_buyhao}
        else:
            print('get_url--------错误') 
        #  return bets
     else:
        print("计划不稳定，下车")    
        return  ''
def tow_jihua():
    if nowTime() :
        url ='https://www.cai2008.com/index.html'
        res = requests.get (url,headers =headers)
        res.encoding = "utf-8"
        # linkes =re.findall('<a href="(.*?)"><div class="row1">(.*?)</div><div class="row2 jihua_2">(.*?)</div><div class="row3 djihua_2">(.*?)</div><div class="row4 zhong_2">(.*?)</div></a>',res.text,re.S) 
        if res.status_code ==200:
            soup =BeautifulSoup(res.text,'lxml')
            linkes = soup.select('#jihua_data > li > a')
            all_list =[]
            for  linke   in linkes:
                aa =linke.get_text() + ' ' +linke.get('href')
                all_list.append(aa)
            aa =all_list
            getMAXLIST= []
            for x in aa:
                getMAXLIST.append(int(x[x.index('率')+1:x.index('率')+4].replace('%','')))
            _gatMAX= max(getMAXLIST)
            print("胜率：",_gatMAX)
            if int(_gatMAX)>94:
                get_good_url =max([ (x[x.index('率')+1:x.index('率')+4].replace('%',''), x[x.index('率')+5:])  for x in aa], key=lambda x:int(x[0]))[1] 
                return 'https://www.cai2008.com/m/html'+get_good_url.strip()
            else:
                return  ''
        # return _global_dict_url
        else:
            print('tow_jihua--------错误')
def nowTime():
    nowTime=datetime.datetime.now().strftime('%M')#现在
    if int(nowTime) <4:
            
        return True
    else:
        return True
# 下注的参数
def  BUYHAOMA(buyNumber,money):
    # buyNumber =['0', '3', '4', '5', '7']
    # money=1
    print('buyNumber=================',buyNumber)
    orders=[]
    for  i  in  buyNumber :
        obj = {'odds':'9.99','play':'B5','code':'cqssc'}
        obj['money']='外边不填写' # 钱
        obj['num']='第五球 '+str(i) # 第几个那个号
        obj['content']=i # 那个号
        obj['title']='第五球 '+str(i) # 第几个那个号
        orders.append(obj) # 拼接数组
    return  orders 
if  __name__ =='__main__':
    get_url()
   
        



           