from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
import time
import requests
import cv2
import numpy as np
web=Chrome()
web.get('http://dun.163.com/trial/sense')

web.find_element_by_xpath('/html/body/main/div[1]/div/div[2]/div[2]/ul/li[2]').click()
time.sleep(1)
web.find_element_by_xpath('/html/body/main/div[1]/div/div[2]/div[2]/div[1]/div[2]/div[1]/div/div[2]/div[3]/div/div/div[1]/div[1]/div/span[1]').click()
time.sleep(1)

url1=web.find_element_by_xpath("//img[@class='yidun_bg-img']").get_attribute('src')
url2=web.find_element_by_xpath("//img[@class='yidun_jigsaw']").get_attribute('src')

open('bg.jpg','wb').write(requests.get(url1).content)
open('front.jpg','wb').write(requests.get(url2).content)

bg=cv2.imread('bg.jpg')
front=cv2.imread('front.jpg')


# 灰度处理
bg=cv2.cvtColor(bg,cv2.COLOR_BGR2GRAY)
front=cv2.cvtColor(front,cv2.COLOR_BGR2GRAY)

# 接下来把滑块做处理
front=front[front.any(1)]   # 不懂！！！！！

# 匹配--》cv图像匹配算法
result=cv2.matchTemplate(bg,front,cv2.TM_CCOEFF_NORMED)  # 精度最高、速度最慢
# 求出匹配最大值所在的位置 为了拿到移动距离
x,y=np.unravel_index(np.argmax(result),result.shape)

div=web.find_element_by_xpath("/html/body/main/div[1]/div/div[2]/div[2]/div[1]/div[2]/div[1]/div/div[2]/div[3]/div/div/div[2]/div/div/div[2]/div[2]")
# 需要引入动作链
ActionChains(web).drag_and_drop_by_offset(div,xoffset=y,yoffset=0).perform()

# 滑块的宽和高
# w,h=front.shape
# x和y规定是反的
# (38,38,38)是颜色 2是线的粗度
# cv2.rectangle(bg,(y,x),(y+w,x+h),(38,38,38),2)
# cv2.imshow("gray",bg)
# cv2.waitKey(0)
# cv2.destroyAllWindows()