

import requests 
import time 
import json 
import re 
from bs4 import  BeautifulSoup


def   get_info():
        urls ='https://kaijiang.aicai.com/open/kcResultByDate.do'
        headers  ={
            'Cookie':'UM_distinctid=161266b65356-0958e361f0e22e-178123e-100200-161266b653678; VUID=C56175353A7A476FA18522D9D106AA8C; AUM=dgOjPy-jfJATT9M78LMCDz-XjN5nt-yqlWtWpTno5j7lw; JSESSIONID=03A802526A2770F62897BF2D47A67FC4.c73; routekjgg=bce7765295b50ac71f342dfa7d99c0dd; NAGENTID=64378; CNZZDATA3538029=cnzz_eid%3D757073876-1522131790-https%253A%252F%252Fwww.baidu.com%252F%26ntime%3D1522137190; Hm_lvt_49024937a7f937de669432245102dac6=1522135243,1522135441,1522137198,1522138172; Hm_lpvt_49024937a7f937de669432245102dac6=1522138172',
            'content-type':'application/x-www-form-urlencoded',
            'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
        }
        ALLLIST =[]
        aalist  =fomrtTime()
        print('看那一天的数据日期',aalist)
        for  itme  in aalist:
                params ={
                    'gameIndex': '301',
                    'searchDate':  '2018-04-20',
                    'gameFrom': ''
                }
                web_data = requests.post(urls,data=params,headers=headers)
                if web_data.status_code == 200:
                    JSON_data_History= json.loads(web_data.text)
                    soup =re.findall("<td style='color:red'>(.*?)</td>",JSON_data_History['resultHtml'],re.S) 
                    for itme  in  soup:
                        _itme=itme.split('|')
                        ALLLIST.append(_itme)
                else:
                    print('itme错误itme:',itme)        
                    # fomrt_LIST(ALLLIST) 
        # print(ALLLIST)   
        print(ALLLIST)
        fomrt_LIST(ALLLIST)        
#     ALLLIST.append(like.get_text().split('|'))
# print(linkes)
# 将时间转换成时间戳
_old_time=0
timeLIST=[]
# ======================================================================================
# 计算出多少天的日期格式
def fomrtTime():
    global _old_time
    global timeLIST
    num  =1
    now = int(time.time())
    _old_time =now
    for i in   range(num):
        _old_time+=86400
        if _old_time ==int(time.time()):
            continue 
        time_local = time.localtime(_old_time)
        dt = time.strftime("%Y-%m-%d",time_local)
        timeLIST.append(dt)
    return timeLIST   


def fomrt_LIST(aa):

    wuxing_not0 =0
    wuxing_not0_list =[]

    wuxing_not1 =0
    wuxing_not1_list =[]

    wuxing_not2 =0
    wuxing_not2_list =[]

    wuxing_not3 =0
    wuxing_not3_list =[]

    wuxing_not4 =0
    wuxing_not4_list =[]

    wuxing_not5 =0
    wuxing_not5_list =[]

    wuxing_not6 =0
    wuxing_not6_list =[]

    wuxing_not7 =0
    wuxing_not7_list =[]

    wuxing_not8 =0
    wuxing_not8_list =[]

    wuxing_not9 =0
    wuxing_not9_list =[]
    for  item in aa:
        if '0' in item:
            wuxing_not0_list.append(wuxing_not0)
            wuxing_not0=0
        else:
            wuxing_not0=wuxing_not0+1

# ==========================================================
        if '1' in item:
            wuxing_not1_list.append(wuxing_not1)
            wuxing_not1=0
        else:
            wuxing_not1=wuxing_not1+1
# ==========================================================              
        if '2' in item:
            wuxing_not2_list.append(wuxing_not2)
            wuxing_not2=0
        else:
            wuxing_not2=wuxing_not2+1 
# ==========================================================               
        if '3' in item:
            wuxing_not3_list.append(wuxing_not3)
            wuxing_not3=0
        else:
            wuxing_not3=wuxing_not3+1     
# ==========================================================            
        if '4' in item:
            wuxing_not4_list.append(wuxing_not4)
            wuxing_not4=0
        else:
            wuxing_not4=wuxing_not4+1 
        if '5' in item:
            wuxing_not5_list.append(wuxing_not5)
            wuxing_not5=0
        else:
            wuxing_not5=wuxing_not5+1 
        if '6' in item:
            wuxing_not6_list.append(wuxing_not6)
            wuxing_not6=0
        else:
            wuxing_not6=wuxing_not6+1 
        if '7' in item:
            wuxing_not7_list.append(wuxing_not7)
            wuxing_not7=0
        else:
            wuxing_not7=wuxing_not7+1 
        if '8' in item:
            wuxing_not8_list.append(wuxing_not8)
            wuxing_not8=0
        else:
            wuxing_not8=wuxing_not8+1 
        if '9' in item:
            wuxing_not9_list.append(wuxing_not9)
            wuxing_not9=0
        else:
            wuxing_not9=wuxing_not9+1                              
   
    print('wuxing_not0_list',(wuxing_not0_list))   
    print('wuxing_not1_list',(wuxing_not1_list))  
    print('wuxing_not2_list',(wuxing_not2_list))  
    print('wuxing_not3_list',(wuxing_not3_list))  
    print('wuxing_not4_list',( wuxing_not4_list) )  
    print('wuxing_not5_list',( wuxing_not5_list) )  
    print('wuxing_not6_list',(wuxing_not6_list))   
    print('wuxing_not7_list',(wuxing_not7_list))   
    print('wuxing_not8_list',(wuxing_not8_list))    
    print('wuxing_not9_list',(wuxing_not9_list))      

          





# 以上调用时间的数据

if  __name__ =='__main__':
    # fomrt_LIST(1)
    # f = open('historyData.txt','w')
    # fomrtTime()
    get_info()
    # f.write(str(ALLLIST))
    # f.close()
