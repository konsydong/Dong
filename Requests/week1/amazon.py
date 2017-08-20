import requests

url = "https://www.amazon.cn/%E5%9B%BE%E4%B9%A6/dp/B01M8L5Z3Y/ref=sr_1_1?" \
      "ie=UTF8&qid=1503129949&sr=8-1&keywords=%E6%9E%81%E7%AE%80"
try:
    kv = {'user-agent': 'Mozilla/5.0'}
    r = requests.get(url, headers=kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text)
except requests.HTTPError:
    print("爬取失败")

# r = requests.get(url)
# print(r.request.headers)
# print("status_code:", r.status_code)
# print("encoding(before):", r.encoding)
# r.encoding = r.apparent_encoding
# print("encoding(now):", r.encoding)
# print(r.text)
