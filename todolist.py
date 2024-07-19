import tkinter as tk
from tkinter import simpledialog, messagebox

class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def __str__(self):
        status = "✔" if self.completed else "✘"
        return f"{status} {self.description}"

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)

    def update_task(self, index, description):
        if 0 <= index < len(self.tasks):
            self.tasks[index].description = description

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].completed = True

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)

    def list_tasks(self):
        return [str(task) for task in self.tasks]

class ToDoApp:
    def __init__(self, root):
        self.todo_list = ToDoList()
        self.root = root
        self.root.title("To-Do List")

        self.task_listbox = tk.Listbox(root)
        self.task_listbox.pack()

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack()

        self.update_button = tk.Button(root, text="Update Task", command=self.update_task)
        self.update_button.pack()

        self.complete_button = tk.Button(root, text="Complete Task", command=self.complete_task)
        self.complete_button.pack()

        self.remove_button = tk.Button(root, text="Remove Task", command=self.remove_task)
        self.remove_button.pack()

    def add_task(self):
        task_description = simpledialog.askstring("Task", "Enter task description:")
        if task_description:
            self.todo_list.add_task(task_description)
            self.update_task_list()

    def update_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            new_description = simpledialog.askstring("Update Task", "Enter new task description:")
            if new_description:
                self.todo_list.update_task(selected_task_index, new_description)
                self.update_task_list()
        except IndexError:
            messagebox.showwarning("Select Task", "Please select a task to update.")

    def complete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            self.todo_list.complete_task(selected_task_index)
            self.update_task_list()
        except IndexError:
            messagebox.showwarning("Select Task", "Please select a task to complete.")

    def remove_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            self.todo_list.remove_task(selected_task_index)
            self.update_task_list()
        except IndexError:
            messagebox.showwarning("Select Task", "Please select a task to remove.")

    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.todo_list.list_tasks():
            self.task_listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()




