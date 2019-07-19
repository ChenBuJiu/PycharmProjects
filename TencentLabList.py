import requests
from lxml import etree


def get_html(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text


def parse_one_page(html):
    parse = etree.HTML(html)
    items = parse.xpath("/html/body/div[4]/div[2]/div/div[2]/ul[1]/li")
    for item in items:
        yield {
            'title': item.xpath('.//h3/text()')[0]
        }
    return items

#/html/body/div[4]/div[2]/div/div[2]/ul/li[1]/a/div/div/div[4]/h3
#/html/body/div[4]/div[2]/div/div[2]/ul/li[3]


def format(item):
    pass


if __name__ == '__main__':
    for i in range(1,10):
        url = 'https://cloud.tencent.com/developer/labs/gallery?page=' + str(i)
        html = get_html(url)
        results = parse_one_page(html)
        for rs in results:
            print(rs)
