from tkinter import *

class Concept_Line(object):

    def __init__(self):
        self.cuantity = ""
        self.description = ""
        self.price = ""
        self.total = ""


    def create_widgets(self,frame):
        elementFrame = Frame(frame)
        elementFrame.pack(fill = "both", expand = "True")

        self.cuantLabel = Label(elementFrame, text = "Cantidad")
        self.cuantLabel.grid(row = 0, column = 0, sticky = "e")

        self.cuantEntry = Entry(elementFrame)
        self.cuantEntry.grid(row=0, column = 1, sticky = "e")

        self.descripLabel = Label(elementFrame, text = "Descripcion")
        self.descripLabel.grid(row = 0, column = 2, sticky = "e")

        self.descripEntry = Entry(elementFrame)
        self.descripEntry.grid(row = 0, column = 3, sticky = "e")
        
        self.priceLabel = Label(elementFrame, text = "Precio")
        self.priceLabel.grid(row = 0, column = 4, sticky = "e")

        self.priceEntry = Entry(elementFrame)
        self.priceEntry.grid(row = 0, column = 5, sticky = "e")

        self.importLabel = Label(elementFrame, text = "Importe")
        self.importLabel.grid(row = 0, column = 6, sticky = "e")

        self.importEntry = Entry(elementFrame)
        self.importEntry.grid(row = 0, column = 7)

    def get_cuantity(self):
        return str(self.cuantEntry.get())

    def get_description(self):
        return str(self.descripEntry.get())

    def get_amount(self):
        return str(self.priceEntry.get())

    def get_total(self):
        return str(self.importEntry.get())

    def set_amount(self, amount):
        self.amount = amount

    def set_total(self, total):
        self.total = total

    def set_cuantity(self, cuantity):
        self.cuantity = cuantity

    def set_description(self, description):
        self.description = description
        

    
    
