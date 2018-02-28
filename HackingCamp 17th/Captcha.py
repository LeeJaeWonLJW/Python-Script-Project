from bs4 import BeautifulSoup
import requests
import base64
from PIL import Image
from pytesseract import *
from selenium import webdriver

url='http://debu.kr:53201/8671d960384a6dc7410701db14af4db2/'

def OCR(imgfile, lang='eng'):
    img=Image.open(imgfile)
    text=image_to_string(img)
    text=text.replace(" ","")
    text=text.replace('\n',"")

    return text

driver = webdriver.Chrome('/usr/local/lib/python3.6/site-packages/chromedriver')
driver.implicitly_wait(3)
driver.get('http://debu.kr:53201/8671d960384a6dc7410701db14af4db2/')


for i in range(1,11,1):
    data=str(driver.page_source)

    tt=data.split('" /></p>')
    kk=tt[0].split(";base64,")

    contents=kk[1]

    print(kk[0])


    txt = base64.b64decode(contents)
    f = open("a"+str(i)+".png",'wb')
    f.write(txt)
    f.close()

    

    result=OCR("a"+str(i)+".png")

    driver.find_element_by_name('answer').send_keys(result)

    driver.find_element_by_xpath("//input[@type='submit']").click()
