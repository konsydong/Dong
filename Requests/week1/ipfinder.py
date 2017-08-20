import requests
url = "http://www.ip138.com/ips1388.asp?ip="
try:
    r = requests.get(url + "113.140.29.13")
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[-2500:-2000])
except requests.HTTPError:
    print("爬取失败")
