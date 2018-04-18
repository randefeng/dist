#-*_coding:utf8-*-
import   requests
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
    if res.status_code =='200':
        
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
    if res.status_code =='200':
        
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
    if res.status_code =='200':
        
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
    if res.status_code =='200':
        
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
    if res.status_code =='200':
        
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
               
if  __name__ =='__main__':
    ge()