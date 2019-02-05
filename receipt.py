# -*- coding: utf-8 -*-
import locale 
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

class Recibo(object):

      def __init__(self, num_receipt, locality, amount, date_issue, maturity,
                   description, payable, office, account_number, address,
                   population, name_shipper):

            self.num_receipt = num_receipt
            self.locality = locality
            self.amount = amount
            self.date_issue = date_issue
            self.maturity = maturity
            self.description = description
            self.payable = payable
            self.office = office
            self.account_number = account_number
            self.name_shipper = name_shipper
            self.address = address
            self.population = population

      def generate_pdf(self):

            locale.setlocale(locale.LC_ALL, '')
            c = canvas.Canvas("Recibo.pdf", pagesize=A4)
            c.setLineWidth(.2)
            c.setFont('Helvetica', 9)

            c = canvas.Canvas("Recibo.pdf")
            c.setLineWidth(.2)
            c.rect(102.86, 771.026, 404.28, 56.904)
            c.line(102.86, 799.478, 507.14, 799.478)
            c.line(178.57, 827.93, 178.57, 799.478)
            c.line(397.143, 827.93, 397.143, 799.478)
            c.line(305.714, 799.478, 305.714, 771.026)
            
            c.rect(102.86, 719.53, 404.28, 44.384)
            c.rect(102.86, 682.83, 404.28, 28.45)
            c.rect(102.86, 611.7, 257.14, 65.153)
            
            c.setFont('Helvetica', 6)
            c.drawString(110, 819.394, "RECIBO NUMERO")
            c.drawString(184.285, 819.394, "LOCALIDAD DE EXPEDICION")
            c.drawString(402.857, 819.394, "IMPORTE")
            
            c.drawString(108.857 , 790.943 , "FECHA DE EXPEDICION")
            c.drawString(311.428 , 790.943, "VENCIMIENTO")
            
            
            c.drawString(111.43, 754.111 , "CONCEPTO") 
            
            
            c.drawString(110, 702.744, "PAGADERO EN (CAJA O BANCO)")
            c.drawString(294.286, 702.744, "OFICINA")
            c.drawString(397.143, 702.744, "CLAVE O Nº CUENTA")
            
            
            c.drawString(110, 667.18, "NOMBRE Y DOMICILIO DEL PAGADOR")
            
            c.drawString(385.714, 672.7, "FIRMA Y NOMBRE DEL EXPEDIDOR")
            c.rect(102.86, 771.026, 404.28, 56.904)
            
            c.line(0, 603.165, 600, 603.165)
            
            c.save()



