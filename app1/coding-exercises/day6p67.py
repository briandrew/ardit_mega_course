#TODO 1 read essay.txt in
#TODO 2 prints out its text with 1st letter of each word uppercase

file = open(f'../files/essay.txt', 'r')
content = file.read()  # read creates 1 single string
file.close()
print(content.title())
print(len(content))


# Exercise 3
#TODO create a program that asks the user to enter a new member in the command line which adds to members.txt


file = open(f'../files/members.txt', 'a')
new_member = input('Enter new user name - first and last: ')
file.writelines(f'{new_member}\n')
file.close()

file = open(f'../files/members.txt', 'r')
print(file.readlines())
file.close()

filenames = ['doc.txt', 'report.txt', 'presentation.txt']

for name in filenames:
    file = open(name, 'w')
    file.write("hello")
    file.close

#TODO create a program that reads each text file and prints out the content of each in the command line.

filenames = ['../files/a.txt', '../files/b.txt', '../files/c.txt']
for filename in filenames:
    file = open(filename, 'r')
    content = file.read()
    print(content)










