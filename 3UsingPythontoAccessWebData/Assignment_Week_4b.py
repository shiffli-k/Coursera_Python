# Assignment Week 4 b
import urllib.request
import re
from bs4 import BeautifulSoup


def return_email():
    listOval = list()
    html_handler = urllib.request.urlopen(current_url)
    bs = BeautifulSoup(html_handler, "html.parser")
    anchor_tag = bs("a")
    for each_tag in anchor_tag:
        listOval.append(each_tag.get("href"))
    print(listOval[position - 1])
    return listOval[position - 1]


# current_url = "http://py4e-data.dr-chuck.net/known_by_Fikret.html"
"""
# For testing
current_url = "http://py4e-data.dr-chuck.net/known_by_Zahraa.html"
search_count = 7
position = 18
"""

current_url = input("Enter Start URL :")
search_count = int(input("Enter count: "))
position = int(input("Enter position: "))

print("The Email Sequence begins with \n {0} \nwith search repetition as {1} \nPosition to look for as {2}".format(
    current_url, search_count, position))

for step in range(search_count):
    current_url = return_email()

print("The Final name is: " + str(re.findall("by_(\S+?).html", current_url)))
