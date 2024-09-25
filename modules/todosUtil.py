EOL = '\n'
FILEPATH = 'data/todos.txt'


def get_todos(file_path=FILEPATH):
    """" Load the todos tasks from file
    and returns a list of todos tasks
    """
    # Read todos tasks
    with open(file_path, 'r') as todosFile:
        todos_returned = todosFile.readlines()
    return todos_returned


def save_todos(todos_arg, file_path=FILEPATH):
    """" Store the todos tasks to a file """
    with open(file_path, 'w') as todosFile:
        todosFile.writelines(todos_arg)


def list_todos(todos_arg):
    """" Show the todos tasks on the terminal """
    # List the todo tasks
    for index, element in enumerate([x.strip(EOL) for x in todos_arg]):
        print(f"{index + 1}.{element}")

def search_index_in_list(lst, value):
    # Use enumerate with lambda to find the index of the first occurrence of 'value' in 'lst'
    return next((index for index, element in enumerate(lst) if element == value), -1)

# todos tasks get print only if todosUtil.py is executed
if __name__ ==  "__main__":
    print(get_todos(f'../{FILEPATH}'))
