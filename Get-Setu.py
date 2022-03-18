import requests
import os
import json
import re

#通过别人的API随机
loli = 'https://api.loliurl.club/api/setu/?tag=loli'
twod = 'https://api.loliurl.club/api/setu/?tag=two%20dimensions'
r18 = 'https://api.loliurl.club/api/setu/?tag=R-18'

root = 'E:/setu/'                #涩图保存位置
time = 500                        #循环获取每种涩图次数

for x in range(time):
    print(x+1)                   #输出保存第X轮
#保存萝莉tag涩图
    r = requests.get(loli).text
    r = json.dumps(r)
    info = r.split('Reload')[-1]
    info = re.findall("..............+.jpg\\\\", info)
    info = ''.join(info)
    info = info.strip('\\\\')
    info = info.replace("</button>\\r\\n    <a href=\\\"","")
    path = root + info.split('/')[-1]
    try:
        if not os.path.exists(root):
            os.mkdir(root)
        if not os.path.exists(path):
            r = requests.get(info)
            with open(path,'wb') as f:
                f.write(r.content)
                print("萝莉-文件保存成功")
        else:
            print("萝莉-文件已经存在")
    except:
        print("萝莉-爬取失败")
#====================================================================
#保存二次元tag涩图
    r = requests.get(twod).text
    r = json.dumps(r)
    info = r.split('Reload')[-1]
    info = re.findall("..............+.jpg\\\\", info)
    info = ''.join(info)
    info = info.strip('\\\\')
    info = info.replace("</button>\\r\\n    <a href=\\\"","")
    path = root + info.split('/')[-1]
    try:
        if not os.path.exists(root):
            os.mkdir(root)
        if not os.path.exists(path):
            r = requests.get(info)
            with open(path,'wb') as f:
                f.write(r.content)
                print("二次元-文件保存成功")
        else:
            print("二次元-文件已经存在")
    except:
        print("二次元-爬取失败")
    #====================================================================
    #保存R18 tag涩图
    r = requests.get(r18).text
    r = json.dumps(r)
    info = r.split('Reload')[-1]
    info = re.findall("..............+.jpg\\\\", info)
    info = ''.join(info)
    info = info.strip('\\\\')
    info = info.replace("</button>\\r\\n    <a href=\\\"","")
    path = root + info.split('/')[-1]
    try:
        if not os.path.exists(root):
            os.mkdir(root)
        if not os.path.exists(path):
            r = requests.get(info)
            with open(path,'wb') as f:
                f.write(r.content)
                print("R18-文件保存成功")
        else:
            print("R18-文件已经存在")
    except:
        print("R18-爬取失败")