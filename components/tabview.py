import customtkinter as ctk
from lib import *


class Tabview:
    def __init__(self, master, new_tabs=[]) -> None:

        self.tabview = ctk.CTkTabview(
            master,
            fg_color="#111111",
            border_color="white",
            border_width=1,
            segmented_button_fg_color="#111111",
            segmented_button_unselected_color="black",
            segmented_button_selected_color="#444444",
        )

        self.tabview.pack(expand=True, fill="both", padx=10, pady=10)

        if len(new_tabs) > 0:
            self.tabs = {}
            self.set_tabs(new_tabs)

    def set_tabs(self, new_tabs):
        for tab in new_tabs:
            tab_obj = self.tabview.add(tab)
            self.tabs[tab] = tab_obj

    def get_tabs(self):
        return self.tabs
