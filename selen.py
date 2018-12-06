from time import sleep
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import pil,track
import random
chrome=webdriver.Chrome()
# chrome.set_page_load_timeout(20)
chrome.maximize_window()
# 如果设置set_page_load_timeout，那么在find时候还会报错，timeout，无解
try:
    chrome.get('https://passport.lagou.com/login/login.html?utm_source=m_cf_cpt_baidu_pc')
except:
    pass
# 找到输入框输入账号密码
username=chrome.find_element_by_xpath('//div[@data-view="passwordLogin"]'
                               '//div[@data-propertyname="username"]'
                               '/input')
username.click()
username.send_keys('13113456765')
passwoed=chrome.find_element_by_xpath(
                                '//div[@data-view="passwordLogin"]'
                               '//div[@data-propertyname="password"]'
                               '/input'
)
passwoed.click()
passwoed.send_keys('lllllllll')
submit=chrome.find_element_by_xpath(
                                '//div[@data-view="passwordLogin"]'
                               '//div[@data-propertyname="submit"]'
                               '/input'
)
submit.click()
# 等滑块验证码出来
WebDriverWait(chrome,20).until(EC.presence_of_element_located(
    (By.XPATH,'//div[@class="geetest_canvas_img geetest_absolute"]')
))
# sleep(10)
num=0
while True:
    # 找到移动按钮，找不到就跳出
    try:
        pic=chrome.find_element_by_xpath(
            '//div[@class="geetest_slider_button"]'
        )
        # if num>0:
        #     ref = chrome.find_element_by_xpath(
        #         '//a[@class="geetest_refresh_1"]'
        #     )
        #     webdriver.ActionChains(chrome).click(ref).perform()
    except:
        break
    sleep(2)
    # 截屏
    chrome.save_screenshot('screenshot.png')
    sleep(2)
    # 计算距离
    offset=pil.m()
    # 模拟轨迹，还是有问题，可以看到距离没问题，轨迹一直有问题
    newtrack=track.get_track(offset)
    webdriver.ActionChains(chrome).click_and_hold(pic).perform()
    for x in newtrack:
        webdriver.ActionChains(chrome).move_by_offset(xoffset=x,yoffset=random.randint(-5,5)).perform()
    sleep(0.5)
    # webdriver.ActionChains(chrome).move_by_offset(xoffset=offset, yoffset=0).perform()
    webdriver.ActionChains(chrome).release().perform()
    sleep(3)
    num+=1
sleep(5)
print()
