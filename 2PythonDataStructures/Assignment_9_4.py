# Assignment 9.4
file_name = "mbox-short"
file_handler = open(file_name.lower() + ".txt", "r")
email_dict = dict()

for each_line in file_handler:
    if each_line.startswith("From:"):
        current_line = each_line.split()
        email_dict[current_line[1]] = email_dict.get(current_line[1], 0) + 1

largest_value = None
largest_key = None
for key, value in email_dict.items():
    if largest_value is None or largest_value < value:
        largest_value = value
        largest_key = key
print(str(largest_key) + " " + str(largest_value))
