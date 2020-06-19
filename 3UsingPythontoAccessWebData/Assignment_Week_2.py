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
