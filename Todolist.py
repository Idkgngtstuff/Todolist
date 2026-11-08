import tkinter as tk
import json
from pathlib import Path

SAVE_FILE =Path(__file__).with_name("tasks.json")
class ToDoList:
    def __init__(self, master):
        self.master = master
        self.master.title("To Do List")
        self.master.geometry("750x500")
        self.master.resizable(False, False)
        self.master.configure(bg="gray20")

        self.tasks = []

        self.task_entry = tk.Entry(self.master, width=30, bg="black", fg="white", insertbackground="white")
        self.task_entry.pack(pady=10)

        self.add_button = tk.Button(self.master, text="Add Task", command=self.add_task, bg="black", fg="white")
        self.add_button.pack(pady=5)

        self.task_listbox = tk.Listbox(self.master, width=50, height=15, bg="black", fg="white", selectbackground="gray", selectforeground="black")
        self.task_listbox.pack(pady=10)

        

        self.file_frame = tk.Frame(self.master,bg="gray20")
        self.file_frame.pack(pady=10)

        self.delete_button = tk.Button(self.file_frame, text="Delete Task", command=self.delete_task, bg="black", fg="white")
        self.delete_button.pack(side="left", padx=5)

        self.check_button = tk.Button(self.file_frame, text="Check Task", command=self.check_task, bg="black", fg="white")
        self.check_button.pack(side="left", padx=5)
        self.update_task_listbox()

        self.save_button = tk.Button(self.file_frame, text="Save Tasks", command=self.save_tasks, bg="black", fg="white")
        self.save_button.pack(side="left", padx=5)

        self.load_button = tk.Button(self.file_frame, text="Load Tasks", command=self.load_tasks, bg="black", fg="white")
        self.load_button.pack(side = "left",padx=5)
        self.load_tasks()

    

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_task_listbox()
            self.task_entry.delete(0, tk.END)

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            del self.tasks[selected_task_index[0]]
            self.update_task_listbox()

    def check_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            index = selected_task_index[0]
            if not self.tasks[index].startswith("✓ "):
                self.tasks[index] = "✓ " + self.tasks[index]
                self.update_task_listbox()

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

    def save_tasks(self):
        SAVE_FILE.write_text(
            json.dumps(self.tasks, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )

    def load_tasks(self):
        if SAVE_FILE.exists():
            self.tasks = json.loads(SAVE_FILE.read_text(encoding="utf-8"))
            self.update_task_listbox()

    class Task:
        def __init__(self, description):
            self.description = description
            self.completed = False

        def mark_completed(self):
            self.completed = True


if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoList(root)
    root.mainloop()


