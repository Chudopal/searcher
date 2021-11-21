from typing import List
import webbrowser
import tkinter as tk
from domain.actions import Core


class SearchWindow():
    def __init__(
        self,
        core: Core
    ):
        self.core = core
        self.links: List = list()
        self.initialize()

    def initialize(self):
        self.window  = tk.Tk()
        self.entry = tk.Entry(width=50)
        elements = [
            tk.Button(
                text="Add resource",
                command=self.create_add_resource_area
            ),
            self.entry,
            tk.Button(
                text="Search", command=self.execute_search
            )
        ]
        self.pack(elements)

    def pack(self, elements):
        for element in elements:
            element.pack()

    def create_add_resource_area(self):
        add_window = tk.Toplevel(self.window)
        add_window.title("Add resource window")
        self.add_entry = tk.Entry(add_window,width=50)
        elements = [
            tk.Label(
                add_window,
                text="Type link of resource:"
            ),
            self.add_entry,
            tk.Button(
                add_window,
                text="Add",
                command=self.add_resource
            )
        ]
        self.pack(elements)

    def add_resource(self):
        link_item = self.add_entry.get()
        self.add_entry.delete(0, tk.END)
        if link_item:
            self.core.add_action(link_item)


    def execute_search(self):
        self.delete_elements(self.links)
        search_string = self.entry.get()
        self.entry.delete(0, tk.END)
        if search_string:
            self.links_items = self.core.search_action(
                search_string
            )
            self.add_links()

    def callback(self, url):
        webbrowser.open_new(url)

    def add_links(self):
        for link_item in self.links_items:
            label = tk.Label(
                text=link_item,
                fg="blue"
            )
            label.bind(
                    "<Button-1>",
                    lambda e: self.callback(
                        link_item
                    )
            )
            label.pack()
            self.links.append(label)

    def delete_elements(self, elements):
        for element in elements:
            element.pack_forget()

    def apply(self):
        self.window.mainloop()

