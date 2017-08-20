import requests
from bs4 import BeautifulSoup


url = "http://python123.io/ws/demo.html"
r = requests.get(url)
demo = r.text
soup = BeautifulSoup(demo, "html.parser")
tag = soup.a  # 返回第一个
print("type(tag):"+str(type(tag)))
print("type(tag.attr):"+str(type(tag.attrs)))



