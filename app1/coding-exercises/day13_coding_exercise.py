# def years(year_of_birth, current_year=2023 ):
#     age = current_year - year_of_birth
#     return age
#
#
# birth_year = int(input("What is your year of birth? "))
#
# years_old = years(birth_year)
# if years_old < 100:
#     print(f"You are {years_old} years old!")
# elif years_old >= 100:
#     print(f"Holy shizbot, you are {years_old}!")
#
#
def count_names(names):
    names = names_in.split(',')
    return len(names)


names_in = input("Enter names separated by commas (no spaces): ")

number_of_names = count_names(names_in)

print(number_of_names)


