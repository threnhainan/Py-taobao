# Py-taobao

python 实现自动抢单，目前只能实现秒(或毫秒)级抢单  
抢单时间同步淘宝服务器时间(非本地时间)  
不会自动付款，抢到后一定要在规定时间内到待付款进行付款
---
设置时间格式: 2020-12-18 15:19:59.900000(必须精确到6位)  
推荐设置100毫秒延迟  
持续抢单预计450毫秒左右(主要看网速快不快)
---
⚠️：请使用 Terminal/CMD 运行代码(否则密码将会已明文形式显示在控制台)

---
配置环境教程(Google Chrome)：  
0、下载 Python3.7.8(也可以其它版本，最好不低于Python3.7)
> https://www.python.org/downloads/release/python-378/

1、使用 pip 下载 selenium 包
> pip install selenium

2、使用 pip 下载 requests 包
> pip install requests

3、下载 ChromeDriver 插件
> http://npm.taobao.org/mirrors/chromedriver/

4、把 ChromeDriver 添加到环境变量(Windows)
> 略

4、把 ChromeDriver 添加到环境变量(MacOS/Linux)
> sudo mv chromedriver /usr/local/bin
