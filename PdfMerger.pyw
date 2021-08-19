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
from tkinter import filedialog
from pathlib import Path
import os
import view
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
        self.view = view.View(self.root)
        # load tkinter ttk style theme
        self.root.tk.call("lappend", "auto_path", Path("Tkinter_Theme/awthemes-9.5.0/"))
        self.root.tk.call("package", "require", Path("awdark"))
        self.style_main = ttk.Style()
        self.style_main.theme_use(Path("awdark"))
        # buttons:
        self.view.screens["Main"].btn_add_file.bind("<ButtonRelease>", lambda x: self.file_add())
        self.view.screens["Main"].btn_delete_file.bind("<ButtonRelease>", lambda x: self.file_delete())
        self.view.screens["Main"].btn_merge_file.bind("<ButtonRelease>", lambda x: self.file_merge())

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
        self.view.screens[screen].tkraise()

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
        self.view.screens["Main"].entry_filelist.config(state="normal")  # unlock entry filelist
        for file in filelist:
            self.view.screens["Main"].entry_filelist.insert("1.0", (file+"\n"))  # put file in entry filelist
        self.view.screens["Main"].entry_filelist.config(state="disabled")  # lock entry filelist

    def file_delete(self):
        """
        -unlock entry field
        -delete first line in entry field
        -lock entry field
        """
        self.view.screens["Main"].entry_filelist.config(state="normal")  # unlock entry filelist
        self.view.screens["Main"].entry_filelist.delete("1.0", "2.0")  # delete first line in entry filelist
        self.view.screens["Main"].entry_filelist.config(state="disabled")  # lock entry filelist

    def file_merge(self):
        """
        -unlock entry field
        -get all lines from entry field and merge them
        -delete all lines from entry field
        -lock entry field
        """
        path = os.path.expanduser("~/Desktop/merged_file.pdf")
        mergefile = fitz.open()  # create new empty PDF
        self.view.screens["Main"].entry_filelist.config(state="normal")  # unlock entry filelist
        files = self.view.screens["Main"].entry_filelist.get("1.0", "end")  # get all lines from entry filelist
        files = files.strip()  # remove whitespace at the beginning and end of string
        files = files.split("\n")  # cut the string at every newline and save the cut strings in a list
        for file in sorted(files):  # sort all pdf files and merge them
            tempfile = fitz.open(file)
            mergefile.insert_pdf(tempfile)
        mergefile.save(path)
        self.view.screens["Main"].entry_filelist.delete("1.0", "end")  # delete all lines in entry filelist
        self.view.screens["Main"].entry_filelist.config(state="disabled")  # lock entry filelist


if __name__ == '__main__':
    app = Controller()
    app.run()
