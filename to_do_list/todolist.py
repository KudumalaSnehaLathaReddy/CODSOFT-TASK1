
from tkinter import *
from tkinter import ttk

class ToDoList:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do-List")
        self.root.geometry('650x410+300+150')

        self.label = Label(self.root, text='To-Do-List-App',
                           font='ariel, 25 bold', width=10, bd=5, bg='yellow', fg='black')
        self.label.pack(side='top', fill=BOTH)

        self.label2 = Label(self.root, text='Add Task',
                            font='ariel, 18 bold', width=10, bd=5, bg='pale green', fg='black')
        self.label2.place(x=40, y=50)

        self.label3 = Label(self.root, text='Tasks',
                            font='ariel, 18 bold', width=10, bd=5, bg='pale green', fg='black')
        self.label3.place(x=350, y=50)

        self.main_text = Listbox(self.root, height=8, bd=5, width=25, font='arial 20 italic bold')
        self.main_text.place(x=250, y=100)

        self.text = Text(self.root, bd=5, height=3, width=30, font='ariel, 10 bold')
        self.text.place(x=20, y=120)

        def add():
            content = self.text.get(1.0, END).strip()
            if content:
                self.main_text.insert(END, content)
                with open('data.txt', 'a') as file:
                    file.write(content + '\n')
                self.text.delete(1.0, END)

        def delete():
            delete_ = self.main_text.curselection()
            if delete_:
                look = self.main_text.get(delete_)
                with open("data.txt", 'r+') as f:
                    new_f = f.readlines()
                    f.seek(0)
                    for line in new_f:
                        if look != line.strip():
                            f.write(line)
                    f.truncate()
                self.main_text.delete(delete_)

        with open('data.txt', 'r') as file:
            read = file.readlines()
            for line in read:
                self.main_text.insert(END, line.strip())

        self.button_add = Button(self.root, text="Add", font='sarif, 20 bold italic',
                                 width=10, bd=5, bg='green', fg='black', command=add)
        self.button_add.place(x=30, y=180)

        self.button_delete = Button(self.root, text="Delete", font='sarif, 20 bold italic',
                                    width=10, bd=5, bg='red', fg='black', command=delete)
        self.button_delete.place(x=30, y=250)

def main():
    root = Tk()
    ui = ToDoList(root)
    root.mainloop()

if __name__ == "__main__":
    main()
