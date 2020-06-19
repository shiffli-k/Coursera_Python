# Assignment Week 6 a
import json
import urllib.request
cummulative_sum = int()
# json_handler = urllib.request.urlopen("http://py4e-data.dr-chuck.net/comments_42.json")
json_handler = urllib.request.urlopen("http://py4e-data.dr-chuck.net/comments_666388.json")
our_dict = json.load(json_handler)

for each_item in our_dict["comments"]:
    cummulative_sum += each_item["count"]

print(cummulative_sum)
