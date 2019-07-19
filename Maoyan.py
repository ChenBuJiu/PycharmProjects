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
    items = parse.xpath('//*[@id="app"]//dd')
    for item in items:
        yield {
            'index': item.xpath('./i/text()')[0],
            'title': item.xpath('./a/@title')[0],
            'star': item.xpath('.//p[@class="star"]/text()')[0].strip(),
            'score': item.xpath('.//p[@class = "score"]/i[1]/text()')[0] +
                     item.xpath('.//p[@class = "score"]/i[2]/text()')[0]
        }
    return items


def format(item):
    pass


if __name__ == '__main__':
    offset = 0
    for i in range(10):
        offset = i * 10
        url = 'http://maoyan.com/board/4?offset=' + str(offset)
        html = get_html(url)
        items = parse_one_page(html)
        for item in items:
            print(item)
