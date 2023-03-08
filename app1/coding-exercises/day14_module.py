# constants (don't change them) denoted by ALL UPPER

FREEZING_POINT = 0
BOILING_POINT = 100


def water_state(temp):
    """uses temp to determine if water is solid, liquid, or gas"""
    if temp >= BOILING_POINT:
        state = 'gas'
    elif temp <= FREEZING_POINT:
        state = 'solid'
    else:
        state = 'liquid'

    return state
