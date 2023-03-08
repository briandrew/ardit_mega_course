import parsersd14
import convertersd14

feet_inches = input("Enter feet and inches: ")

parsed_input = parsersd14.parse_input(feet_inches)  # get a dictionary back

result = convertersd14.convert(parsed_input['feet'], parsed_input['inches'])


print(f"{parsed_input['feet']} feet and {parsed_input['inches']} inches is equal to {round(result,2)} meters")


if result < 1:
    print("Kid is too small to ride.")
else:
    print("Kid can ride.")
