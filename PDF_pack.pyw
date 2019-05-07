import tkinter as tk
import PDF_pack_model
import PDF_pack_view

class Controller():
    def __init__(self):
        self.root = tk.Tk()
        self.fenster_breite = 600 
        self.fenster_hoehe = 400 
        self.monitor_breite = self.root.winfo_screenwidth()
        self.monitor_hoehe = self.root.winfo_screenheight()
        self.fenster_start_posX = (self.monitor_breite/2) - (self.fenster_breite/2)
        self.fenster_start_posY = (self.monitor_hoehe/2) - (self.fenster_hoehe/2)
        self.root.title("PDF-pack")#Fenstertitel
        self.root.iconbitmap("PDF_pack.ico")#Icon oben Links vom Fenster
        self.root.resizable(0, 0)#Fenstergrösse kann nicht verstellt werden
        self.root.geometry('%dx%d+%d+%d' %(self.fenster_breite, self.fenster_hoehe, self.fenster_start_posX, self.fenster_start_posY))
        self.model = PDF_pack_model.Model()
        self.view = PDF_pack_view.View(self.root)
        #Buttons PDF:
        self.view.seiten["PDF"].btn_dateien_hinzufügen.bind("<ButtonRelease>", self.pdf_datei_auswahl)
        self.view.seiten["PDF"].btn_letzen_loeschen.bind("<ButtonRelease>", self.pdf_datei_loeschen)
        self.view.seiten["PDF"].btn_druckdatei_erstellen.bind("<ButtonRelease>", self.pdf_zusammenfuegen)

    def run(self):
        self.zeige_seite("PDF")
        self.root.mainloop()

    def zeige_seite(self, seitenname):
        self.view.seiten[seitenname].tkraise()

    def pdf_datei_auswahl(self, event):
        self.view.seiten["PDF"].textfeld_dateien.config(state= "normal")#Textfeld für die Bearbeitung freigeben
        self.dateinamenliste = self.model.pdf_datei_hinzufuegen()
        for dateiname in self.dateinamenliste:
            self.view.seiten["PDF"].textfeld_dateien.insert("1.0",(dateiname+"\n"))#absatz zusätzlich anfügen
        self.view.seiten["PDF"].textfeld_dateien.config(state= "disabled")#Textfeld für die Bearbeitung sperren

    def pdf_datei_loeschen(self, event):
        self.view.seiten["PDF"].textfeld_dateien.config(state = "normal")#Textfeld für die Bearbeitung freigeben
        self.view.seiten["PDF"].textfeld_dateien.delete("1.0","2.0")#Textfeld oberste Zeile löschen
        self.view.seiten["PDF"].textfeld_dateien.config(state= "disabled")#Textfeld für die Bearbeitung sperren
    
    def pdf_zusammenfuegen(self, event):
        self.view.seiten["PDF"].textfeld_dateien.config(state= "normal")#Textfeld für die Bearbeitung freigeben
        self.dateinamenstring = self.view.seiten["PDF"].textfeld_dateien.get("1.0","end")#Textfeldinhalt einlesen
        self.model.pdf_datei_erstellen(self.dateinamenstring)
        self.view.seiten["PDF"].textfeld_dateien.delete("1.0","end")#Textfeldinhalt komplett löschen
        self.view.seiten["PDF"].textfeld_dateien.config(state= "disabled")#Textfeld für die Bearbeitung sperren



                                                          
if __name__ == '__main__':
    app= Controller()
    app.run()

