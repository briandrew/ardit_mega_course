names = ['john smith', 'jay santi', 'eva kuki']
names = [name.title()for name in names]
print(names)

usernames = ['john 1990', 'alberta1970', 'magnola2000']
num_chars_name = [len(username) for username in usernames]
print(num_chars_name)

user_entries = ['10', '19.1', '20']
floats = [float(entry) for entry in user_entries]
print(floats)
print(sum(floats))