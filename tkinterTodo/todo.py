import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from ttkbootstrap import Style
from tkinter import font
import json


class ModifyTaskDialog(simpledialog.Dialog):
    def __init__(self, parent, title, current_task):
        self.current_task = current_task
        super().__init__(parent, title)

    def body(self, master):
        ttk.Label(master, text="Modify task:").grid(row=0, column=0, sticky="w")
        self.entry = ttk.Entry(master, font=("TkDefaultFont", 16))
        self.entry.insert(tk.END, self.current_task)
        self.entry.grid(row=0, column=1, sticky="w")
        return self.entry

    def apply(self):
        self.result = self.entry.get()

class TodoList(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Todo List")
        self.geometry("500x500")
        style = Style(theme="flatly")
        style.configure("Custom.TEntry", foreground="grey")

        # Icon for the window
        self.iconbitmap(default="tkinterTodo/todoicon.ico")

        # Created input field for adding tasks
        self.task_input = ttk.Entry(self, font=("TkDefaultFont", 16), width=30, style="Custom.TEntry")
        self.task_input.pack(pady=10)

        # Placeholder for input field
        self.task_input.insert(0, "Enter your todo here......")

        # Binding event to clear placeholder when input field is focused
        self.task_input.bind("<FocusIn>", self.clear_placeholder)
        # Binding event to restore placeholder when input field loses focus
        self.task_input.bind("<FocusOut>", self.restore_placeholder)

        # Created button to add tasks
        ttk.Button(self, text="Add", command=self.add_task).pack(pady=5)

        # Created Listbox to display added tasks
        self.task_list = tk.Listbox(self, font=("TkDefaultFont", 16), height=10, selectmode=tk.NONE)
        self.task_list.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Created Button for marking tasks as done or deleting them
        ttk.Button(self, text="Done", style="success.TButton", command=self.mark_done).pack(side=tk.LEFT, padx=10, pady=10)
        ttk.Button(self, text="Delete", style="danger.TButton", command=self.delete_task).pack(side=tk.LEFT, padx=10,
                                                                                               pady=10)

        # Created Button for updating tasks
        ttk.Button(self, text="Modify", style="primary.TButton", command=self.update_task).pack(side=tk.LEFT, padx=10, pady=10)

        # Created Button for displaying task statistics
        ttk.Button(self, text="View Stats", style="info.TButton", command=self.view_tasks).pack(side=tk.RIGHT, pady=10, padx=10)

        self.load_tasks()

    def add_task(self):
        task = self.task_input.get()
        if task != "Enter your todo here......":
            self.task_list.insert(tk.END, task)
            self.task_list.itemconfig(tk.END, fg="orange")
            self.task_input.delete(0, tk.END)
            self.save_tasks()

    def mark_done(self):
        task_index = self.task_list.curselection()
        if task_index:
            self.task_list.itemconfig(task_index, fg="green")
            self.save_tasks()

    def delete_task(self):
        task_index = self.task_list.curselection()
        if task_index:
            self.task_list.delete(task_index)
            self.save_tasks()

    def update_task(self):
        task_index = self.task_list.curselection()
        if task_index:
            current_task = self.task_list.get(task_index[0])
             # Used the custom dialog for modifying the task
            dialog = ModifyTaskDialog(self, "Update Task", current_task)

            if dialog.result is not None:
                new_task = dialog.result
                self.task_list.delete(task_index)
                self.task_list.insert(task_index, new_task)
                self.task_list.itemconfig(task_index, fg="orange")  # Setting the foreground color to orange
                self.save_tasks()

    def view_tasks(self):
        done_count = 0
        total_count = self.task_list.size()
        for i in range(total_count):
            if self.task_list.itemcget(i, "fg") == "green":
                done_count += 1
        messagebox.showinfo("Task statistics", f"Total task : {total_count}\nCompleted tasks : {done_count}")

    def clear_placeholder(self, event):
        if self.task_input.get() == "Enter your todo here......":
            self.task_input.delete(0, tk.END)
            self.task_input.configure(style="TEntry")

    def restore_placeholder(self, event):
        if self.task_input.get() == "":
            self.task_input.insert(0, "Enter your todo here......")
            self.task_input.configure(style="Custom.TEntry")

    def load_tasks(self):
        try:
            with open("tkinterTodo/tasks.json", "r") as f:
                data = json.load(f)
                for task in data:
                    self.task_list.insert(tk.END, task["text"])
                    self.task_list.itemconfig(tk.END, fg=task["color"])
        except FileNotFoundError:
            pass

    def save_tasks(self):
        data = []
        for i in range(self.task_list.size()):
            text = self.task_list.get(i)
            color = self.task_list.itemcget(i, "fg")
            data.append({"text": text, "color": color})
        with open("tkinterTodo/tasks.json", "w") as f:
            json.dump(data, f)


if __name__ == '__main__':
    app = TodoList()
    app.mainloop()
