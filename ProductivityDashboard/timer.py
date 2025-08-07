import tkinter as tk


# Timer App
class TimerApp:

    def __init__(self, root):

        # Timer/Stopwatch panel inside a Tkinter frame
        self.root = root
        self.time = 0  # Tracks elaspsed time in seconds
        self.running = False  # Timer state flag

        # Display laber for time (MM:SS)
        self.label = tk.Label(
            root,
            text=self.format_time(),
            font=("Verdana", 30, "bold"),
            fg='#333333'
        )
        self.label.pack(pady=20)

        # Control buttons frame
        button_frame = tk.Frame(root)
        button_frame.pack()

        self.start_button = tk.Button(
            button_frame,
            text="Start",
            width=8,
            command=self.start,
            bg='#4CAF50',
            fg='white')
        self.pause_button = tk.Button(
            button_frame,
            text="Pause",
            width=8,
            command=self.pause,
            bg='#f0ad4e',
            fg='white'
        )
        self.reset_button = tk.Button(
            button_frame,
            text="Reset",
            width=8,
            command=self.reset,
            bg='#d9534f',
            fg='white'
        )

        self.start_button.grid(row=0, column=0, padx=5)
        self.pause_button.grid(row=0, column=1, padx=5)
        self.reset_button.grid(row=0, column=2, padx=5)

    def format_time(self):

        # Returns formatted time string MM:SS from total seconds
        mins = self.time // 60
        secs = self.time % 60
        return f"{mins:02d}:{secs:02d}"

    def update_timer(self):

        # Internal loop that increments time every seond when running
        if self.running:
            self.time += 1
            self.label.config(text=self.format_time())
            self.root.after(1000, self.update_timer)

    def start(self):

        # Starts the timer if not already running
        if not self.running:
            self.running = True
            self.update_timer()

    def pause(self):

        # Pauses the timer
        self.running = False

    def reset(self):

        # Stops the timer and resets the elapsed time to zero
        self.running = False
        self.time = 0
        self.label.config(text=self.format_time())
