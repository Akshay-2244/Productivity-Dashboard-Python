import tkinter as tk
from tkinter import messagebox
import datetime
import threading
import time
import winsound  # For beep sound when alarm hits


# Alarm App
class AlarmApp:

    def __init__(self, root):

        # Alarm panel inside a Tkinter frame to set and trigger alarms
        self.root = root
        self.alarm_time = None

        # Header
        header = tk.Label(
            root,
            text="⏰ Alarm Clock",
            font=("Helvetica", 16, "bold")
        )

        # Input fields for hour and minute
        frm = tk.Frame(root)
        frm.pack(pady=5)

        tk.Label(
            frm,
            text="Hour (0-23):",
            font="bold"
        ).grid(row=0, column=0, padx=5)
        self.hour_entry = tk.Entry(frm, width=5)
        self.hour_entry.grid(row=0, column=1)

        tk.Label(
            frm,
            text="Min (0-59):",
            font="bold"
        ).grid(row=1, column=0, padx=5)
        self.minute_entry = tk.Entry(frm, width=5)
        self.minute_entry.grid(row=1, column=1)

        # Alarm button
        set_button = tk.Button(
            root,
            text="Set Alarm",
            command=self.set_alarm,
            bg="#007BFF",
            fg="white"
        )
        set_button.pack(pady=10)

    def set_alarm(self):

        # Reads input, schedules background check for alarm and shows confirmation
        try:
            hour = int(self.hour_entry.get())
            minute = int(self.minute_entry.get())
            if not (0 <= hour <= 23 and 0 <= minute <= 59):
                raise ValueError

        except ValueError:
            messagebox.showerror(
                "Invalid Time",
                "Please enter valid numbers for hour (0–23) and minute (0–59)."
            )
            return

        self.alarm_time = datetime.time(hour, minute)
        messagebox.showinfo(
            "Alarm Set",
            f"Alarm set for {self.alarm_time.strftime('%H:%M')}"
        )
        threading.Thread(target=self._watch_alarm, daemon=True).start()

    def _watch_alarm(self):

        # Background loop that checks time and alerts when alarm time hits
        while True:
            now = datetime.datetime.now().time()
            if now.hour == self.alarm_time.hour and now.minute == self.alarm_time.minute:

                # Ignore if you don't need beep sound
                winsound.Beep(1000, 1000)
                messagebox.showinfo("Alarm", "⏰ Time's up!")
                break
            time.sleep(10)  # check every 10 seconds
