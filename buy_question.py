import json
from selenium import webdriver

def buyQuestions(driver, url):
    id = url[48-len(url):]
    driver.get(url)
    driver.execute_script("buyQuestion({})".format(id))

if __name__ == "__main__":
    data = json.load(open('./data_ask.json'))
    data = data['data'][0]
    driver = webdriver.Chrome('./chromedriver')
    driver.get('https://ask.bigschool.vn')
    # driver.add_cookie(data['cookies'])
    element = driver.find_element_by_xpath("//a[contains(text(),'Đăng nhập')]")
    element.click()
    element = driver.find_element_by_xpath("//input[@id='user_name_this']")
    element.send_keys("hantv2")
    element = driver.find_element_by_xpath("//input[@id='password_this']")
    element.send_keys("tinhdunghatuan168")
    element = driver.find_element_by_xpath("//button[contains(text(),'Đăng nhập')]")
    element.click()
    for url in data['urls']:
        buyQuestions(driver, url)

