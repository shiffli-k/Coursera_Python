# Assignment 5.2
largest_val = None
smallest_num = None

while True:
    user_data = input("Enter Number: ")
    if user_data.lower() == "done":
        break
    try:
        user_number = int(user_data)
    except:
        print("Invalid input")
        continue
    if largest_val is None:
        largest_val = user_number
    if smallest_num is None:
        smallest_num = user_number
    if user_number > largest_val:
        largest_val = user_number
    if user_number < smallest_num:
        smallest_num = user_number

print("Maximum is " + str(largest_val))
print("Minimum is " + str(smallest_num))

# --------End of course "Python for everybody"--------------"
