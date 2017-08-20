# 优化输出 对齐
import requests
from bs4 import BeautifulSoup
import bs4


def get_html_text(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except requests.HTTPError:
        return ""


def fill_univ_list(u_list, html):
    soup = BeautifulSoup(html, "html.parser")
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            u_list.append([tds[0].string, tds[1].string, tds[3].string])
    pass


def print_univ_list(u_list, num):
    tp_lt = "{0:^10}\t{1:{3}^10}\t{2:^10}"
    print("{:^10}\t{:^9}\t{:^16}".format("排名", "学校名称", "总分"))
    for i in range(num):
        u = u_list[i]
        print(tp_lt.format(u[0], u[1], u[2], chr(12288)))


def main():
    u_info = []
    url = "http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html"
    html = get_html_text(url)
    fill_univ_list(u_info, html)
    print_univ_list(u_info, 20)
main()
