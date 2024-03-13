import customtkinter as ctk
from components.ctk_xyframe import CTkXYFrame
from CTkTable import *


class Table:
    def __init__(self, master, new_columns=[]) -> None:
        self.parent_frame = ctk.CTkFrame(master)
        self.parent_frame.pack(fill="both", expand=True, padx=10, pady=10)

        self.xy_frame = CTkXYFrame(self.parent_frame)
        self.xy_frame.pack(fill="both", expand=True, padx=0, pady=0)

        self.table = None
        self.columns = new_columns

        if len(new_columns) > 0:
            self.set_columns(new_columns)

    def set_columns(self, new_columns):
        self.table = CTkTable(self.xy_frame, values=new_columns, corner_radius=2)
        self.table.pack(expand=True, fill="both", pady=5, padx=5)

    def set_data(self, new_data):
        for row in new_data:
            self.columns.append(row)

        self.table.destroy()
        self.table = CTkTable(self.xy_frame, values=self.columns, corner_radius=2)
        self.table.pack(expand=True, fill="both", pady=5, padx=5)

