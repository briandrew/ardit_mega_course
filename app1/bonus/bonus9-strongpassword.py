password = input("Please enter password: ")

# check password should be 8 or more characters
# used a list and a dictionary for practice

result = []
result_dict = {}
if len(password) >= 8:
    result_dict['length'] = True
    result.append(True)
else:
    result_dict['length'] = False
    result.append(False)

# check password requires at least 3 numbers
# strings have method isdigit a
number_count = []

for char in password:
    if char.isdigit():
        number_count.append(int(char))

if len(number_count) >= 3:
    result.append(True)
    result_dict['numbers'] = True
else:
    result_dict['numbers'] = False
    result.append(False)

# check for >= 1 UPPERCASE character

# strings have isupper method
upper = False
for char in password:
    if char.isupper():
        upper = True
result_dict['upper'] = upper
result.append(upper)
print(result_dict)

# print(result)
# 'all' function returns True if all items are True in this case
# print(all(result)) # very cool, if all items in result[] are evaluate to True, prints True, else False

# if result[0] and result[1] and result[2]:
# so can now use the 'all' function

if all(result):
    if len(password) == 8:
        print(f"your password is {len(password)} which is good but longer is better")
    print("Good strong password")

else:
    print("Your password is weak")

if not result[0]:
    print("Your password is to short")
if not result[1]:
    print("Password needs at least 3 numbers")
if not result[2]:
    print("Password needs at least 1 UPPERCASE letter")

if all(result_dict.values()):
    print(result_dict.values())
    print("strong")
else:
    print(result_dict.values())
    print("weak")
