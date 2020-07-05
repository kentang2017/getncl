from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
import urllib.request
import urllib
import time
import os

html = "http://192.83.186.192/NCLSearch/Search/SearchDetail?item=ec4419f3b5514e4bb6a82480c9de8bb7fDcyNzk50&image=1&page=1&whereString=&sourceWhereString=&SourceID="
chrome_options = Options()
chrome_options.add_argument("--headless")
broswer = webdriver.Chrome(chrome_options=chrome_options)
broswer.get(html)


def genjpg(page, bookname):
    f_image_path = broswer.find_element_by_xpath('//*[@id="ImageDisplay"]')
    f_src = f_image_path.get_attribute('src')
    if not os.path.exists(bookname):
        os.mkdir(bookname)
    f_file = urllib.request.urlretrieve(f_src, bookname+"/"+str(0).zfill(3)+".jpg")
    pageurl = []
    for i in range(1, page):
        button = broswer.find_element_by_xpath('//*[@id="AftT"]')
        ActionChains(broswer).click(button).perform()
        time.sleep(3)
        image_path = broswer.find_element_by_xpath('//*[@id="ImageDisplay"]')
        src = image_path.get_attribute('src')
        file = urllib.request.urlretrieve(src, bookname+"/"+str(i).zfill(3)+".jpg")
        print(str(i).zfill(3))
        pageurl.append(src)
    return pageurl
	
if __name__ == '__main__':
    genjpg(244, "大六壬秘本")