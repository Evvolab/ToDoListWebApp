def get_todos(filepath='files/todos.txt'):
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath='files/todos.txt'):
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)


if __name__ == '__main__':
    while True:
        user_action = input("type 'add' or 'show' or 'edit':")
        # strip() removes any extra spaces in the match-case input
        user_action = user_action.strip()

        # 'add' to add an item into the toDoList
        if user_action.startswith('add'):
            todo = user_action[4:] + "\n"

            toDoList = get_todos('files/todos.txt')
            toDoList.append(todo)
            # Writing the to-do list items to a file on disk
            write_todos('files/todos.txt', toDoList)

        # 'show' to show the toDoList
        elif user_action.startswith('show'):

            # for loop to iterate over the toDoList and print each item one by one
            toDoList = get_todos('files/todos.txt')
            toDoList = [item.strip('\n') for item in toDoList]
            # print(toDoList)
            for index, item in enumerate(toDoList):
                item = item.title()
                print(f'{index + 1}. {item}')

        elif user_action.startswith('edit'):
            try:
                number = user_action[5:]
                number = int(number)
                number = number - 1

                toDoList = get_todos('files/todos.txt')
                existing_todo = toDoList[number]
                edit = input('Enter the correction')
                toDoList[number] = edit + '\n'
                write_todos('files/todos.txt', toDoList)

            except ValueError:
                print('Input is not Valid')
                continue
        elif user_action.startswith('complete'):
            try:
                number = int(input('Number of todo that is finished'))
                toDoList = get_todos('files/todos.txt')
                toDoList = [item.strip('\n') for item in toDoList]
                index = number - 1
                completed_item = toDoList.pop(index) + "\n"
                toDoList = [i + '\n' for i in toDoList]
                message = f"The task {completed_item} has been marked as completed"
                # print(toDoList)
                print(message)

                # Remove the completed task from the todos list
                write_todos('files/todos.txt', toDoList)
            except IndexError:
                print('There is no to-do with this number')
                continue
        elif user_action.startswith('exit'):
            break
        else:
            print("Command is not valid")

    print('Bye')

    