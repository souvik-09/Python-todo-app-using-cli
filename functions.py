file_path = 'todos.txt'

def get_todos(filepath=file_path):
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local 

def write_todos(todos_arg, filepath=file_path):
       with open(filepath, 'w') as file:
            file.writelines(todos_arg)
