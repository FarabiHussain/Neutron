import customtkinter as ctk
from components.ctk_xyframe import CTkXYFrame


class Table:
    def __init__(self, master, new_columns=[]) -> None:
        self.parent_frame = ctk.CTkFrame(master)
        self.parent_frame.pack(fill="both", expand=True, padx=10, pady=10)

        self.xy_frame = CTkXYFrame(self.parent_frame)
        self.xy_frame.pack(fill="both", expand=True, padx=0, pady=0)

        if len(new_columns) > 0:
            self.columns = []
            self.set_columns(master, new_columns)

    def set_columns(self, master, new_columns):
        master.grid_columnconfigure(1, weight=1)

        for idx, col in enumerate(new_columns):
            self.columns.append(col)
            print("col: ", col)

            ctk.CTkLabel(
                self.xy_frame, text=col, fg_color="#aaaaaa"
            ).grid(row=0, column=idx, pady=5, padx=5)
