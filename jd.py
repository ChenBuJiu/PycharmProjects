import time
from selenium import webdriver


def login():
    acount_num = input('请输入账号:\n')
    passwd_str = input('请输入密码:\n')
    driver = webdriver.Chrome()
    url = 'https://passport.jd.com/new/login.aspx'
    driver.get(url)
    time.sleep(30)

    account = driver.find_element_by_id('loginname')
    password = driver.find_element_by_id('nloginpwd')
    submit = driver.find_element_by_id('loginsubmit')

    account.clear()
    password.clear()
    account.send_keys('yourname')
    password.send_keys('yourpassword')

    submit.click()
    time.sleep(5)


if __name__ == '__main__':
    login()