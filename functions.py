FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):   # use default value if not sent but can be overwritten
    """
        Returns and returns the todos list from the specified file.
        todos.txt by default
    """
    # read items from file to list
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(new_todos, filepath=FILEPATH):   # use default values if not sent but can be overwritten
    """
       writes the todos list sent to the specified file.
       todos.txt by default
    """
    # write list back to file
    with open(filepath, "w") as file:
        file.writelines(new_todos)


if __name__ == "__main__":
    print("Hello name is __main__")
