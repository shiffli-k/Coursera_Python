def trial():
    # Using Try and except
    integer_value = input("Give an integer")
    try:
        convert_2_int = int(integer_value)
    except:
        print("Not Possibru")


# Assignment 3.1 : Prompt user for hours, rate per hour.
work_hours = float(input("Enter hours worked: "))
rate_per_hour = float(input("Enter the rate per hour"))

gross_pay = work_hours * rate_per_hour

if work_hours > 40:
    bonus_additive = (work_hours - 40.0) * (rate_per_hour * 0.5)
    gross_pay += bonus_additive

print("Pay: " + str(gross_pay))
