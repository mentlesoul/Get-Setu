import requests
import os

url = "https://iw233.cn/API/Random.php"
n = 0
p = 0
for i in range(500):
    response = requests.get(url)
    name = response.url.split("/")[-1]
    path = "jpg\\" + name
    if not os.path.exists(path):
        with open(path, 'wb') as f:
            f.write(response.content)
        n += 1
    else:
        p += 1
print("成功保存%c张图片，失败%c张" % (n, p))