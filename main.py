
from tkinter import *
from receipt import Receipt
from bill import Bill 

class App(object):

    def __init__(self):
        self.root = Tk()
        self.create_main_widgets()
        self.root.mainloop()

    def create_main_widgets(self):
        self.root.title("Bill - Generator")
        #self.root.call("wm", "attributes", ".", "-fullscreen", "true")
        self.boton_bill = Button(self.root, text="Factura", command=self.Factura)
        self.boton_bill.pack()
        self.boton_receipt = Button(self.root, text="Recibo", command=self.Recibo)
        self.boton_receipt.pack()
        self.boton_budget = Button(self.root, text="Presupuesto", command=self.Presupuesto)
        self.boton_budget.pack()
        
    def Factura(self):
        self.root.destroy()
        self.root = Tk()
        #self.root.call("wm", "attributes", ".", "-fullscreen", "true")
        self.create_bill_widgets()
        self.root.mainloop()

    def Recibo(self):
        self.root.destroy()
        self.root = Tk()
        self.create_receipt_widgets()
        self.root.mainloop()

    def Presupuesto(self):
        self.root.destroy()
        self.root = Tk()
        self.create_budget_widgets()
        self.root.mainloop()


    def create_budget_widgets(self):
        pass
    
    def create_bill_widgets(self):
        #self.root.config(bg="blue")
        self.frame_info_bill = Frame(self.root)
        self.frame_info_bill.pack(fill="x")
        #self.frame_info_bill.config(bg="green", width="400", height="30")
        
        self.label_num_bill = Label(self.frame_info_bill, text="Número factura")
        self.label_num_bill.grid(row=0, column=0)
        self.entry_num_bill = Entry(self.frame_info_bill)
        self.entry_num_bill.grid(row=0, column=1)
        
        self.label_date = Label(self.frame_info_bill, text="Fecha")
        self.label_date.grid(row=0, column=2)
        self.entry_date_day_bill = Entry(self.frame_info_bill)
        self.entry_date_day_bill.grid(row=0, column=3)
        self.entry_date_month_bill = Entry(self.frame_info_bill)
        self.entry_date_month_bill.grid(row=0, column=4)
        self.entry_date_year_bill = Entry(self.frame_info_bill)
        self.entry_date_year_bill.grid(row=0, column=5)


        
        self.frame_client = Frame(self.root)
        self.frame_client.pack(fill="x")
        #self.frame_client.config(bg="red",width="600", height="60")

        self.label_name = Label(self.frame_client, text="Nombre y apellidos")
        self.label_name.grid(row=0, column=0)
        self.label_nif = Label(self.frame_client, text="DNI/NIF")
        self.label_nif.grid(row=0, column=2)
        self.label_address = Label(self.frame_client, text="Domicilio")
        self.label_address.grid(row=1, column=0)
        self.label_population = Label(self.frame_client, text="Población")
        self.label_population.grid(row=1, column=2)
        self.label_postal_code = Label(self.frame_client, text="Código Postal")
        self.label_postal_code.grid(row=2, column=0)
        self.label_taxes = Label(self.frame_client, text="I.V.A")
        self.label_taxes.grid(row=2, column=2)
        self.label_way_to_pay = Label(self.frame_client, text="Modo de pago")
        self.label_way_to_pay.grid(row=2, column=4)
        
        
        self.entry_name_bill = Entry(self.frame_client)
        self.entry_name_bill.grid(row=0, column=1)
        self.entry_nif_bill = Entry(self.frame_client)
        self.entry_nif_bill.grid(row=0, column=3)
        self.entry_address_bill = Entry(self.frame_client)
        self.entry_address_bill.grid(row=1, column=1)
        self.entry_population_bill = Entry(self.frame_client)
        self.entry_population_bill.grid(row=1, column=3)
        self.entry_postal_code_bill = Entry(self.frame_client)
        self.entry_postal_code_bill.grid(row=2, column=1)
        self.entry_taxes_bill = Entry(self.frame_client)
        self.entry_taxes_bill.grid(row=2, column=3)
        self.entry_way_to_pay_bill = Entry(self.frame_client)
        self.entry_way_to_pay_bill.grid(row=2, column=5)
        
        self.frame_description = Frame(self.root)
        self.frame_description.pack(fill="x")
        #self.frame_description.config(bg="yellow", width="400", height="1000")
        for x in range(0,30):
            self.create_description(self.frame_description)

        self.buton = Button(self.root, text="Generar Factura", command=self.generate_bill)
        self.buton.pack(side=RIGHT)

    def create_description(self, frame):
        elementFrame = Frame(frame)
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


    def create_receipt_widgets(self):
        self.label_num_receipt = Label(self.root, text="Recibo Numero")
        self.label_num_receipt.pack()
        self.entry_num_receipt = Entry(self.root)
        self.entry_num_receipt.pack()
        
        self.label_locality_expedition = Label(self.root, text="Localidad de expedición")
        self.label_locality_expedition.pack()
        self.entry_locality_expedition = Entry(self.root)
        self.entry_locality_expedition.pack()
        
        self.label_amount = Label(self.root, text="Importe")
        self.label_amount.pack()
        self.entry_amount = Entry(self.root)
        self.entry_amount.pack()
        
        self.label_date_expedition = Label(self.root, text="Fecha de vencimiento")
        self.label_date_expedition.pack()
        self.entry_date_expedition = Entry(self.root)
        self.entry_date_expedition.pack()
        
        self.label_maturity = Label(self.root, text="Vencimiento")
        self.label_maturity.pack()
        self.entry_maturity = Entry(self.root)
        self.entry_maturity.pack()
        
        self.label_concept = Label(self.root, text="Concepto")
        self.label_concept.pack()
        self.entry_concept = Entry(self.root)
        self.entry_concept.pack()

        
        self.label_payable = Label(self.root, text="Pagadero en (caja o banco)")
        self.label_payable.pack()
        self.entry_payable = Entry(self.root)
        self.entry_payable.pack()
        
        self.label_office = Label(self.root, text="Oficina")
        self.label_office.pack()
        self.entry_office = Entry(self.root)
        self.entry_office.pack()
        
        self.label_account_number = Label(self.root, text="Clave o Nº Cuenta")
        self.label_account_number.pack()
        self.entry_account_number = Entry(self.root)
        self.entry_account_number.pack()
        
        self.label_name_receipt = Label(self.root, text="Nombre")
        self.label_name_receipt.pack()
        self.entry_name_receipt = Entry(self.root)
        self.entry_name_receipt.pack()
        
        self.label_address_receipt = Label(self.root, text="Dirección")
        self.label_address_receipt.pack()
        self.entry_address_receipt = Entry(self.root)
        self.entry_address_receipt.pack()
        
        self.label_population_receipt = Label(self.root, text="Población")
        self.label_population_receipt.pack()
        self.entry_population_receipt = Entry(self.root)
        self.entry_population_receipt.pack()
        

        self.button_generate_receipt = Button(self.root, text="Generar Recibo",
                                              command=self.generar_receipt)
        self.button_generate_receipt.pack()

    def generar_receipt(self):
        num_receipt = self.entry_num_receipt.get()
        locality = self.entry_locality_expedition.get()
        amount = self.entry_amount.get()
        date_issue = self.entry_date_expedition.get()
        maturity = self.entry_maturity.get()
        concept = self.entry_concept.get()
        payable = self.entry_payable.get()
        office = self.entry_office.get()
        account_number = self.entry_account_number.get()
        name_shipper = self.entry_name_receipt.get()
        address = self.entry_address_receipt.get()
        population = self.entry_population_receipt.get()

        
        Receipt(num_receipt, locality, amount, date_issue, maturity, concept,
                payable, office, account_number, address, population,
                name_shipper).generate_pdf()


    def generate_bill(self):
        num_bill = self.entry_num_bill.get()
        date_day_bill = self.entry_date_day_bill.get()
        date_month_bill = self.entry_date_month_bill.get()
        date_year_bill = self.entry_date_year_bill.get()
        name_client_bill = self.entry_name_bill.get()
        nif_bill = self.entry_nif_bill.get()
        address_bill = self.entry_address_bill.get()
        population_bill = self.entry_population_bill.get()
        postal_code = self.entry_postal_code_bill.get()
        taxes_bill = self.entry_taxes_bill.get()
        way_to_pay_bill = self.entry_way_to_pay_bill.get()
        

        #Bill(name_client_bill, "", address_bill, population_bill, postal_code,
        #     num_bill, date_day_bill, date_month_bill, date_year_bill, nif_bill, "diccionario o array", taxes_bill, way_to_pay_bill).generate_pdf()

            

            
            

if __name__ == "__main__":

    aplication = App()
