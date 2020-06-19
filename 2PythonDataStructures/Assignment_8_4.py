# Assignment 8.4
user_file_name = "romeo"
output_list = list()
try:
    file_handler = open(user_file_name.lower() + ".txt", "r")
except:
    print(user_file_name + " : Does not exist!")
    quit()
for line in file_handler:
    line = line.rstrip()
    split_line = line.split()
    for word in split_line:
        if word in output_list: continue
        output_list.append(word)
output_list.sort()
print(output_list)
