"""
PdfMerger - merge PDF file to one File
Copyright (C) 2021  Marvin Mangold (Marvin.Mangold00@googlemail.com)
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import tkinter as tk
import tkinter.ttk as ttk
from pathlib import Path


class View(object):
    def __init__(self, master):
        self.container = ttk.Frame(master, style="TFrame")
        self.container.place(x=0, y=0, height="400", width="600")
        self.screens = {"Main": Mainscreen(self.container)}
        for screen in self.screens:
            self.screens[screen].place(x=0, y=0, height="400", width="600")


class Mainscreen(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)
        self.background = tk.Canvas(self)
        self.background.place(x=0, y=0, width=600, height=400)
        self.image = tk.PhotoImage(file=Path("Media/background.png"))
        self.background.create_image(0, 0, anchor="nw", image=self.image)
        # ----------------------------------------------------
        # label actual chosen files
        self.label_chosen_files = ttk.Label(self, text="Files:", style="TLabel")
        self.label_chosen_files.place(x=28, y=60, height=20)
        # entry chosen files
        self.entry_filelist = tk.Text(self, width=10, wrap="word", bg="#3d4145", fg="#ffffff",
                                      bd=5, font=("arial", 10), state="disabled")
        self.entry_filelist.place(x=28, y=85, height=220, width=292)
        # button add file to list
        self.btn_add_file = ttk.Button(self, text="ADD", style="TButton")
        self.btn_add_file.place(x=28, y=310, width=140)
        # button remove file from list
        self.btn_delete_file = ttk.Button(self, text="REMOVE", style="TButton")
        self.btn_delete_file.place(x=180, y=310, width=140)
        # button merge listed files
        self.btn_merge_file = ttk.Button(self, text="MERGE", style="TButton")
        self.btn_merge_file.place(x=28, y=350, width=292, height=35)
