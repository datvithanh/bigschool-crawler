import json
from selenium import webdriver


def buyQuestions(driver, url):
    id = url[48-len(url):]
    driver.get(url)
    driver.execute_script("buyQuestion({})".format(id))


if __name__ == "__main__":
    all = json.load(open('./data_ask.json'))
    config = json.load(open('config.json'))['bigschool']
    data = all['data'][1]
    driver = webdriver.Chrome('./chromedriver')
    driver.get('https://ask.bigschool.vn')
    # driver.add_cookie(data['cookies'])
    element = driver.find_element_by_xpath("//a[contains(text(),'Đăng nhập')]")
    element.click()
    element = driver.find_element_by_xpath("//input[@id='user_name_this']")
    element.send_keys(config['user'])
    element = driver.find_element_by_xpath("//input[@id='password_this']")
    element.send_keys(config['password'])
    element = driver.find_element_by_xpath(
        "//button[contains(text(),'Đăng nhập')]")
    element.click()
    if 'bought' in data.keys():
        data['bought'] = data['bought']
    else:
        data['bought'] = []
    f = open('temp.txt', 'a')
    for url in data['urls']:
        if url not in data['bought']:
            buyQuestions(driver, url)
            data['bought'].append(url)
            f.write('"{}",\n'.format(url))
