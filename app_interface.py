import tkinter as tk
from tkinter.filedialog import *
import pyttsx3


bienvenue = ("Salut ! Bienvenue dans mon application de conversion de PDF en audio."
             "\n\n Vous avez la possibilité de choisir entre une voix masculine ou féminine."
             "\n Veuillez sélectionner un fichier PDF à convertir en audio.")


class AppInterface(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Pdf To Speech App')
        w, h = self.winfo_screenwidth(), self.winfo_screenheight()
        self.geometry("%dx%d" % (w, h))
        self.label = tk.Label(self, text=bienvenue, font=('OpenSans', 20))
        self.label.pack(pady=10)
        self.button = tk.Button(self, text='Select PDF file', command=self.on_click)
        self.button.pack(pady=10)
        self.engine = pyttsx3.init()
        self.voiceGender = "Male"

    def on_click(self):
        filepath = askopenfilename(title="Ouvrir un document", filetypes=[('pdf files', '.pdf'), ('txt files', '.txt')])
        self.label.config(text='Selected file: ' + filepath)
        self.convert_pdf_to_audio(filepath)

    def run(self):
        self.mainloop()

    def convert_pdf_to_audio(self, filepath):
        self.engine.say("Salut les gars")
        self.engine.runAndWait()