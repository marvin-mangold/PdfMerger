"""
PdfMerger - merge multiple PDF Files to one File
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
from tkinter import filedialog
from pathlib import Path
import os
import fitz


class Controller(object):
    def __init__(self):
        """
        -initialise window
        -set windowsize and position
        -set title and icon
        -call view class
        -bind button callbacks
        """
        self.root = tk.Tk()
        self.window_width = 600
        self.window_height = 400
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        self.screen_posX = (self.screen_width / 2) - (self.window_width / 2)
        self.screen_posY = (self.screen_height / 2) - (self.window_height / 2)
        self.root.title("PdfMerger")  # window title
        self.root.iconbitmap("Media/icon.ico")  # icon in window titlebar
        self.root.resizable(0, 0)  # lock windowsize
        self.root.geometry('%dx%d+%d+%d' % (self.window_width, self.window_height, self.screen_posX, self.screen_posY))
        # load tkinter ttk style theme
        self.root.tk.call("lappend", "auto_path", Path("Tkinter_Theme/awthemes-9.5.0/"))
        self.root.tk.call("package", "require", Path("awdark"))
        self.style_main = ttk.Style()
        self.style_main.theme_use(Path("awdark"))
        # load screens
        self.container = ttk.Frame(self.root, style="TFrame")
        self.container.place(x=0, y=0, height="400", width="600")
        self.screens = {"Main": Mainscreen(self.container)}
        for screen in self.screens:
            self.screens[screen].place(x=0, y=0, height="400", width="600")
        # buttons:
        self.screens["Main"].btn_add_file.bind("<ButtonRelease>", lambda x: self.file_add())
        self.screens["Main"].btn_delete_file.bind("<ButtonRelease>", lambda x: self.file_delete())
        self.screens["Main"].btn_merge_file.bind("<ButtonRelease>", lambda x: self.file_merge())

    def run(self):
        """
        -open Main screen
        -start mainloop
        """
        self.show_screen("Main")
        self.root.mainloop()

    def show_screen(self, screen="Main"):
        """
        -change screen
        """
        self.screens[screen].tkraise()

    def file_add(self):
        """
        -open filedialog to choose one or more pdf files
        -put the path for each choosed file in a list
        -unlock entry field
        -insert filenames in entry field
        -lock entry field
        """
        # get files
        filelist = []
        files = tk.filedialog.askopenfilenames(title="choose files", filetypes=(("pdf files", "*.pdf"),))
        for file in files:
            filelist.append(file)
        # save files in entry field
        self.screens["Main"].entry_filelist.config(state="normal")  # unlock entry filelist
        for file in filelist:
            self.screens["Main"].entry_filelist.insert("1.0", (file+"\n"))  # put file in entry filelist
        self.screens["Main"].entry_filelist.config(state="disabled")  # lock entry filelist

    def file_delete(self):
        """
        -unlock entry field
        -delete first line in entry field
        -lock entry field
        """
        self.screens["Main"].entry_filelist.config(state="normal")  # unlock entry filelist
        self.screens["Main"].entry_filelist.delete("1.0", "2.0")  # delete first line in entry filelist
        self.screens["Main"].entry_filelist.config(state="disabled")  # lock entry filelist

    def file_merge(self):
        """
        -unlock entry field
        -get all lines from entry field and merge them
        -delete all lines from entry field
        -lock entry field
        """
        path = os.path.expanduser("~/Desktop/merged_file.pdf")
        mergefile = fitz.open()  # create new empty PDF
        self.screens["Main"].entry_filelist.config(state="normal")  # unlock entry filelist
        files = self.screens["Main"].entry_filelist.get("1.0", "end")  # get all lines from entry filelist
        files = files.strip()  # remove whitespace at the beginning and end of string
        files = files.split("\n")  # cut the string at every newline and save the cut strings in a list
        for file in sorted(files):  # sort all pdf files and merge them
            tempfile = fitz.open(file)
            mergefile.insert_pdf(tempfile)
        mergefile.save(path)
        self.screens["Main"].entry_filelist.delete("1.0", "end")  # delete all lines in entry filelist
        self.screens["Main"].entry_filelist.config(state="disabled")  # lock entry filelist


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


if __name__ == '__main__':
    app = Controller()
    app.run()
