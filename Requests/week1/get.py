import requests
r = requests.get("https://www.baidu.com")
print("%s%d" % ("r.status_code: ", r.status_code))
print("type(r):" + str(type(r)))
print("r.headers:" + str(r.headers))
r.encoding = 'utf-8'
print(r.text)

