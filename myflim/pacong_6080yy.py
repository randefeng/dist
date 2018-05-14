import  requests 

headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Mobile Safari/537.36'
}

res =  requests.get('https://yyy6080.cc/')
res.encoding = "utf-8"

result =res.text
f = open('historyMoney.html','a',encoding='UTF-8')
f.write(str(result))
f.close()
