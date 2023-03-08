def parse_input(feet_inches):
    parts = feet_inches.split(" ")  # creates a list with items split on what is between ""
    feet = float(parts[0])
    inches = float(parts[1])
    # return feet, inches  # returns a tuple with feet and inches
    return {"feet": feet, "inches": inches}  # used dictionary also for practice
