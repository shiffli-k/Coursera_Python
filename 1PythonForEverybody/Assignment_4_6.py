# Assignment 4.6
def computepay(work_hours, rate_per_hour):
    gross_pay = work_hours * rate_per_hour

    if work_hours > 40:
        bonus_additive = (work_hours - 40.0) * (rate_per_hour * 0.5)
        gross_pay += bonus_additive
    return gross_pay


work_hours = float(input("Enter hours worked: "))
rate_per_hour = float(input("Enter the rate per hour"))
gross_pay = computepay(work_hours, rate_per_hour)
print("Pay " + str(gross_pay))
# ------------End of Day 13-JUN-2020-----------------
