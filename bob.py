import functions
import time

now = time.strftime("%b %d,%Y %H:%M:%S")
print ("it is", now)

while True:
    User_action = input("Type add, show, edit, or exit")
    User_action = User_action.strip()

    if User_action.startswith('add'):
        todo = User_action[4:]


        todos = functions.get_todos()


        todos.append(todo + '\n')

        functions.write_todos(todos)



    elif User_action.startswith('show'):


        todos = functions.get_todos()


        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print (row)


    elif User_action.startswith('edit'):
        try:
            number = int(User_action[5:])
            number = number - 1


            todos = functions.get_todos()


            new_todo = input ('enter a new todo')
            todos[number] = new_todo + '\n'


            functions.write_todos(todos)

        except ValueError:
            print ('Your command is not valid')
            continue


    elif User_action.startswith('complete'):
        try:
            number = int(User_action[9:])


            todos = functions.get_todos()


            index = number - 1
            todo_to_remove = todos[index].strip('\n')

            todos.pop(index)

            functions.write_todos(todos)

            message = f'Todo {todo_to_remove} was removed from the list'
            print(message)
        except IndexError:
            print ("there is no item with that number")
            continue



    elif User_action.startswith('exit'):
        break





    else:
        print ('command is not valid')
        


print ("bye")



