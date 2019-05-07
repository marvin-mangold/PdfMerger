import tkinter as tk
from PIL import ImageTk

class View():
    def __init__(self, master):
        self.container = tk.Frame(master)
        self.container.place(x=0, y=0, height="400", width="600")
        self.seiten={"PDF":seite_pdf_zusammenfuegen(self.container)}
        for s in self.seiten:
            self.seiten[s].place(x=0, y=0, height="400", width="600")
                
class seite_pdf_zusammenfuegen(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.hintergrundbild = tk.Canvas(self)
        self.hintergrundbild.place(x=0,y=0,width=600,height=400)
        self.image = ImageTk.PhotoImage(file = "Background.png")
        self.hintergrundbild.create_image(0, 0, anchor= "nw", image = self.image)
        #----------------------------------------------------
        #Label fuer aktuelle Dateien erstellen
        self.label_dateien = tk.Label(self, text="Ausgewählte Dateien:")    
        self.label_dateien.place(x=28, y=60 ,height=20)
        #Textfeld fuer Dateien erstellen
        self.textfeld_dateien = tk.Text(self, width=10, wrap="word")
        self.textfeld_dateien.place(x=28, y=85, height=220, width=292)
        #Button fuer Dateien hinzufügen erstellen.
        self.btn_dateien_hinzufügen = tk.Button(self, text="Dateien hinzufügen")
        self.btn_dateien_hinzufügen.place(x=28, y=310, width=140)
        #Button Letzen Eintrag entfernen erstellen.
        self.btn_letzen_loeschen = tk.Button(self, text="Letzten Eintrag entfernen")
        self.btn_letzen_loeschen.place(x=180, y=310, width=140)
        #Button Druckdatei erstellen erstellen.
        self.btn_druckdatei_erstellen = tk.Button(self, text="Druckdatei erstellen")
        self.btn_druckdatei_erstellen.place(x=28, y=350, width=292, height= 35)
