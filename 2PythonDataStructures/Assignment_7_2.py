# Assignment 7.2
user_file_name = input("Enter a file name to capitalize: ")
# user_file_name = "mbox-short"
string_to_find = "X-DSPAM-Confidence:"
counter = 0
confidence_val_total = 0.0
try:
    file_handler = open(user_file_name.lower()+".txt", "r")
except:
    print(user_file_name + " : Does not exist!")
    quit()

for i in file_handler:
    i = i.rstrip()
    if i.startswith(string_to_find):
        counter += 1
        confidence_val_total += float(i[i.find("0"):len(i)])

# print("Total is: " + str(confidence_val_total))
# print("Count is: " + str(counter))
# print("Average is: " + str(round(confidence_val_total/counter, 12)))
print("Average spam confidence: " + str(round(confidence_val_total / counter, 12)))
