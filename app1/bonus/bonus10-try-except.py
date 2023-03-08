try:
    number = float(input("Enter the number: "))
    percent = float(input("Enter the percent: "))

    percent_of_number = number * (percent/100)

    print(f"{round(percent)} percent of {round(number)} is {round(percent_of_number,2)}.")
except ValueError:
    print("Please enter numbers like this: '2' or '7.5' ")


# divide by zero error

try:
    number = int(input("Please enter a number: "))

    result = number / 0
except ZeroDivisionError:
    print("haha silly, can't divide by zero")




