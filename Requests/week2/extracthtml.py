import requests
from bs4 import BeautifulSoup

url = "http://python123.io/ws/demo.html"
r = requests.get(url)
demo = r.text
soup = BeautifulSoup(demo, "html.parser")
# print(soup.prettify())
for link in soup.find_all('a'):
    print(link.get('href'))

