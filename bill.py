# -*- coding: utf-8 -*-
import locale 
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

class Bill(object):

    def __init__(self, name, second_name, address, population, postal_code,
                 num_bill, day, month, year, cif, elementos, taxes, way_to_pay):

        self.name = name
        self.second_name = second_name
        self.address = address
        self.population = population
        self.postal_code = postal_code
        self.num_bill = num_bill
        self.day = day
        self.month = month
        self.year = year
        self.cif = cif
        self.elementos = elementos
        self.taxes = taxes
        self.way_to_pay = way_to_pay
        self.total = 0

    def generate_pdf(self):

        locale.setlocale(locale.LC_ALL, '')
        c = canvas.Canvas("Factura.pdf", pagesize=A4)
        c.setLineWidth(.3)
        c.setFont('Helvetica', 9)

        c.drawString(310,730, self.name + " " + self.second_name)
        c.drawString(310, 715, self.address)
        c.drawString(310, 700, self.population)
        c.drawString(310, 685, self.postal_code)

        c.drawString(150, 595, self.num_bill)
        c.drawRightString(360, 595, self.day + " de " + self.month + " de " + self.year)
        c.drawRightString(530, 595, self.cif)

        c.drawString(260, 75, str(self.taxes) + " %")
        c.drawRightString(360, 75, str(locale.format_string("%.2f",
                                                            (self.total*self.taxes)/100,
                                                            grouping = True)))

        c.drawRightString(530, 75, str(locale.format_string("%.2f",
                                                            self.total*(1 + self.taxes/100.),
                                                            grouping = True)))
        c.drawRightString(360, 35, self.way_to_pay)


        
        #------------------- Logo Information ----------------------------
        #c.drawImage("../Bill-Generator/LOGO.png", 30, 630, width = 240, height = 190)
        altura = 710

        c.setFont('Helvetica', 10)
	
        #------------------- Rectangle Info Client Adress ----------------- 
        #canvas.rect(300, 660,230, 100)

        c.line(300, 760, 310, 760)
        c.line(300, 750, 300, 760)

        c.line(300, 660, 300, 670)
        c.line(300, 660, 310, 660)

        c.line(520, 660, 530, 660)
        c.line(530, 660, 530, 670)

        c.line(530, 750, 530, 760)
        c.line(520, 760, 530, 760)

        #------------------- Rectangles Info Bill + NIF -------------------
        c.rect(50, 590, 147.4, 30)
        c.rect(222.4, 590, 147.4, 30)
        c.rect(394.8, 590, 147.4, 30)
        c.setFont('Helvetica', 10)
        c.drawString(51,610, "Nº Factura")
        c.drawString(223.4, 610, "Fecha")
        c.drawString(395.8, 610, "C.I.F./D.N.I.")

        #------------------- Rectangles Total Bill ------------------------
        c.rect(50, 70, 147.4, 30)
        c.rect(222.4, 70, 147.4, 30)
        c.rect(394.8, 70, 147.4,30)

        c.drawString(52, 90, "Importe")
        c.drawString(224.4, 90, "I.V.A.")
        c.drawString(396.8, 90, "Total")

        #------------------- Rectangles Way to pay ------------------------
        c.rect(50, 30, 492.2, 30)
        c.drawString(51, 50, "Forma de pago")

        #------------------- Table Material Description -------------------
        h = A4
        x_list = [50,120, 420, 480, 542.2]
        y_list = [115, 565, 580]
        c.grid(x_list, y_list)
        c.drawString(64, 569, "Cantidad")
        c.drawString(250,569, "Concepto")
        c.drawString(435, 569, "Precio")
        c.drawString(493, 569, "Importe")

        c.rotate(90)
        c.drawString(119, -45, "Andy Murray 929292929W")
        c.save()

