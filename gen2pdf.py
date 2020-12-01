from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
import urllib.request
import urllib
import time
import os
from tkinter import *

html = "http://192.83.186.192/NCLSearch/Search/SearchDetail?item=e98b57623d7d4671815798d2bdfbcde5fDcyNzkx0&image=1&page=6&whereString=&sourceWhereString=&SourceID="

def click():
	entered_text=textentry.get()
	output.delete(0.0, END)
	try:
		run = genjpg(entered_text)
	except:
		run = "沒有結果"
	output.insert(END, run)


window = Tk()
window.geometry("500x200")
window.title("國家圖書館古籍與特藏文獻資源-下載易")

Label (window) .grid(row=0, column=0, sticky=W)
Label (window, text="請輸入古籍網址") .grid(row=1, column=0, sticky=W)


textentry = Entry(window, width=180, bg="white")
textentry.grid(row=2, column=0, sticky=W)
Button(window, text="提交", width=2, command=click).grid(row=3, column=0, sticky=W)

Label (window, text="結果") .grid(row=4, column=0, sticky=W)
output = Text(window, width=160, height=7, wrap=WORD, background="black")
output.grid(row=5, column=0, sticky=W)



def genjpg(url):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    broswer = webdriver.Chrome(chrome_options=chrome_options)
    broswer.get(url)
    title = broswer.find_element_by_xpath('//*[@id="F1"]/table/tbody/tr[4]/td').text
    if "鈔本" in title == True:
        title = broswer.find_element_by_xpath('//*[@id="F1"]/table/tbody/tr[2]/td').text
        if "鈔本" in title == True:
            title = broswer.find_element_by_xpath('//*[@id="F1"]/table/tbody/tr[4]/td').text
    
    
    pagenum = broswer.find_element_by_xpath('//*[@id="sel-content-no"]').text.replace("/ ","").split("\n")
    f_image_path = broswer.find_element_by_xpath('//*[@id="ImageDisplay"]')
    f_src = f_image_path.get_attribute('src')
    if not os.path.exists(title):
        os.mkdir(title)
    f_file = urllib.request.urlretrieve(f_src, title+"/"+str(0).zfill(5)+".jpg")
    pageurl = []
    for i in pagenum:
        button = broswer.find_element_by_xpath('//*[@id="AftT"]')
        ActionChains(broswer).click(button).perform()
        time.sleep(3)
        image_path = broswer.find_element_by_xpath('//*[@id="ImageDisplay"]')
        src = image_path.get_attribute('src')
        file = urllib.request.urlretrieve(src, title+"/"+str(i).zfill(5)+".jpg")
        print(str(i).zfill(3))
        pageurl.append(src)
    return pageurl
	

if __name__ == '__main__':
	window.mainloop()
    
