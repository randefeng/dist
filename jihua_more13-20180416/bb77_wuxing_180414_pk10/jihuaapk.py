#-*_coding:utf8-*-
import   requests
import   time
import   math
import   re
from lxml import  etree
#设置表头
headers={
    'Cookie': 'Hm_lvt_311efc33b120b3d6b860ed6ad22ada92=1521615736,1523349303; PHPSESSID=ijc7onvht4jh6k4ovuqurnks4v',
    'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
}
def  get_info():
    url  ='https://www.aapk10.com/Pro/Ajax.php?FunctionNum=2&ObjName=Right1'
    res =requests.get(url, headers=headers,timeout=5)
    res.encoding = 'utf-8'
    if res.status_code ==200:
        req  =res.text
        infos = re.findall(r'\$\("\#NumWill"\)\.html\(\'(.*?)\'\)', req)
        item = re.findall('【(.*?)】',str(infos[0]),re.S) 
        will_buyhao = list(item[0])
        return {'buyParms':BUYHAOMA(will_buyhao,''),'will_buyhao':will_buyhao}
    else:
        pass
        print('接口挂了')
        return []    
# ================================================================================
# 下注的参数
def  BUYHAOMA(buyNumber,money):
    # buyNumber =['0', '3', '4', '5', '7']
    # money=1
    print('buyNumber=================',buyNumber)
    orders=[]
    for  i  in  buyNumber :
        obj = {'odds':'9.99','play':'B5','code':'cqssc'}
        obj['money']=money # 钱
        obj['num']='第五球 '+str(i) # 第几个那个号
        obj['content']=i # 那个号
        obj['title']='第五球 '+str(i) # 第几个那个号
        orders.append(obj) # 拼接数组
    return  orders 
if  __name__ =='__main__':
   print(get_info())