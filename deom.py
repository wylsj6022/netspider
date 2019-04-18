import re,requests,random

url=r"http://v.baidu.com/"

'''
#ip代理
proxylist=[
	{"http":"111.19.51.208:80"},
	{"http":"111.19.51.208:80"},
	{"http":"111.19.51.208:80"},
	{"http":"111.19.51.208:80"},
	{"http":"111.19.51.208:80"},
	
]	

proxy=random.choice(proxylist)

#构建代理处理器对象
proxyHandler=request.ProxyHandler(proxy)

#创建自定义opener
opener=request.build_opener(proxyHandler)

#创建请求对象
#req=request.Request("http://www.baidu.com")
#创建请求对象
req=request.Request("http://www.baidu.com")

res=opener.open(req)


#print(proxy)
print(res.read().decode())
'''
#谷哥浏览器user-agent1
agent1="Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"

#火狐浏览器user-agent2
agent2="Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0"

#360浏览器user-agent3
agent3="Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE"

#UC浏览器user-agent4
agent4="Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.2.3831.211 Safari/537.36"
#构造请求头信息
list1=[agent1,agent2,agent3,agent4]

agent=random.choice(list1)

headers={"User-Agent": agent}

response=requests.get(url,headers=headers)


print(response.text)
