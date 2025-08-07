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
<img width="621" height="532" alt="ProductivityDashboard(ScreenShot-5)" src="https://github.com/user-attachments/assets/9c4cfd61-c993-4168-b636-04d1b74db2e3" />
<img width="617" height="532" alt="ProductivityDashboard(ScreenShot-4)" src="https://github.com/user-attachments/assets/ee2707d5-c53a-4969-a718-a03e95a855a3" />
<img width="620" height="534" alt="ProductivityDashboard(ScreenShot-3)" src="https://github.com/user-attachments/assets/a2412234-e488-4173-977a-78623f1caf37" />
<img width="619" height="534" alt="ProductivityDashboard(ScreenShot-2)" src="https://github.com/user-attachments/assets/caf1e0e1-47bc-4532-bd55-67511dd2c14b" />
<img width="619" height="532" alt="ProductivityDashboard(ScreenShot-1)" src="https://github.com/user-attachments/assets/1892abac-ede2-4bff-997e-40445d7bbe7b" />

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
