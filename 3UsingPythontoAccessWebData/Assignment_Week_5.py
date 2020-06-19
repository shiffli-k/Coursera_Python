# Assignment Week 5
import urllib.request
import xml.etree.ElementTree as elTree
string_value = str()
cumulative_value = int()
# xml_handler = urllib.request.urlopen("http://py4e-data.dr-chuck.net/comments_42.xml")
xml_handler = urllib.request.urlopen("http://py4e-data.dr-chuck.net/comments_666387.xml")


for each_line in xml_handler:
    string_value += str(each_line.decode())

formatted_string = elTree.fromstring(string_value)
found_items = formatted_string.findall('comments/comment')

for each_item in found_items:
    current_num = int(each_item.find("count").text)
    cumulative_value += current_num

print("\nThe sum of {} items found were {}".format(len(found_items), cumulative_value))
