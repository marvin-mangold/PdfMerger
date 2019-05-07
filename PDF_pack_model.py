import os
import tkinter as tk
from tkinter import filedialog
from PyPDF2 import PdfFileMerger, PdfFileReader

class Model():
    def __init__(self):
        pass

    def pdf_datei_hinzufuegen(self):
        self.dateinamenliste = []
        self.dateidialog = tk.filedialog.askopenfilenames(title= "Dateien auswählen",filetypes= (("pdf Dateien","*.pdf"),))#Dateiauswahldialog öffnen
        for dateiname in self.dateidialog:#Jeden Dateinname der ausgewählt wurde auslesen und als String in das Textfeld schreiben
            self.dateinamenliste.append(dateiname)
        return self.dateinamenliste

    def pdf_datei_erstellen(self, dateinamenstring):
        self.pdf_zusammenfasser = PdfFileMerger()#Pdf-datei handler erstellen
        self.desktop_pfad = os.path.expanduser("~/Desktop/Druckdatei.pdf")
        self.dateinamenstring = dateinamenstring
        self.dateinamenstring = self.dateinamenstring.strip()#Leerzeichen am Anfang und Ende abschneiden
        self.dateinamenliste = self.dateinamenstring.split("\n")#Bei jedem Absatz einen schnitt setzen und alle einzelteile in Liste speichern
        for pdf_dateiname in sorted(self.dateinamenliste):#für jede Datei in der ab jetzt sortierten Liste:
            self.pdf_zusammenfasser.append(PdfFileReader(open(os.path.join(pdf_dateiname), 'rb')))#Datei dem neuen PDF hinzufügen
        self.pdf_zusammenfasser.write(self.desktop_pfad)#neue PDF erstellen
    

