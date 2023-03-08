
student_grades = {"Mary": 9.1, "Sim": 8.8, "John": 7.5}

for item in student_grades.items():
    print(item)

for grade in student_grades.values():
    print(grade)

for student in student_grades.keys():
    print(student)

phone_numbers = {"John": "+37682929928", "Marry": "+423998200919"}

for key, value in phone_numbers.items():
    print(f"{key} has as phone number {value}")

#could also use

for pair in phone_numbers.items():
    print(f"{pair[0]} has as phone number {pair[1]}")

#but the first option with key, value is better