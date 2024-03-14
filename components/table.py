from tkinter import StringVar
import customtkinter as ctk
from components.ctk_xyframe import CTkXYFrame
from CTkTable import *


class Table:
    def __init__(self, master, new_headings=[]) -> None:
        self.parent_frame = ctk.CTkFrame(master)
        self.parent_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # add the filters frame
        self.controls_frame = ctk.CTkFrame(self.parent_frame)
        # self.controls_frame.pack(fill="both", expand=True, padx=0, pady=5)
        self.controls_frame.grid(row=0, column=0, pady=1, padx=1, sticky="nsew")

        # add the table of clients
        self.xy_frame = CTkXYFrame(self.parent_frame)
        # self.xy_frame.pack(fill="both", expand=True, padx=0, pady=5)
        self.xy_frame.grid(row=1, column=0, pady=1, padx=1, sticky="nsew", rowspan=3)

        # add the frame that contains operations on the selected client
        self.operations_frame = ctk.CTkFrame(self.parent_frame, height=50)
        # self.operations_frame.pack(fill="both", expand=True, padx=0, pady=5)
        self.operations_frame.grid(row=4, column=0, pady=1, padx=1, sticky="nsew")

        self.parent_frame.grid_rowconfigure(1, weight=1)
        self.parent_frame.grid_columnconfigure(0, weight=1)
        self.parent_frame.grid_propagate(False)

        self.headings = new_headings
        self.rows = []
        self.radio = StringVar(value="")
        self.widths = [200, 300, 300, 200, 100]

        if len(new_headings) > 0:
            self.set_headings(self.headings)

    def set_headings(self, headings):
        for i, col in enumerate(headings):

            ctk.CTkLabel(
                self.xy_frame,
                text=col,
                fg_color="#222222",
                corner_radius=2,
                width=self.widths[i],
            ).grid(row=0, column=i, pady=1, padx=1)

    def set_rows(self, new_data):
        for i, row in enumerate(new_data):

            ctk.CTkRadioButton(
                self.xy_frame,
                width=self.widths[0],
                height=30,
                text=row[0],
                radiobutton_height=15,
                radiobutton_width=15,
                variable=self.radio,
                value=row,
                bg_color="#444444" if i % 2 == 0 else "#333333",
            ).grid(row=(i + 1), column=0, pady=1, padx=1)

            for j, col in enumerate(row):

                if j > 0:
                    ctk.CTkLabel(
                        self.xy_frame,
                        text=col,
                        fg_color="#444444" if i % 2 == 0 else "#333333",
                        corner_radius=2,
                        width=self.widths[j],
                        height=30,
                    ).grid(row=(i + 1), column=j, pady=1, padx=1)

            self.rows.append(row)
