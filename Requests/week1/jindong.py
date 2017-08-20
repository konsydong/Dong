import requests

url = "https://item.jd.com/2967929.html"
try:
    r = requests.get(url)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[:1000])
except requests.HTTPError:
    print("爬取失败")

# r = requests.get("https://item.jd.com/2967929.html")
# print("status_code:", str(r.status_code))
# print("encoding:", str(r.encoding))
# print("text:", r.text[:1000])
