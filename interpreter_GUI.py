__author__ = 'home'
from tkinter import *
from tkinter.scrolledtext import ScrolledText

root = Tk()

file_name_label = Label(root, text="Filename")
file_name_label.grid(row=0, sticky=W)

file_name_entry = Entry(root)
file_name_entry.grid(row=0, column=1, sticky=W)

label1 = Label(root, text="Enter program Here:")
label1.grid(row=1, sticky=W, pady=10)

main_text_area = ScrolledText(root)
main_text_area.grid(row=2, sticky=W)

root.mainloop()