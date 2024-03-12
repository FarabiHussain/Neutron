import customtkinter as ctk
from components.ctk_xyframe import CTkXYFrame


class Table:
    def __init__(self, master, new_columns=[]) -> None:
        self.parent_frame = ctk.CTkFrame(master, fg_color="#444444")
        self.parent_frame.pack(fill="both", expand=True, padx=10, pady=10)

        self.xy_frame = CTkXYFrame(self.parent_frame, fg_color="#444444")
        self.xy_frame.pack(fill="both", expand=True, padx=10, pady=10)

        if len(new_columns) > 0:
            self.columns = []
            self.set_columns(new_columns)

    def set_columns(self, new_columns):
        for col in new_columns:
            self.columns.append(col)
            print(col)
