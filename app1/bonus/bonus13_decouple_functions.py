
feet_inches = input("Enter feet and inches: ")


def convert(feet_inches):
    parts = feet_inches.split(" ")  # creates a list with items split on what is between ""
    feet = float(parts[0])
    inches = float(parts[1])
    meters = feet * .3048 + inches * .0254
    return meters


result = convert(feet_inches)

if result < 1:
    print("Kid is too small.")
else:
    print("Kid can ride.")


def cubic_meters(liters_in):
    c_meters = liters_in / 1000
    return c_meters


meters_in = float(input("Enter meters to convert to cubic meters: "))
converted = cubic_meters(meters_in)
print(f"{meters_in} meters = {converted} cubic meters.")

