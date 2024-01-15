# To-Do App


![image](https://github.com/ali0999109/todo-app/assets/145396907/4309c3f7-2550-4659-99db-23d8bbed5077)

# Code

```python import functions
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
        


print ("bye")...



-----------------------------------------------

## Back end code

FILEPATH = 'bob.txt'


def get_todos(filepath=FILEPATH):
    """ read a text file and return the of
    to-do items.

    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()

    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """write the to-do items list into the text file"""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)



# GUI interface for todo-app

import functions
import PySimpleGUI as sg
import time

sg.theme("Black")

clock = sg.Text('',key='clock')
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip= 'enter todo', key = 'todo')
add_button = sg.Button("add")
list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=[45, 10])
edit_button = sg.Button('Edit')
complete_button = sg.Button('Complete')
exit_button = sg.Button('Exit')

window = sg.Window('My to-do app',
                   layout=[[clock],
                           [label],
                           [input_box,add_button],
                           [list_box,edit_button,complete_button],
                           [exit_button]],
                   font=('Helvetica',20))
while True:
    event, values = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%b %d,%Y %H:%M:%S"))
    match event:
        case "add":
            todos = functions.get_todos()
            new_todos = values['todo'] + '\n'
            todos.append(new_todos)
            functions.write_todos(todos)
            window['todos'].update(values=todos)


        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("please select an item first",font=('Helvetica',15))

        case 'Complete':
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup("please select an item first",font=('Helvetica',15))


        case 'Exit':
            break



        case 'todos':
            window['todo'].update(value=values['todos'][0])


        case sg.WIN_CLOSED:
            break


window.close()













