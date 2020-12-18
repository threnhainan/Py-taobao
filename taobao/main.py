# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from datetime import datetime
from getpass import getpass
import requests

options = Options()
options.add_argument("headless") # 设置无头模式
# --- 无头模式下无效 --- #
# prefs = { "profile.managed_default_content_settings.images": 2 } # 设置无图模式
# options.add_experimental_option("prefs", prefs) # 加载无图模式
# --- 无头模式下无效 --- #
options.add_argument("user-agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.page_load_strategy = "none"
browser = webdriver.Chrome(options=options)
with open("/Users/admin/pythonProject/taobao/stealth.min.js") as f: # 文件要绝对路径
    puppeteer = f.read()
browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
  "source": puppeteer
})
browser.implicitly_wait(30)
browser.get("https://login.taobao.com")

def login(username, password):
    browser.find_element_by_xpath("//*[@id='fm-login-id']").send_keys(username)
    browser.find_element_by_xpath("//*[@id='fm-login-password']").send_keys(password)
username = input("会员名/邮箱/手机号: ")
password = getpass("请输入登录密码: ")
timeStart = input("设置抢单时间: ")
# login(username, password)
# --- 用户名 --- #
# browser.find_element_by_xpath("//*[@id='fm-login-id']").send_keys()
# --- 密  码 --- #
# browser.find_element_by_xpath("//*[@id='fm-login-password']").send_keys("")
# --- 登  录 --- #
browser.find_element_by_xpath("//*[@id='login-form']/div[4]/button").click()

print("登录成功！")

try:
    browser.get_screenshot_as_file("screenshots/" + browser.title + ".png")
except BaseException as msg:
    print(msg)

browser.find_element_by_xpath("//*[@id='mc-menu-hd']").click()

selectAll = browser.find_element_by_xpath("//*[@id='J_SelectAll1']")
if "selected" not in selectAll.get_attribute("class"):
    selectAll.click()

try:
    browser.get_screenshot_as_file("screenshots/" + browser.title + ".png")
except BaseException as msg:
    print(msg)

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
}

print("准备抢单中。。。")

while True:
    timestamp = requests.request("get", "http://api.m.taobao.com/rest/api3.do?api=mtop.common.getTimestamp", headers=headers)
    timestamp = eval(timestamp.text)
    data = str(timestamp["data"]["t"])
    timestamp = float(int(data) / 1000)
    dateArray = datetime.fromtimestamp(timestamp)
    dateTime = dateArray.strftime("%Y-%m-%d %H:%M:%S.%f")
    print(dateTime)
    if dateTime >= timeStart: # 设置抢单时间格式: "2020-12-14 23:59:59.900000" 推荐提前100毫秒开抢
        browser.find_element_by_xpath("//*[@id='J_SmallSubmit']").click()
        browser.find_element_by_partial_link_text("提交订单").click()
        print("抢单成功！")
        try:
            browser.get_screenshot_as_file("screenshots/" + browser.title + ".png")
        except BaseException as msg:
            print(msg)
        finally:
            break
