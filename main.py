import tkinter as tk


class Description:
    def __init__(self, frame):
        elementFrame = tk.Frame(frame)
        elementFrame.pack(fill = "both", expand = "True")

        cuantLabel = tk.Label(elementFrame, text = "Cantidad")
        cuantLabel.grid(row = 0, column = 0, sticky = "e")

        cuantEntry = tk.Entry(elementFrame)
        cuantEntry.grid(row=0, column = 1, sticky = "e")

        descripLabel = tk.Label(elementFrame, text = "Descripcion")
        descripLabel.grid(row = 0, column = 2, sticky = "e")

        descripEntry = tk.Entry(elementFrame)
        descripEntry.grid(row = 0, column = 3, sticky = "e")

        priceLabel = tk.Label(elementFrame, text = "Precio")
        priceLabel.grid(row = 0, column = 4, sticky = "e")

        priceEntry = tk.Entry(elementFrame)
        priceEntry.grid(row = 0, column = 5, sticky = "e")

        importLabel = tk.Label(elementFrame, text = "Importe")
        importLabel.grid(row = 0, column = 6, sticky = "e")

        importEntry = tk.Entry(elementFrame)
        importEntry.grid(row = 0, column = 7)


class App(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        
        #----------------Frame bill info ------------------
        infoFrame = tk.Frame(root, width = "1000", height = "200")
        infoFrame.pack(fill = "both", expand= "True")

        numEntry = tk.Entry(infoFrame)
        numEntry.grid(row = 0, column = 1, padx = 50 , pady = 20)

        numFactLabel = tk.Label(infoFrame, text ="Numero de factura: ")
        numFactLabel.grid(row= 0, column= 0, sticky = "e")
        
        dateEntry = tk.Entry(infoFrame)
        dateEntry.grid(row = 0, column = 3)

        dateLabel = tk.Label(infoFrame, text = "Fecha")
        dateLabel.grid(row = 0, column = 2, sticky = "e")

        #----------------Frame client info ---------------

        clientFrame = tk.Frame(root, width = 1000, height = 200)
        clientFrame.pack(fill = "both", expand= "True")

        nameLabel = tk.Label(clientFrame, text="Nombre y apellidos")
        nameLabel.grid(row = 0, column = 0, sticky="e")
        
        nameEntry = tk.Entry(clientFrame)
        nameEntry.grid(row = 0, column = 1, sticky ="e")
        
        dniLabel = tk.Label(clientFrame, text = "DNI/NIF")
        dniLabel.grid(row = 0, column = 2, sticky = "e")
        
        dniEntry = tk.Entry(clientFrame)
        dniEntry.grid(row = 0, column = 3, sticky = "e")
        
        addressLabel = tk.Label(clientFrame, text="Domicilio")
        addressLabel.grid(row = 1, column = 0, sticky = "e")
        
        addressEntry = tk.Entry(clientFrame)
        addressEntry.grid(row = 1, column = 1, sticky = "e")
        
        poblLabel = tk.Label(clientFrame, text = "Poblacion")
        poblLabel.grid(row = 1, column = 2, sticky = "e")
        
        poblEntry = tk.Entry(clientFrame)
        poblEntry.grid(row = 1, column = 3, sticky = "e")


        #----------------Frame material info ------------

        materialFrame = tk.Frame(root, width = 1000, height = 200)
        materialFrame.pack(fill = "both", expand="True")
        
        element1Frame = tk.Frame(materialFrame)
        element1Frame.pack(fill = "both", expand = "True")
        
        element2Frame = tk.Frame(materialFrame)
        element2Frame.pack(fill = "both", expand = "True")
        
        element3Frame = tk.Frame(materialFrame)
        element3Frame.pack(fill = "both", expand = "True")
        
        element4Frame = tk.Frame(materialFrame)
        element4Frame.pack(fill = "both", expand = "True")
        
        element5Frame = tk.Frame(materialFrame)
        element5Frame.pack(fill = "both", expand = "True")

        
        
        elemento1 = Description(element1Frame)
        elemento2 = Description(element2Frame)
        elemento3 = Description(element3Frame)
        elemento4 = Description(element4Frame)
        elemento5 = Description(element5Frame)

        #--------------- Frame button -------------------

        generateButton = tk.Button(root, text = "Generar", command=generar_button)
        generateButton.pack()
    
    def generar_button(self):
	print(1)



root = tk.Tk()
app = App(master=root)
app.mainloop()
        
