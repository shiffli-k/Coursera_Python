# Assignment 7.1
user_file_name = input("Enter a file name to capitalize: ")
try:
    file_handler = open(user_file_name.lower()+".txt", "r")
except:
    print(user_file_name + " : Does not exist!")
    quit()

for i in file_handler:
    i = i.rstrip()
    print(i.upper())
