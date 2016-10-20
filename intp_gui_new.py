# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'intp_gui_new.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import re
import webbrowser

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_Dialog(object):

    def __init__(self):
        self.variables = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5}
        self.values = [0, 0, 0, 0, 0, 0]
        self.syntax = ['put', 'show', 'add', 'mul', 'div', 'sub', 'and', 'or', 'not', 'end', 'a', 'b', 'c', 'd', 'e', 'f']
        self.syntax_correct = True

    def setupUi(self, Dialog):

        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(517, 566)

        self.horizontalLayoutWidget = QtGui.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 451, 41))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))

        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))

        self.file_name = QtGui.QLabel(self.horizontalLayoutWidget)
        self.file_name.setObjectName(_fromUtf8("file_name"))

        self.horizontalLayout.addWidget(self.file_name)

        self.file_name_input = QtGui.QLineEdit(self.horizontalLayoutWidget)
        self.file_name_input.setObjectName(_fromUtf8("file_name_input"))

        self.horizontalLayout.addWidget(self.file_name_input)

        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 50, 101, 16))
        self.label.setObjectName(_fromUtf8("label"))

        self.main_window_area = QtGui.QTextEdit(Dialog)
        self.main_window_area.setGeometry(QtCore.QRect(10, 70, 311, 191))
        self.main_window_area.setObjectName(_fromUtf8("main_window_area"))

        self.run = QtGui.QPushButton(Dialog)
        self.run.setGeometry(QtCore.QRect(10, 280, 101, 23))
        self.run.setObjectName(_fromUtf8("run"))
        self.run.clicked.connect(self.compile_n_run)

        self.help = QtGui.QPushButton(Dialog)
        self.help.setGeometry(QtCore.QRect(370, 120, 91, 61))
        self.help.setObjectName(_fromUtf8("help"))
        self.help.clicked.connect(self.open_help)

        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 320, 46, 13))
        self.label_2.setObjectName(_fromUtf8("label_2"))

        self.textEdit = QtGui.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(10, 340, 311, 191))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "College OS Project Compiler", None))
        self.file_name.setText(_translate("Dialog", "File Name", None))
        self.label.setText(_translate("Dialog", "Enter Program Here:", None))
        self.run.setText(_translate("Dialog", "Compile and Run", None))
        self.help.setText(_translate("Dialog", "Help", None))
        self.label_2.setText(_translate("Dialog", "Output:", None))

    def compile_n_run(self):
        prog_file_name = self.file_name_input.text()
        if prog_file_name == '':
            self.textEdit.setText("Enter a valid filename")
            # print("Enter a valid filename")
        else:
            program = self.main_window_area.toPlainText()
            if program == '':
                self.textEdit.setText("Enter a program")
                # print("Enter a program")
            else:
                file_write = open(prog_file_name, 'w')
                file_write.write(program)
                file_write.close()

                self.instr_list = re.sub("[^\w,.'\"#]", " ", program).split()
                print(self.instr_list)
                for x in self.instr_list:
                    if x in self.syntax or self.is_num(x):
                        continue
                    else:
                        self.textEdit.setText("Syntax error at " + x)
                        self.syntax_correct = False
                        break

                if self.syntax_correct:
                    self.textEdit.setText("Syntax Correct")
                    self.execute(self.instr_list)

    def is_num(self, num):                # checks whether given string is a number
        try:
            int(num)
            return True
        except ValueError:
            return False

    def execute(self, instructions):                              # MAIN PART ----> executes the program written in text file
        counter = 0

        while True:
            instr = instructions[counter]
            counter += 1
            if instr == 'put':
                operand1 = int(instructions[counter])
                counter += 1
                operand2 = instructions[counter]
                self.values[self.variables[operand2]] = operand1
                counter += 1
                continue

            elif instr == 'show':
                var_to_show = instructions[counter]
                self.ans = "Value in " + var_to_show + ": " + str(self.values[self.variables[var_to_show]])
                self.textEdit.setText(self.ans)
                # print("Value in " + var_to_show + ": ", self.values[self.variables[var_to_show]])
                counter += 1
                continue

            elif instr == 'add':
                if self.is_num(instructions[counter]):
                    operand1 = int(instructions[counter])
                    counter += 1
                else:
                    operand1 = self.values[self.variables[instructions[counter]]]
                    counter += 1

                if self.is_num(instructions[counter]):
                    operand2 = int(instructions[counter])
                    counter += 1
                else:
                    operand2 = self.values[self.variables[instructions[counter]]]
                    counter += 1

                dest = instructions[counter]
                s = operand1 + operand2
                self.values[self.variables[dest]] = s

            elif instr == 'sub':
                if self.is_num(instructions[counter]):
                    operand1 = int(instructions[counter])
                    counter += 1
                else:
                    operand1 = self.values[self.variables[instructions[counter]]]
                    counter += 1

                if self.is_num(instructions[counter]):
                    operand2 = int(instructions[counter])
                    counter += 1
                else:
                    operand2 = self.values[self.variables[instructions[counter]]]
                    counter += 1

                dest = instructions[counter]
                s = operand1 - operand2
                self.values[self.variables[dest]] = s

            elif instr == 'mul':      # Change it
                if self.is_num(instructions[counter]):
                    operand1 = int(instructions[counter])
                    counter += 1
                else:
                    operand1 = self.values[self.variables[instructions[counter]]]
                    counter += 1

                if self.is_num(instructions[counter]):
                    operand2 = int(instructions[counter])
                    counter += 1
                else:
                    operand2 = self.values[self.variables[instructions[counter]]]
                    counter += 1


                dest = instructions[counter]
                s = operand1 * operand2
                self.values[self.variables[dest]] = s

            elif instr == 'div':      # Change it
                if self.is_num(instructions[counter]):
                    operand1 = int(instructions[counter])
                    counter += 1
                else:
                    operand1 = self.values[self.variables[instructions[counter]]]
                    counter += 1

                if self.is_num(instructions[counter]):
                    operand2 = int(instructions[counter])
                    counter += 1
                else:
                    operand2 = self.values[self.variables[instructions[counter]]]
                    counter += 1

                dest = instructions[counter]
                try:
                    s = operand1 / operand2
                except ZeroDivisionError:
                    s = 'N/A'
                self.values[self.variables[dest]] = s

            elif instr == 'and':
                if self.is_num(instructions[counter]):
                    operand1 = int(instructions[counter])
                    counter += 1
                else:
                    operand1 = self.values[self.variables[instructions[counter]]]
                    counter += 1

                if self.is_num(instructions[counter]):
                    operand2 = int(instructions[counter])
                    counter += 1
                    bin2 = bin(operand2)
                else:
                    operand2 = self.values[self.variables[instructions[counter]]]
                    counter += 1

                dest = instructions[counter]
                s = operand1 and operand2
                self.values[self.variables[dest]] = s

            elif instr == 'or':
                if self.is_num(instructions[counter]):
                    operand1 = int(instructions[counter])
                    counter += 1
                else:
                    operand1 = self.values[self.variables[instructions[counter]]]
                    counter += 1

                if self.is_num(instructions[counter]):
                    operand2 = int(instructions[counter])
                    counter += 1
                else:
                    operand2 = self.values[self.variables[instructions[counter]]]
                    counter += 1

                dest = instructions[counter]
                s = operand1 or operand2
                self.values[self.variables[dest]] = s

            elif instr == 'not':
                if self.is_num(instructions[counter]):
                    operand1 = int(instructions[counter])
                    counter += 1
                else:
                    operand1 = self.values[self.variables[instructions[counter]]]
                    counter += 1

                dest = instructions[counter]
                s = not operand1
                self.values[self.variables[dest]] = s

            elif instr == 'end':
                print('Simulation Complete')
                break

    def open_help(self):
        webbrowser.open("ASP_help.txt")


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

