import urllib.request
import http.cookiejar

#博客來
url = 'https://www.books.com.tw/web/books_bmidm_0802/?loc=P_003_2_002'

print('urllib下载网页方法1：最简洁方法')
print('我要練習蟒蛇 好帥')
# 直接请求 
res = urllib.request.urlopen(url) 
# 获取状态码，如果是200则获取成功 
print(res.getcode()) 
# 读取内容 #cont是很长的字符串就不输出了 
cont = res.read().decode('utf-8')
#print(cont) 

#以上成功
from bs4 import BeautifulSoup 
# 第一步：根据HTML网页字符串创建BeautifulSoup对象 

# 以 Beautiful Soup 解析 HTML 程式碼
soup = BeautifulSoup(cont, 'html.parser')

# 輸出排版後的 HTML 程式碼
#print(soup.prettify())

# 網頁標題 HTML 標籤
title_tag = soup.title
print(title_tag)



# 所有的超連結
#a_tags = soup.find_all('a')
name_box = soup.find("div", attrs={'class': 'wrap'})

name_box2 = name_box.find_all("div", attrs={'class': 'item'})
# 輸出超連結的文字
#print(name_box2) 

#成功抓到標題
i = 0    
for tag in name_box2:
    name_box3 = tag.find("h4")
    print(i)
    print(name_box3.text)
    print('\r\n') #跳行
    i = i +1
    if i == 5:
      break
    