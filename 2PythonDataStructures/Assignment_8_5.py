# Assignment 8.5
counter = 0
user_file_name = "mbox-short"
try:
    file_handler = open(user_file_name.lower() + ".txt", "r")
except:
    print(user_file_name + " : Does not exist!")
    quit()
for line in file_handler:
    if line.startswith("From") and not line.startswith("From:"):
        current_line = line.split()
        print(current_line[1])
        counter += 1
print("There were", counter, "lines in the file with From as the first word")
