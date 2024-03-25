from lib import *
from tkinter import StringVar
import customtkinter as ctk, re
from components.ctk_xyframe import CTkXYFrame
from CTkTable import *


class Table:

    def __init__(self, master, tab, new_headings: list[str] = []) -> None:
        """
        Renders the table including its supporting components
        like the table controls and row operations
        """

        # add the parent frame that holds all of the following
        self.parent_frame = ctk.CTkFrame(master)
        self.parent_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # add the filters frame
        self.controls_frame = ctk.CTkFrame(self.parent_frame)
        self.controls_frame.grid(row=0, pady=3, padx=1, sticky="nsew")

        # add the table of clients
        self.scroll_frame = ctk.CTkScrollableFrame(self.parent_frame)
        self.scroll_frame.grid(row=1, pady=3, padx=1, sticky="nsew", rowspan=3)

        # add the frame that contains operations on the selected client
        self.operations_frame = ctk.CTkFrame(self.parent_frame, height=50)
        self.operations_frame.grid(row=4, pady=3, padx=1, sticky="nsew")

        self.parent_frame.grid_rowconfigure(1, weight=1)
        self.parent_frame.grid_columnconfigure(0, weight=1)
        self.parent_frame.grid_propagate(False)

        self.headings = new_headings
        self.rows = []
        self.radio = StringVar(value="")
        self.widths = [200, 300, 300, 200, 100]
        self.tab = tab

        self.place_delete_button()

        if len(new_headings) > 0:
            self.set_headings(self.headings)

    def set_headings(self, headings: list[str]):
        """Set the table headers using the passed array"""

        for i, col in enumerate(headings):

            self.scroll_frame.grid_columnconfigure(i, weight=1)

            ctk.CTkLabel(
                self.scroll_frame,
                text=col,
                fg_color="#222222",
                corner_radius=2,
            ).grid(
                row=0,
                column=i,
                pady=2,
                padx=2,
                sticky="nsew",
            )

    def set_data_in_cells(self, new_data: list | tuple):
        for i, row in enumerate(new_data):

            row_color = "#444444" if i % 2 == 0 else "#3d3d3d"

            ctk.CTkRadioButton(
                self.scroll_frame,
                height=30,
                text=row[0],
                radiobutton_height=15,
                radiobutton_width=15,
                variable=self.radio,
                value=row,
                bg_color=row_color,
            ).grid(
                row=(i + 1),
                column=0,
                pady=2,
                padx=2,
                sticky="nsew",
            )

            for j, col in enumerate(row):
                if j > 0:
                    ctk.CTkLabel(
                        self.scroll_frame,
                        text=col,
                        fg_color=row_color,
                        corner_radius=2,
                        height=30,
                    ).grid(
                        row=(i + 1),
                        column=j,
                        pady=2,
                        padx=2,
                        sticky="nsew",
                    )

            self.rows.append(row)

    def set_data_in_rows(self, new_data: list | tuple):
        for i, row in enumerate(new_data):

            row_frame = ctk.CTkFrame(
                self.scroll_frame,
                height=40,
                fg_color="#444444" if i % 2 == 0 else "#555555",
            )

            ctk.CTkRadioButton(
                row_frame,
                width=self.widths[0],
                height=30,
                text=row[0],
                radiobutton_height=15,
                radiobutton_width=15,
                variable=self.radio,
                value=row,
            ).grid(
                row=(i + 1),
                column=0,
                pady=1,
                padx=1,
            )

            row_frame.grid(
                row=(i + 1),
                column=0,
                pady=1,
                padx=1,
                columnspan=len(row),
                sticky="nsew",
            )

            for j, col in enumerate(row):
                if j > 0:
                    ctk.CTkLabel(
                        row_frame,
                        text=col,
                        corner_radius=2,
                        width=self.widths[j],
                        height=30,
                    ).grid(
                        row=(i + 1),
                        column=j,
                        pady=1,
                        padx=1,
                    )

            self.rows.append(row)

    def set_data(self, new_data: list | tuple, style: str = "cells"):
        """
        Replace existing table data with the new data.\n
        Set the style as either 'cells' or 'rows'.
        """

        if style == "cells":
            self.set_data_in_cells(new_data)
        elif style == "rows":
            self.set_data_in_rows(new_data)

    def remove_data(self):
        """
        Executes a query to remove the data and another to populate the table.\n
        It re-renders the table to display the updated database
        """

        queries = self.generate_queries()

        vr.db.conn.execute(queries['remove'])
        vr.db.conn.commit()
        table_data = vr.db.conn.execute(queries['populate'])

        self.scroll_frame.destroy()
        self.scroll_frame = ctk.CTkScrollableFrame(self.parent_frame)
        self.scroll_frame.grid(row=1, pady=3, padx=1, sticky="nsew", rowspan=3)

        self.set_headings(self.headings)
        self.set_data(table_data.fetchall())

    def place_delete_button(self):
        master = self.operations_frame

        ctk.CTkButton(
            master,
            text="delete client",
            width=200,
            corner_radius=4,
            fg_color="#1F1E1E",
            command=lambda: self.remove_data(),
        ).grid(
            row=0,
            column=0,
            pady=2,
            padx=2,
            sticky="nsew",
        )

    def generate_queries(self):
        """
        Returns the required query based on the current tab
        """

        # The StringVar gets returned as a string instead of a tuple
        # unfortunately I have to convert this into a list[str] myself
        data = (re.sub("\(|\)|'", "", self.radio.get())).split(", ")

        # define the query which will populate the table again once data is deleted
        if self.tab == "Clients":
            table = "Client"
            populate = """
                SELECT client_uci, first_name, last_name, status_type, cases_qty
                FROM Client
                NATURAL JOIN Status
                LIMIT 50
                """
        elif self.tab == "Documents":
            table = "Document"
            populate = ""
        elif self.tab == "Cases":
            table = "Case"
            populate = ""
        elif self.tab == "Finances":
            table = "Finance"
            populate = ""

        # define the query that needs to run when the button is clicked based on the tab
        # in the converted list above, the 0 index MUST contain the client_uci
        remove = f"""
            DELETE 
            FROM {table} 
            WHERE client_id=(
                SELECT client_id 
                FROM Client 
                WHERE client_uci="{data[0]}"
            )
            """

        return {"remove": remove, "populate": populate}
