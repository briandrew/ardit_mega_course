title = input("Enter title: ")
title_length = len(title)
if title_length < 100:
    print(f"The length is: {title_length} characters")
else:
    print('too long')

print(type(title_length))
