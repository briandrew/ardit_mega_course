def weather_condition(temp):
    if temp > 7:
        return 'It is warm today'
    else:
        return 'Brr, it is cold'

print()
user_input = float(input("Please enter the temperature: "))
print()
print(weather_condition(user_input))
print()
