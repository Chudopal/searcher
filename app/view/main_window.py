from typing import List
import tkinter as tk
import webbrowser


class MainWindow():
    def __init__(self, search_action = None, add_action = None):
        self.search_action = search_action
        self.add_action = add_action
        self.elements: List = list()
        self.initialize()

    def initialize(self):
        self.window  = tk.Tk()
        self.search_button = tk.Button(
            text="Search", command=self.execute_search
        )
        
        self.label = tk.Label(text="Enter the query:")
        self.label.bind("<Button-1>", lambda e: self.callback("https://ru.wikipedia.org"))
        self.entry = tk.Entry(width=50)
        self.elements += [
            self.label,
            self.entry,
            self.search_button
        ]
        self.pack()

    def pack(self):
        for element in self.elements:
            element.pack()

    def execute_search(self):
        self.entry.delete(0, tk.END)

    def callback(self, url):
        webbrowser.open_new(url)

    def apply(self):
        self.window.mainloop()

MainWindow().apply()