import requests
import os


url = "http://rs.xidian.edu.cn/data/attachment/forum/201708/18/203320qrrqar0lzllm7tlo.png"
root = ".\\download\\picture\\"
path = root + url.split('/')[-1]
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        with open(path, 'wb') as f:
            f.write(r.content)
            f.close()
            print("文件保存成功")
    else:
        print("文件已存在")
except requests.HTTPError:
    print("爬取失败")
