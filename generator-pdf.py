# -*- coding: utf-8 -*-
import locale 
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont


locale.setlocale(locale.LC_ALL, '')

canvas = canvas.Canvas("form.pdf", pagesize = A4)
canvas.setLineWidth(.3)


print("Bienvenido al generador de facturas Versión 1.0\n")
print("De momento solo existe un formulario. En un futuro muy próximo se podrá elegir que modelo de factura se quiera escoger\n")

print("Comenzamos con la introducción de datos!!!!. Introduzca los datos poquito a poco y la factura se generará en un plis plas.")

canvas.setFont('Helvetica', 9)

name = raw_input("Nombre y apellidos: ")
address = raw_input("Dirección: ")
population = raw_input("Población: ")
postal_code = raw_input("Código postal: ")

canvas.drawString(310, 730, name)
canvas.drawString(310, 715, address)
canvas.drawString(310, 700, population)
canvas.drawString(310, 685, postal_code)

num_Bill = raw_input("Número de factura: ")
day = raw_input("Día: ")
month = raw_input("Mes: ")
year = raw_input("Año: ")
cif = raw_input("C.I.F./D.N.I.: ")

canvas.drawString(150, 595, num_Bill)
canvas.drawRightString(360, 595, day + " de " + month + " de " + year)
canvas.drawRightString(530, 595, cif)

num_material = input("Introduzca el número de conceptos que va a querer introducir: ")
total = 0
height = 550
for i in range(num_material):
    print("-------------------------Elemento " + str(i) + "------------------------")
    cuantity = input("Cantidad (0 en caso de caso vacío)\n")
    description = raw_input("Concepto\n")
    prize = input("Precio\n")
    total += cuantity*prize
    canvas.drawCentredString(84,height - 15*i, str(cuantity))
    canvas.drawString(130, height - 15*i, description)
    canvas.drawRightString(474, height - 15*i, str(locale.format_string("%.2f", prize, grouping=True)))
    canvas.drawRightString(537, height - 15*i, str(locale.format_string("%.2f", cuantity*prize, grouping = True)))

canvas.drawRightString(175, 75, str(locale.format_string("%.2f", total, grouping = True)))

taxes = input("I.V.A. : ")
canvas.drawString(260, 75, str(taxes)+" %")
canvas.drawRightString(360, 75, str(locale.format_string("%.2f",(total*taxes)/100, grouping = True)))

canvas.drawRightString(530, 75, str(locale.format_string("%.2f",total*(1 + taxes/100.), grouping = True)))
way_to_pay = raw_input("Forma de pago")
canvas.drawRightString(360, 35, way_to_pay)

#------------------- Logo Information ----------------------------
canvas.drawImage("../Bill-Generator/LOGO.png", 30, 630, width = 240, height = 190)
altura = 710

canvas.setFont('Helvetica', 10)
	
#------------------- Rectangle Info Client Adress ----------------- 
#canvas.rect(300, 660,230, 100)

canvas.line(300, 760, 310, 760)
canvas.line(300, 750, 300, 760)

canvas.line(300, 660, 300, 670)
canvas.line(300, 660, 310, 660)

canvas.line(520, 660, 530, 660)
canvas.line(530, 660, 530, 670)

canvas.line(530, 750, 530, 760)
canvas.line(520, 760, 530, 760)

#------------------- Rectangles Info Bill + NIF -------------------
canvas.rect(50, 590, 147.4, 30)
canvas.rect(222.4, 590, 147.4, 30)
canvas.rect(394.8, 590, 147.4, 30)
canvas.setFont('Helvetica', 10)
canvas.drawString(51,610, "Nº Factura")
canvas.drawString(223.4, 610, "Fecha")
canvas.drawString(395.8, 610, "C.I.F./D.N.I.")

#------------------- Rectangles Total Bill ------------------------
canvas.rect(50, 70, 147.4, 30)
canvas.rect(222.4, 70, 147.4, 30)
canvas.rect(394.8, 70, 147.4,30)

canvas.drawString(52, 90, "Importe")
canvas.drawString(224.4, 90, "I.V.A.")
canvas.drawString(396.8, 90, "Total")

#------------------- Rectangles Way to pay ------------------------
canvas.rect(50, 30, 492.2, 30)
canvas.drawString(51, 50, "Forma de pago")
#------------------- Table Material Description -------------------
h = A4
x_list = [50,120, 420, 480, 542.2]
y_list = [115, 565, 580]
canvas.grid(x_list, y_list)
canvas.drawString(64, 569, "Cantidad")
canvas.drawString(250,569, "Concepto")
canvas.drawString(435, 569, "Precio")
canvas.drawString(493, 569, "Importe")

canvas.rotate(90)
canvas.drawString(119, -45, "Andy Murray 929292929W")
canvas.save()





