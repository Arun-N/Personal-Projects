__author__ = 'Arun Nair'

import re
import time

variables = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5}
values = [0, 0, 0, 0, 0, 0]
syntax = ['put', 'show', 'add', 'mult', 'div', 'sub', 'end', 'a', 'b', 'c', 'd', 'e', 'f']


def new_or_load_or_edit():                    # asks user if he wants to create a new file or load existing file
    print("Opening Editor")
    for _ in range(3):
        time.sleep(0.5)
        print(".")

    print("Open NEW file (write 'new') or LOAD saved file (write 'load') or EDIT saved file (write 'edit') ?")
    return input()


def write_prog():                            # function for writing the program
    print("Enter the name of new file")
    file_name = input()
    file_write = open(file_name, 'w')
    print("Enter the program")
    while True:
        inp_text = input()
        if inp_text == 'end':
            file_write.write(inp_text)
            break
        else:
            file_write.write(inp_text + '\n')
            continue

    return file_name


def break_up(file_name):                    # functon for breaking up the content of text file into individual words
    file_read = open(file_name, 'r')
    text = file_read.read()
    print("Reading file")
    time.sleep(1)
    for _ in range(2):
        print(".")
        time.sleep(0.5)
    print(".")
    time.sleep(0.5)

    instr_list = re.sub("[^\w,.'\"#]", " ", text).split()
    file_read.close()
    # print(instr_list)
    return instr_list


def syntax_check(instructions):                          # checks the syntax of written program
    for x in instructions:
        if x in syntax or is_num(x):
            continue
        else:
            print('Syntax error at ' + x)
            return False
    return True


def is_num(num):                                        # checks whether given string is a number
    try:
        int(num)
        return True
    except ValueError:
        return False


def execute(instructions):                              # MAIN PART ----> executes the program written in text file
    counter = 0

    while True:
        instr = instructions[counter]
        counter += 1
        if instr == 'put':
            operand1 = int(instructions[counter])
            counter += 1
            operand2 = instructions[counter]
            values[variables[operand2]] = operand1
            counter += 1
            continue

        elif instr == 'show':
            var_to_show = instructions[counter]
            print("Value in " + var_to_show + ": ", values[variables[var_to_show]])
            counter += 1
            continue

        elif instr == 'add':
            if is_num(instructions[counter]):
                operand1 = int(instructions[counter])
                counter += 1
            else:
                operand1 = values[variables[instructions[counter]]]
                counter += 1

            if is_num(instructions[counter]):
                operand2 = int(instructions[counter])
                counter += 1
            else:
                operand2 = values[variables[instructions[counter]]]
                counter += 1

            dest = instructions[counter]
            s = operand1 + operand2
            values[variables[dest]] = s

        elif instr == 'sub':
            if is_num(instructions[counter]):
                operand1 = int(instructions[counter])
                counter += 1
            else:
                operand1 = values[variables[instructions[counter]]]
                counter += 1

            if is_num(instructions[counter]):
                operand2 = int(instructions[counter])
                counter += 1
            else:
                operand2 = values[variables[instructions[counter]]]
                counter += 1

            dest = instructions[counter]
            s = operand1 - operand2
            values[variables[dest]] = s

        elif instr == 'end':
            print('Simulation Complete')
            break

# ---------------------------------------------------MAIN PROGRAM-------------------------------------------------------
option = new_or_load_or_edit()
if option == 'new':
    file = write_prog()
    commands = break_up(file)
    if syntax_check(commands):
        print("Syntax is correct")
        execute(commands)
else:
    print("Enter the name of saved file")
    file = input()
    try:
        commands = break_up(file)
        if syntax_check(commands):
            print("Syntax is correct")
            execute(commands)
    except FileNotFoundError:
        print("No Such file Found")