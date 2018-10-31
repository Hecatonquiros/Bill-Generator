# -*- coding: utf-8 -*-
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

canvas = canvas.Canvas("form.pdf", pagesize = A4)
canvas.setLineWidth(.3)


numBill = 8888
fecha = "31/10/2018"
cif_nif = "B-123456789"

#------------------- Logo Information ----------------------------
canvas.drawImage("../Bill-Generator/logocompleto.png", 40, 710, width = 200, height = 100)
altura = 710

canvas.setFont('Helvetica', 8)

#canvas.drawString(40, altura, "")
#canvas.drawString(40, altura-10, "")
#canvas.drawString(40, altura-20, "")

#canvas.setFont('Helvetica', 7)
#canvas.drawString(40, altura -40, "")
#canvas.drawString(40, altura -50, "")
#canvas.drawString(40, altura -60, "")
#canvas.drawString(40, altura -70, "")
#canvas.drawString(40, altura -80, "")

#------------------- Rectangle Info Client Adress ----------------- 
canvas.rect(300, 660,230, 100)

#------------------- Rectangles Info Bill + NIF -------------------
canvas.rect(50, 590, 147.4, 30)
canvas.rect(222.4, 590, 147.4, 30)
canvas.rect(394.8, 590, 147.4, 30)
canvas.setFont('Helvetica', 10)
canvas.drawString(51,610, "Nº Factura")

#------------------- Rectangles Total Bill ------------------------
canvas.rect(50, 70, 147.4, 30)
canvas.rect(222.4, 70, 147.4, 30)
canvas.rect(394.8, 70, 147.4,30)

#------------------- Rectangles Way to pay ------------------------
canvas.rect(50, 30, 492.2, 30)

#------------------- Table Material Description -------------------
h = A4
x_list = [50,120, 430, 480, 542.2]
y_list = [115, 565, 580]
canvas.grid(x_list, y_list)

canvas.save()



