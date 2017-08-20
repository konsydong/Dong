import requests
# baidu
keyword = "Python"
try:
    kv = {'wd': keyword}
    r = requests.get("http://www.baidu.com/s", params=kv)
    r.raise_for_status()
    print(r.request.url)
    print(len(r.text))
except requests.HTTPError:
    print("爬取失败")

# 360
# keyword = "Python"
# try:
#     kv = {'wd': keyword}
#     r = requests.get("http://www.so.com/s", params=kv)
#     r.raise_for_status()
#     print(r.request.url)
#     print(len(r.text))
# except requests.HTTPError:
#     print("爬取失败")
