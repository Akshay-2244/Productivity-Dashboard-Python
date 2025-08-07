import tkinter as tk
from tkinter import ttk

from todo import TodoApp
from timer import TimerApp
from alarm import AlarmApp
from quotes import QuoteApp

# Initialize the main window
root = tk.Tk()
root.title("🧠 Smart Productivity Dashboard")
root.geometry("500x400")

# Create notebook
notebook = ttk.Notebook(root)
notebook.pack(expand=1, fill='both')

# Create frames for each tab
todo_frame = tk.Frame(notebook)
timer_frame = tk.Frame(notebook)
alarm_frame = tk.Frame(notebook)
quote_frame = tk.Frame(notebook)

# Add tabs to notebook
notebook.add(todo_frame, text="📝 To-Do")
notebook.add(timer_frame, text="⏳ Timer")
notebook.add(alarm_frame, text="⏰ Alarm")
notebook.add(quote_frame, text="💡 Quote")

# Load each module into its frame
TodoApp(todo_frame)
TimerApp(timer_frame)
AlarmApp(alarm_frame)
QuoteApp(quote_frame)

# Start the application
root.mainloop()

