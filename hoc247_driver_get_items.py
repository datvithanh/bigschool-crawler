import json
from selenium import webdriver

if __name__ == "__main__":
    config = json.load(open('config.json'))['hoc247']
    driver = webdriver.Chrome('./chromedriver')
    driver.get('https://hoc247.net/tai-khoan/dang-nhap.html')
    #fill username
    element = driver.find_element_by_id('txtLoginUsername')
    element.send_keys(config['user'])
    #fill password
    element = driver.find_element_by_id('txtLoginPassword')
    element.send_keys(config['password'])
    #click login
    element = driver.find_element_by_xpath("//button[@type='submit']")
    element.click()
    #go to crawled website
    driver.get('https://hoc247.net/bai-tap-chuyen-de-dao-ham-va-ung-dung')
    driver.execute_script("viewAnswer(45770,1)")
    #get answer
    element = driver.find_element_by_xpath("//div[@class='loigiai']")
    element.get_attribute('innerHTML')
