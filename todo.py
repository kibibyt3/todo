#!/usr/bin/python3.7

from sys import argv;
from ast import literal_eval;

doneTodo = [];
todoTodo = [];

def main():
    try:
        readList();
        if argv[1] == "add":
            print(add(argv[2]));
        elif argv[1] == "del":
            print(delete(argv[2]));
        elif argv[1] == "todo":
            print(getList());
        elif argv[1] == "do":
            print(do(argv[2]));
        elif argv[1] == "reset":
            print(reset());
        elif argv[1] == "help":
            print(help());
        else:
            print("Argument misunderstood; try help.");
        save();
    except IndexError:
        if argv == ["/home/madkingcabbage/project/todo/todo.py"]:
            print(getList());
        else:
            print("Not enough arguments supplied; try help.");

def readList():
    global doneTodo;
    global todoTodo
    doneTodoString = "";
    todoTodoString = "";
    listFile = open("/home/madkingcabbage/project/todo/todo.list", "r");
    listString = listFile.read();
    listFile.close();
    read = 0;
    tries = 0;
    updateRead = 0;
    for elem in listString:
        if read == 0:
            if elem == '<':
                updateRead = 1
        if elem == '>':
            read = 0  
            tries += 1
        if read == 1:
            if tries == 0:
                doneTodoString += elem
            elif tries == 1:
                todoTodoString += elem
        if updateRead == 1:
            read = 1
            updateRead = 0
    if doneTodoString:
        doneTodo = literal_eval(doneTodoString);
    if todoTodoString:
        todoTodo = literal_eval(todoTodoString);

def save():
    global doneTodo;
    global todoTodo;
    saveString = "<" + str(doneTodo) + ">" + "<" + str(todoTodo) + ">";
    listFile = open("/home/madkingcabbage/project/todo/todo.list", "w");
    listFile.write(saveString);

def add(item):
    global todoTodo;
    todoTodo.append(item);
    return item + " added!";

def delete(item):
    global doneTodo;
    global todoTodo;
    if doneTodo.__contains__(item):
        doneTodo.remove(item);
        return item + " removed!";
    elif todoTodo.__contains__(item):
        todoTodo.remove(item);
        return item + " removed!";
    else:
        return item + " not found!";

def getList():
    global doneTodo;
    global todoTodo;
    return "Done: " + str(doneTodo) + "\nTo do: " + str(todoTodo);

def do(item):
    global doneTodo;
    global todoTodo;
    if todoTodo.__contains__(item):
        todoTodo.remove(item);
        doneTodo.append(item);
        return item + " marked as done!";
    elif doneTodo.__contains__(item):
        return item + " already marked as done!";
    else:
        return item + " not found!";

def reset():
    global doneTodo;
    global todoTodo;
    for elem in doneTodo:
        todoTodo.append(elem);
    while len(doneTodo) != 0:
        del doneTodo[0];
    return "Lists reset!";

def help():
    return("add\ndel\ntodo\ndo\nreset\nhelp");

main();
