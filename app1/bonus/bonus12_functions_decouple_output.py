

def parse_input(feet_inches):
    parts = feet_inches.split(" ")  # creates a list with items split on what is between ""
    feet = float(parts[0])
    inches = float(parts[1])
    # return feet, inches  # returns a tuple with feet and inches
    return {"feet": feet, "inches": inches}  # used dictionary also for practice


def convert(feet, inches):  # this function did too much - parsing and conversion - so made another function
    meters = feet * .3048 + inches * .0254
    return meters


feet_inches = input("Enter feet and inches: ")

parsed_input = parse_input(feet_inches)  # get the dictionary back

result = convert(parsed_input['feet'], parsed_input['inches'])


print(f"{parsed_input['feet']} feet and {parsed_input['inches']} inches is equal to {round(result,2)} meters")


if result < 1:
    print("Kid is too small.")
else:
    print("Kid can ride.")

