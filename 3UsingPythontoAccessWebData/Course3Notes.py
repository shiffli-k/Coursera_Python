# Regular Expression --------------------- Cheat Sheet
"""
        ^           Match Beginning of line
        $           Match end of line
        .           Match any character
        \s          Match Whitespace
        \S          Match nonwhite space
        *           Repeats character zero or more times
        *?          Repeats character zero or more times (Non Greedy)
        +           Repeats character One or more times
        +?          Repeats character One or more times (Non Greedy)
        [aeiou]     Matches a single char in the listed set
        [^xyz]      Matches a single char not in listed set
        [a-z0-9]    Range of characters
        (           Start of string extraction
        )           end of string extraction
        [^ ]        A set which means look for anything but a non blank character
"""

# ----------------------------------------------------------------------------------------------------------------------


"""
import re

file_handler = open("mbox-short.txt", "r")

for line in file_handler:
    line = line.rstrip()
    if re.search("^From:", line):
        print(line)
    elif re.search("^X.*:", line):
        print(line)
"""
# ----------------------------------------------------------------------------------------------------------------------
"""
sample_String1 = "X-Sumin Value:"
sample_String2 = "X-Woah:"
if re.search("^X-\S*:", sample_String1):
    print(sample_String1)
if re.search("^X-\S*:", sample_String2):
    print(sample_String2)
"""

# ----------------------------------------------------------------------------------------------------------------------

"""
f_email = "My Email: id is Shiffli.k@gmail.com:, Contact me for info 9954678594."
# email = re.findall("^My.+ (\S+@\S+)", f_email)
email = re.search("[a-z0-9]", f_email)

print(email)
print(re.search("[0-9]+", f_email))
print(re.findall("^M.+:", f_email))
print(re.findall("\S+?@\S+", f_email))
"""

# ----------------------------------------------------------------------------------------------------------------------

"""
# Using these instead of the entire assignment week 2 code.
import re
file_handler = open("regex_sum_666383.txt", "r")
print(sum([each_line for each_line in file_handler ("[0-9)+", file_handler.read())]))
"""

# ----------------------------------------------------------------------------------------------------------------------

"""
# Getting data from a site or internet in general
import socket
socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket1.connect(("data.pr4e.org", 80))
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\n\n'.encode()
socket1.send(cmd)

while True:
    data = socket1.recv(512)
    if (len(data)) < 1:
        break
    print(data.decode())
socket1.close()

# Unicode Characters and Strings
print(ord("A"))
"""

# ----------------------------------------------------------------------------------------------------------------------

"""
import urllib.error
import urllib.request

eFileHandler = urllib.request.urlopen("http://data.pr4e.org/romeo.txt")
for line in eFileHandler:
    print(line.decode().rstrip())
"""

# ----------------------------------------------------------------------------------------------------------------------

"""
# Using beautiful soup, to find things in a badly coded HTML page: Parsing web pages
import urllib.error
import urllib.request
from bs4 import BeautifulSoup

html = urllib.request.urlopen("https://shiffli-k.github.io/Coursera_HTML/")
bs = BeautifulSoup(html, 'html.parser')

anchor_tags = bs("a")
print(anchor_tags)
for each_tag in anchor_tags:
    print(each_tag.get("href", None))
"""

# ----------------------------------------------------------------------------------------------------------------------

"""
# Quiz What word does the following sequence of numbers represent in ASCII:
Ascii_list = [108, 105, 110, 101]
for each_num in Ascii_list:
    print(chr(each_num))
print(chr(42))
"""

# ----------------------------------------------------------------------------------------------------------------------

# Chapter 13 - Sending data formally in web.
"""
XML Serialization : Where you change internal format for a language to a XML format for web communication 
    to a program that might not be the same.
    Two ways of Doing it : 1. XML 2. JSON
    
    1. XML should follow a schema.
        > A schema is like a validator
        > XSD is a W3c schema
        > Data Types in XSD : Integer, decimal, dateTime, date, string
        > dateTime format : YYYY-MM-DDTHH:MM:SSZ : z is timezone, usually UTC or GMT
"""

# ----------------------------------------------------------------------------------------------------------------------

"""
# JSON Javascript Object Notation
import json
data = '''{
  "name" : "user1",
  "phone" : {
    "type" : "int1",
    "number": "919"
  },
  "email" : {
    "hide" : "yes"
  }
}'''

info = json.loads(data)
# loads stand for Load from string
print(info["email"]["hide"])
"""
# -------------------------------------End of Course 3 : Python Access Web Data-----------------------------------------
