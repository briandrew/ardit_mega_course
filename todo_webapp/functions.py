FILEPATH = 'todos.txt'


def get_todos(filepath=FILEPATH):  # set default file path so don't need to re-specify in code
    """ returns existing todos from text file """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ modifies existing todos file with updates """
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)


'''any valid code outside of the defs will be run when imported.
to prevent that, and only run when the module is directly executed, 
perhaps for testing, we use the following '''

if __name__ == "__main__":  # main is only main when run directly, else 'functions' in this case
    # anything we want to execute
    print('x')
