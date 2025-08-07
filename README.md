# 🧠 Productivity Dashboard – Python + Tkinter

A clean and user-friendly productivity dashboard desktop app made with Python.  
It includes a to-do list with checkboxes, a timer/stopwatch, an alarm clock, and a motivational quote generator — all in a simple, unified interface.

---

## 🔧 Features

- ✅ **To-Do List**
  - Add, mark as complete, and remove tasks with double-click.
  - Tasks are saved automatically using local JSON file.

- ⏱ **Timer / Stopwatch**
  - Start, pause, and reset timer.
  - Ideal for productivity sprints (e.g. Pomodoro sessions).

- ⏰ **Alarm Clock**
  - Set a custom time for reminders.
  - Runs in the background and shows an alert when triggered.

- 💬 **Motivational Quotes**
  - Fetches random inspirational quotes from an API.
  - Great for daily motivation.

---

## 🖥️ Tech Stack

- Python 3
- Tkinter (GUI)
- JSON (Local Data Storage)
- API (Quotes) using `requests`
- Threading (for Alarm and API to keep UI responsive)

---

## 📸 Screenshots

---

## 📁 Folder Structure

productivity-dashboard-python/
│
├── main.py # Main app window with all panels
├── todo.py # To-Do List logic and UI
├── timer.py # Timer/Stopwatch logic
├── alarm.py # Alarm functionality
├── quotes.py # Quotes API fetcher
├── data/
│ └── tasks.json # Saved tasks (auto-generated)
├── README.md
└── .gitignore

---
