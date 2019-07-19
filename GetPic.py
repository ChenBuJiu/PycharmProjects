import os

import requests
from requests import RequestException


def get_html():
    url = 'http://t.dyxz.la/upload/img/201412/593.jpg'
    headers={
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}
    try:
        response = requests.get(url, headers = headers)
        if(response.status_code == 200):
            file_path = '01.jpg'
            if not os.path.exists(file_path):
                # 开始下载图片
                with open(file_path, 'wb') as f:
                    f.write(response.content)
                    print('该图片已下载完成')
            else:
                print('该图片已下载')
            return response.text
    except RequestException:
        print('请求失败')
        return None
if __name__ == '__main__':
    html = get_html();
   # print(get_html())


