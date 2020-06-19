# Assignment 3.3
try:
    user_input_score = float(input("Enter your score: "))
except:
    print("Enter an Floating point score.")

if 0.0 <= user_input_score <= 1.0:
    if user_input_score >= 0.9:
        print("For the score : " + str(user_input_score) + " you are graded 'A' ")
    elif user_input_score >= 0.8:
        print("For the score : " + str(user_input_score) + " you are graded 'B' ")
    elif user_input_score >= 0.7:
        print("For the score : " + str(user_input_score) + " you are graded 'C' ")
    elif user_input_score >= 0.6:
        print("For the score : " + str(user_input_score) + " you are graded 'D' ")
    else:
        print("For the score : " + str(user_input_score) + " you are graded 'F' \n Good Luck Next Time!, Don't give up!")
else:
    print("Invalid Score: Must be between 0.0 and 1.0")
