# filenames = ['document', 'report', 'presentation']
# for index, item in enumerate(filenames):
#     print(f"{index} - {item.title()}.txt")

# ips = ['100.122.133.105', '100.122.133.111']
# ip_index = int(input("Please enter a '0' or '1': "))
# for index, item in enumerate(ips):
#     if ip_index == index:
#         print(f"Your ip is: {item}")
    
# # Bug-fixing exercise 1 lesson 57
# menu = ["pasta", "pizza", "salad"]
# user_choice = int(input("Enter the index of the item '0', '1', or '2': ")) # int wasn't there
# message = f"You chose {menu[user_choice]}."
# print(message)

# Bug fixing exercise 2
menu = ["pasta", "pizza", "salad"]
 
for i, j in enumerate(menu):
    print(f"{i}.{j}")

# bug fix exercise 3
menu = ["pasta", "pizza", "salad"]
 
for i, j in enumerate(menu):
    print(f"{i}.{j}")

# iterate over 3 variables example
people = [('John', 'Sen', 'Morro'), ('Lin', 'Ajay', 'Filip')]
for first, second, third in people:
    print(first, second, third)
for index, item in enumerate(people):
    print(index, item)