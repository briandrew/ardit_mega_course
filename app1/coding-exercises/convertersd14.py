def convert(feet, inches):  # this function did too much - parsing and conversion - so made another function
    meters = feet * .3048 + inches * .0254
    return meters
