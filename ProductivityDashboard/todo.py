import tkinter as tk
from tkinter import messagebox
import json
import os

# File to store tasks
TASKS_FILE = "data/tasks.json"


# File I/O functions


def save_tasks(tasks):

    # Save tasks to a JSON file with their completion status
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)


def load_tasks():

    # Load tasks from the JSON file
    # Returns a list of dictionaries with 'text' and 'done' keys
    # If file doesn't exist, return an empty list
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, 'r') as f:
        return json.load(f)


# To-Do App
class TodoApp:

    def __init__(self, root):

        # Initialize the To-Do list tab
        self.root = root
        self.tasks = load_tasks()
        self.task_vars = []  # Holds IntVars linked to checkboxes

        # ------------- UI Layout -------------

        # Title
        title = tk.Label(
            root,
            text="📝 Your Tasks",
            font=("Helvetica", 16, "bold")
        )
        title.pack(pady=10)

        # Input field for adding tasks
        input_frame = tk.Frame(root)
        input_frame.pack(pady=5)

        self.task_entry = tk.Entry(input_frame, width=30, font=("Arial", 12))
        self.task_entry.grid(row=0, column=0, padx=5)

        # Add Task button
        add_button = tk.Button(
            input_frame,
            text="➕ Add Task",
            font=("Arial", 10, "bold"),
            bg="#4CAF50",
            fg="white",
            command=self.add_task
        )
        add_button.grid(row=0, column=1)

        # Scrollable task area
        self.task_frame = tk.Frame(root)
        self.task_frame.pack(fill='both', expand=True, padx=10, pady=10)

        # Canvas inside frame (for scrolling)
        self.canvas = tk.Canvas(self.task_frame)
        self.scrollbar = tk.Scrollbar(
            self.task_frame,
            orient="vertical",
            command=self.canvas.yview
        )
        self.scrollable_frame = tk.Frame(self.canvas)

        # Bind scrolling
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all"))
        )

        # Attach frame to canvas
        self.canvas.create_window(
            (0, 0),
            window=self.scrollable_frame,
            anchor="nw"
        )
        self.scrollbar.pack(side="right", fill="y")

        # Display canvas and scrollbar
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        # Load and show tasks
        self.load_task_list()

    def add_task(self):

        # Add a task from the entry field to the list and save it
        task = self.task_entry.get().strip()
        if task:
            self.tasks.append({"task": task, "done": False})
            self.task_entry.delete(0, tk.END)
            self.update_listbox()
            save_tasks(self.tasks)
        else:
            messagebox.showwarning("Input Error", "Please enter a task.")

    def toggle_task(self, index):

        # Toggle the 'done' status of a task when checkbox is clicked
        self.tasks[index]["done"] = not self.tasks[index]["done"]
        save_tasks(self.tasks)

    def remove_task(self, event, index):

        # Remove a task when it's double-clicked in the list
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            self.update_listbox()
            save_tasks(self.tasks)

    def update_listbox(self):

        # Redraw all checkboxes and task labels in the scrollable panel

        # Clear previous task widgets
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        self.task_vars = []

        for idx, task in enumerate(self.tasks):
            var = tk.IntVar(value=1 if task["done"] else 0)

            # Create checkbox for each task
            cb = tk.Checkbutton(
                self.scrollable_frame,
                text=task["task"],
                variable=var,
                font=("Arial", 11),
                anchor="w",
                command=lambda i=idx: self.toggle_task(i)
            )

            # Double-click event to delete task
            cb.bind(
                "<Double-Button-1>",
                lambda e,
                i=idx: self.remove_task(e, i)
            )

            cb.pack(fill="x", pady=2, anchor="w")
            self.task_vars.append(var)

    def load_task_list(self):

        # Load tasks from file and display them in the UI
        self.update_listbox()

