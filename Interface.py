try:
    from Tkinter import *
except ImportError:
    from tkinter import *
    

    
root=Tk()
root.title("FacturApp")
#----------------Frame bill info ------------------

infoFrame = Frame(root, width = "1000", height = "200")
infoFrame.pack(fill = "both", expand= "True")

numEntry = Entry(infoFrame)
numEntry.grid(row = 0, column = 1, padx = 50 , pady = 20)

numFactLabel = Label(infoFrame, text ="Numero de factura: ")
numFactLabel.grid(row= 0, column= 0, sticky = "e")

dateEntry = Entry(infoFrame)
dateEntry.grid(row = 0, column = 3)

dateLabel = Label(infoFrame, text = "Fecha")
dateLabel.grid(row = 0, column = 2, sticky = "e")

#----------------Frame client info ---------------

clientFrame = Frame(root, width = 1000, height = 200)
clientFrame.pack(fill = "both", expand= "True")

nameLabel = Label(clientFrame, text="Nombre y apellidos")
nameLabel.grid(row = 0, column = 0, sticky="e")

nameEntry = Entry(clientFrame)
nameEntry.grid(row = 0, column = 1, sticky ="e")

dniLabel = Label(clientFrame, text = "DNI/NIF")
dniLabel.grid(row = 0, column = 2, sticky = "e")

dniEntry = Entry(clientFrame)
dniEntry.grid(row = 0, column = 3, sticky = "e")

addressLabel = Label(clientFrame, text="Domicilio")
addressLabel.grid(row = 1, column = 0, sticky = "e")

addressEntry = Entry(clientFrame)
addressEntry.grid(row = 1, column = 1, sticky = "e")

poblLabel = Label(clientFrame, text = "Poblacion")
poblLabel.grid(row = 1, column = 2, sticky = "e")

poblEntry = Entry(clientFrame)
poblEntry.grid(row = 1, column = 3, sticky = "e")

#----------------Frame material info ------------

materialFrame = Frame(root, width = 1000, height = 200)
materialFrame.pack(fill = "both", expand="True")

element1Frame = Frame(materialFrame)
element1Frame.pack(fill = "both", expand = "True")

element2Frame = Frame(materialFrame)
element2Frame.pack(fill = "both", expand = "True")

element3Frame = Frame(materialFrame)
element3Frame.pack(fill = "both", expand = "True")

element4Frame = Frame(materialFrame)
element4Frame.pack(fill = "both", expand = "True")

element5Frame = Frame(materialFrame)
element5Frame.pack(fill = "both", expand = "True")


class Description:
    def __init__(self, frame):
        elementFrame = Frame (frame)
        elementFrame.pack(fill = "both", expand = "True")

        cuantLabel = Label(elementFrame, text = "Cantidad")
        cuantLabel.grid(row = 0, column = 0, sticky = "e")

        cuantEntry = Entry(elementFrame)
        cuantEntry.grid(row=0, column = 1, sticky = "e")

        descripLabel = Label(elementFrame, text = "Descripcion")
        descripLabel.grid(row = 0, column = 2, sticky = "e")

        descripEntry = Entry(elementFrame)
        descripEntry.grid(row = 0, column = 3, sticky = "e")

        priceLabel = Label(elementFrame, text = "Precio")
        priceLabel.grid(row = 0, column = 4, sticky = "e")

        priceEntry = Entry(elementFrame)
        priceEntry.grid(row = 0, column = 5, sticky = "e")

        importLabel = Label(elementFrame, text = "Importe")
        importLabel.grid(row = 0, column = 6, sticky = "e")

        importEntry = Entry(elementFrame)
        importEntry.grid(row = 0, column = 7)



elemento1 = Description(element1Frame)
elemento2 = Description(element2Frame)
elemento3 = Description(element3Frame)
elemento4 = Description(element4Frame)
elemento5 = Description(element5Frame)

#--------------- Frame button -------------------

def generarFactura():
    print 1
    
generateButton = Button(root, text = "Generar", command = generarFactura)
generateButton.pack()



root.mainloop() 
