# Assignment Week 4 a
import urllib.request
from bs4 import BeautifulSoup

sum_Num = int()
user_link = input("Enter - ")

# html = urllib.request.urlopen("http://py4e-data.dr-chuck.net/comments_42.html")
# html = urllib.request.urlopen("http://py4e-data.dr-chuck.net/comments_666385.html")

html = urllib.request.urlopen(user_link)
bs = BeautifulSoup(html, 'html.parser')
span_tag = bs("span")
for each_item in span_tag:
    current_num = each_item.getText()
    if len(current_num) == 0:
        continue
    else:
        sum_Num += int(current_num)
print(sum_Num)
