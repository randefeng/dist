#-*_coding:utf8-*-
import   requests
import   time
import   math
import   re
from lxml import  etree
#设置表头
headers={
    'Cookie': 'PHPSESSID=trhi06ieiji1r11a73gslrg1l3; page=bjpk10; more=undefined; goeasyNode=2',
    'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
}
def  ge():
    url  ='http://ttcgo.com/plan_go/jh1.asp'
    data={
        'my1': 2,
        'my2': 5,
        'my3': 3,
    }
    
    res =requests.post(url, data = data,headers=headers,timeout=5)
    res.encoding = 'utf-8'
    if res.status_code ==200:
        
        selector =etree.HTML(res.text)
        infos = selector.xpath('//div[@class="plan_list3"]')
        ge=[]
        for  index,info  in  enumerate(infos) :
            if index==2:
                break
            href= info.xpath('div[6]/a/@href')
            id= info.xpath('div[4]/text()')
            bu_num= info.xpath('div[2]/textarea/text()')
            id.append(href[0])
            id.append(bu_num[0])
            ge.append(id)
        aa =ge
        print('ge=========',ge)
        if int(aa[0][0].replace("%",''))==100 and int(aa[1][0].replace("%",''))==100:
            bb =aa[0][-1].replace('【','')
            bb = bb.replace('】','')
            cc=aa[1][-1].replace('【','')
            cc= cc.replace('】','')
            L = set(cc) & set(bb)
            return L
        else:
            return []
    else:
        print('接口挂了')
        return []
        

def  shi():
    url  ='http://ttcgo.com/plan_go/jh1.asp'
    data={
        'my1': 2,
        'my2': 4,
        'my3': 3,
    }
    
    res =requests.post(url, data = data,headers=headers,timeout=5)
    res.encoding = 'utf-8'
    if res.status_code ==200:
        
        selector =etree.HTML(res.text)
        infos = selector.xpath('//div[@class="plan_list3"]')
        ge=[]
        for  index,info  in  enumerate(infos) :
            if index==2:
                break
            href= info.xpath('div[6]/a/@href')
            id= info.xpath('div[4]/text()')
            bu_num= info.xpath('div[2]/textarea/text()')
            id.append(href[0])
            id.append(bu_num[0])
            ge.append(id)
        aa =ge
        print('ge=========',ge)
        if int(aa[0][0].replace("%",''))==100 and int(aa[1][0].replace("%",''))==100:
            bb =aa[0][-1].replace('【','')
            bb = bb.replace('】','')
            cc=aa[1][-1].replace('【','')
            cc= cc.replace('】','')
            L = set(cc) & set(bb)
            return L
        else:
            return []
    else:
        print('接口挂了')
        return []
        
 
    
def  bai():
    url  ='http://ttcgo.com/plan_go/jh1.asp'
    data={
        'my1': 2,
        'my2': 3,
        'my3': 3,
    }
    
    res =requests.post(url, data = data,headers=headers,timeout=5)
    res.encoding = 'utf-8'
    if res.status_code ==200:
        
        selector =etree.HTML(res.text)
        infos = selector.xpath('//div[@class="plan_list3"]')
        ge=[]
        for  index,info  in  enumerate(infos) :
            if index==2:
                break
            href= info.xpath('div[6]/a/@href')
            id= info.xpath('div[4]/text()')
            bu_num= info.xpath('div[2]/textarea/text()')
            id.append(href[0])
            id.append(bu_num[0])
            ge.append(id)
        aa =ge
        print('ge=========',ge)
        if int(aa[0][0].replace("%",''))==100 and int(aa[1][0].replace("%",''))==100:
            bb =aa[0][-1].replace('【','')
            bb = bb.replace('】','')
            cc=aa[1][-1].replace('【','')
            cc= cc.replace('】','')
            L = set(cc) & set(bb)
            return L
        else:
            return []
    else:
        print('接口挂了')
        return []
        

def  qian():
    url  ='http://ttcgo.com/plan_go/jh1.asp'
    data={
        'my1': 2,
        'my2': 2,
        'my3': 3,
    }
    
    res =requests.post(url, data = data,headers=headers,timeout=5)
    res.encoding = 'utf-8'
    if res.status_code ==200:
        
        selector =etree.HTML(res.text)
        infos = selector.xpath('//div[@class="plan_list3"]')
        ge=[]
        for  index,info  in  enumerate(infos) :
            if index==2:
                break
            href= info.xpath('div[6]/a/@href')
            id= info.xpath('div[4]/text()')
            bu_num= info.xpath('div[2]/textarea/text()')
            id.append(href[0])
            id.append(bu_num[0])
            ge.append(id)
        aa =ge
        print('ge=========',ge)
        if int(aa[0][0].replace("%",''))==100 and int(aa[1][0].replace("%",''))==100:
            bb =aa[0][-1].replace('【','')
            bb = bb.replace('】','')
            cc=aa[1][-1].replace('【','')
            cc= cc.replace('】','')
            L = set(cc) & set(bb)
            return L
        else:
            return []
    else:
        print('接口挂了')
        return []
        

def  wan():
    url  ='http://ttcgo.com/plan_go/jh1.asp'
    data={
        'my1': 2,
        'my2': 1,
        'my3': 3,
    }
    
    res =requests.post(url, data = data,headers=headers,timeout=5)
    res.encoding = 'utf-8'
    if res.status_code ==200:
        
        selector =etree.HTML(res.text)
        infos = selector.xpath('//div[@class="plan_list3"]')
        ge=[]
        for  index,info  in  enumerate(infos) :
            if index==2:
                break
            href= info.xpath('div[6]/a/@href')
            id= info.xpath('div[4]/text()')
            bu_num= info.xpath('div[2]/textarea/text()')
            id.append(href[0])
            id.append(bu_num[0])
            ge.append(id)
        aa =ge
        print('ge=========',ge)
        if int(aa[0][0].replace("%",''))==100 and int(aa[1][0].replace("%",''))==100:
            bb =aa[0][-1].replace('【','')
            bb = bb.replace('】','')
            cc=aa[1][-1].replace('【','')
            cc= cc.replace('】','')
            L = set(cc) & set(bb)
            return L
        else:
            return []
    else:
        print('接口挂了')
        return []

def  wuxing():
    url  ='http://ttcgo.com/plan_go/jh1.asp'
    data={
        'my1': 2,
        'my2': 6,
        'my3': 3,
    }
    res =requests.post(url, data = data,headers=headers,timeout=5)
    res.encoding = 'utf-8'
    
    if res.status_code ==200:
        selector =etree.HTML(res.text)
        infos = selector.xpath('//div[@class="plan_list3"]')
        # n  =  infos.xpath('div[1]/test()')
        ge=[]
        for  index,info  in  enumerate(infos) :
            if index==2:
                break
            href= info.xpath('div[6]/a/@href')
            id= info.xpath('div[4]/text()')
            bu_num= info.xpath('div[2]/textarea/text()')
            name =info.xpath('div[1]/text()')
            id.append(href[0])
            id.append(bu_num[0])
            ge.append(id)
        aa =ge
        if int(aa[0][0].replace("%",''))>80:
            bb =aa[0][-1].replace('【','')
            bb = bb.replace('】','')
            if int(current_qi()) ==int(getNowqi()):
                return BUYHAOMA([bb],'')
            else:
                print('计划期数与现在不一致')
                return BUYHAOMA(['00'],'')  
        else:
            print("计划不稳定")  
            return []
    else:
        print('接口挂了')
        return []
	
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
		
	return qi    

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
		
	return qi    
# 这个服务老挂。取一下他页面的开奖，不一致的话不玩了
def  getNowqi():
    url  ='http://ttcgo.com/go/code.asp'
    data={
        'my1': 2,
        'my2': 20
    }
    res =requests.post(url, data = data,headers=headers,timeout=5)
    res.encoding = 'utf-8'
    if res.status_code ==200:
        linkes =re.findall('<td width="32%" height="40" align="center" valign="middle" class="mdiv1_info_a1">(.*?)</td>',res.text,re.S) 
        # # print(current_qi())
        # selector =etree.HTML(res.text)
        # infos = selector.xpath('tr')
        return linkes[0][0:3] 
    else:
        print('接口挂了')
        return []    
def  BUYHAOMA(buyNumber,money):
    print('buyNumber=================',buyNumber)
    # print('money=================',money)

    if buyNumber[0]=='00':
        return   {
            'buyParms': '',
            'will_buyhao':''
        }
    else:    
        orders=[]
        for  i  in  range(5) :
            obj = {'odds':'9.99','play':'B1','code':'cqssc'}
            obj['money']='' # 钱
            obj['play']='B'+str(i+1) # 钱
            obj['num']='第'+fomfun(i)+'球 '+(buyNumber[0]) # 第几个那个号
            obj['content']=buyNumber[0] # 那个号
            obj['title']='整合'# 第几个那个号
            obj['check']='true'# 第几个那个号
            orders.append(obj) # 拼接数组
        return   {
            'buyParms': orders,
            'will_buyhao':buyNumber
        }
def fomfun(num):
    if num==0:
        return '一'
    elif num ==1:
        return '二'    
    elif num ==2:
        return '三'  
    elif num ==3:
        return '四'  
    elif num ==4:
        return '五'  
    else:
        return '0'    

if  __name__ =='__main__':
    while True:
        try:
            print(9)
            wuxing()
            print(wuxing())
            time.sleep(59)
        except Exception as e:
            print(e)       
   