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

<img width="619" height="532" alt="ProductivityDashboard(ScreenShot-1)" src="https://github.com/user-attachments/assets/a0729942-a875-47c5-9e2f-e3fc745c3f60" />
<img width="619" height="534" alt="ProductivityDashboard(ScreenShot-2)" src="https://github.com/user-attachments/assets/25ccc186-e574-49a7-b860-ca550f7f2ab4" />
<img width="620" height="534" alt="ProductivityDashboard(ScreenShot-3)" src="https://github.com/user-attachments/assets/3024bcdd-8261-4fdd-b7f9-d8158ca400da" />
<img width="617" height="532" alt="ProductivityDashboard(ScreenShot-4)" src="https://github.com/user-attachments/assets/745c02c3-b253-46ea-b586-dc32e3102236" />
<img width="621" height="532" alt="ProductivityDashboard(ScreenShot-5)" src="https://github.com/user-attachments/assets/ff322555-ad75-4ef6-82c6-30939c3c423b" />

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

## 🚀 How to Run

1. Make sure you have **Python 3.x** installed.
2. Clone the repository:

   ```bash
   git clone https://github.com/Akshay-2244/Productivity-Dashboard-Python.git
   cd productivity-dashboard-python/ProductivityDashboard
   python main.py

---



