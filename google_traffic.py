from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.proxy import *
import time
import os

list_of_proxy = ['203.190.251.114','213.85.92.10','115.124.86.50','111.161.126.100','205.186.154.32','178.32.248.125']
list_of_port = ['80','80','8080','80','3128','3128']

count_proxy = 0

#myProxy = "216.236.253.218"
#proxy = Proxy({
 #   'proxyType': ProxyType.MANUAL,
  #  'httpProxy': myProxy,
   # 'ftpProxy': myProxy,
    #'sslProxy': myProxy,
    #'noProxy':''})

#browser = webdriver.Firefox(proxy)
#browser = webdriver.Chrome(os.path.expanduser('~/chromedriver'))
with open('keywordsforautoclick.txt') as f:

    for line in f:
        profile = webdriver.FirefoxProfile()
        profile.set_preference("network.proxy.type", 1)
        profile.set_preference("network.proxy.http", list_of_proxy[count_proxy])
        profile.set_preference("network.proxy.http_port", list_of_port[count_proxy])
        profile.update_preferences()
        browser = webdriver.Firefox(firefox_profile=profile)
        q = str(line)

        qe="" 

        alert = ""
        qe = q.replace(' ', '+')
        print qe
        count_proxy = count_proxy + 1
        counter=0
        for i in range(0,20):
            body = browser.find_element_by_tag_name("body")
            body.send_keys(Keys.CONTROL + 't')
            browser.get("https://www.google.com/search?q=" + qe + "&start=" + str(counter))
            body = browser.find_element_by_tag_name("body")
            if "thetaranights" in body.text:
                print "found"
                browser.find_element_by_xpath('//a[starts-with(@href,"http://www.thetaranights.com")]').click()
        
                break
            counter+=10

