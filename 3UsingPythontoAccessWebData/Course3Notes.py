# Regular Expression
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

"""
sample_String1 = "X-Sumin Value:"
sample_String2 = "X-Woah:"
if re.search("^X-\S*:", sample_String1):
    print(sample_String1)
if re.search("^X-\S*:", sample_String2):
    print(sample_String2)
"""
"""
f_email = "My Email: id is Shiffli.k@gmail.com:, Contact me for info 9954678594."
# email = re.findall("^My.+ (\S+@\S+)", f_email)
email = re.search("[a-z0-9]", f_email)

print(email)
print(re.search("[0-9]+", f_email))
print(re.findall("^M.+:", f_email))
print(re.findall("\S+?@\S+", f_email))
"""

"""
# Assignment Week 2
import re
sum_of_numbers = 0
# file_handler = open("regex_sum_42.txt", "r")
file_handler = open("regex_sum_666383.txt", "r")

for line in file_handler:
    current_line = line.rstrip()
    num_found = re.findall("[0-9]+", current_line)
    if len(num_found) == 0:
        continue
    elif len(num_found) > 1:
        for each_num in num_found:
            sum_of_numbers += int(each_num)
    else:
        sum_of_numbers += int(num_found[0])
print(sum_of_numbers)
"""

"""
# Using these instead of the entire assignment week 2 code.
import re
file_handler = open("regex_sum_666383.txt", "r")
print(sum([each_line for each_line in file_handler ("[0-9)+", file_handler.read())]))
"""

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
"""
