# import pytesseract
# from PIL import Image
#
# img=Image.open('recaptcha.png')
#
# gray=img.convert('L')
# gray.show()
# bw = gray.point(lambda x: 0 if x < 1 else 255,'1')
# bw.show()
# print(pytesseract.image_to_string(bw))

from selenium import webdriver
import pytesseract
from PIL import Image
import time

browser = webdriver.Chrome()
url = 'http://my.cnki.net/elibregister/commonRegister.aspx'
browser.get(url)
html = browser.page_source
print(html)
browser.save_screenshot('zhiwang.png')
img = browser.find_element_by_id('checkcode')
left = img.location['x']  # 验证码图片左上角横坐标
top = img.location['y']  # 验证码图片左上角纵坐标
right = left + img.size['width']  # 验证码图片右下角横坐标
bottom = top + img.size['height']  # 验证码图片右下角纵坐标
im = Image.open('zhiwang.png')
im_crop = im.crop((left, top, right, bottom))  # 这个 im_crop 就是从整个页面截图中再截出来的验证码的图片
im_crop.save('zrecaptchar.png')
img = Image.open('zrecaptchar.png')
img.show()
# 可以看出，验证码文本一般都是黑色的，背景则会更加明亮，
# 所以我们可以通过检查像素是否为黑色将文本分离出来，该处理过程又被称为阈值化。通过Pillow可以容易地实现该处理过程。
gray = img.convert('L')  # 灰度化，图片转化成灰度图
gray.show()
# 二值化,指定而二值化的阈值，默认阈值 127
threshold = 155
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)
bw = gray.point(table, '1')
bw.show()
strcode = pytesseract.image_to_string(bw)
print(strcode)
user = browser.find_element_by_id('username')
pwd = browser.find_element_by_id('txtPassword')
email = browser.find_element_by_id('txtEmail')
checkCode = browser.find_element_by_id('txtOldCheckCode')
btnReg = browser.find_element_by_id('ButtonRegister')
user.send_keys('guojiantao@163.com')
time.sleep(2)
pwd.send_keys('mimamima')
time.sleep(2)
email.send_keys('guojiantao@163.com')
time.sleep(2)
checkCode.send_keys(strcode)
# 模拟点击按钮
btnReg.click()
