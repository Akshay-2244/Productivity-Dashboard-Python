import tkinter as tk
import requests
import threading

API_KEY = "yv9O2+X48AyD2eTZw7j0cQ==rwyqCTAoCzc7btJR"
API_URL = "https://api.api-ninjas.com/v1/quotes"


# Quote App
class QuoteApp:

    def __init__(self, root):

        # Fetches and shows daily quotes via API in a Tkinter frame
        self.root = root

        # Header
        header = tk.Label(
            root,
            text="💡 Daily Quote",
            font=("Helvetica", 16, "bold")
        )
        header.pack(pady=10)

        self.quote_label = tk.Label(
            root,
            text="Fetching quote...",
            wraplength=400,
            justify="center",
            font=("Arial", 12),
            padx=10,
            pady=10
        )
        self.quote_label.pack(pady=10)

        # Refresh button
        self.refresh_button = tk.Button(
            root,
            text="New Quote",
            command=self.fetch_quote_thread,
            bg="#17A2B8",
            fg="white"
        )
        self.refresh_button.pack(pady=5)

        # Initial fetch
        self.fetch_quote_thread()

    def fetch_quote_thread(self):

        # Start a thread to fetch quote without blocking the UI
        threading.Thread(target=self.fetch_quote, daemon=True).start()

    def fetch_quote(self):

        # Calls API, parses JSON and updates the UI with quote and author
        try:
            headers = {'X-Api-Key': API_KEY}
            response = requests.get(API_URL, headers=headers, timeout=5)
            response.raise_for_status()
            data = response.json()[0]
            quote = f"“{data['quote']}”\n\n— {data['author']}"

        except Exception as e:
            quote = f"Error fetching quote. \n{e}"

        self.quote_label.config(text=quote)

