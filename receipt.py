# -*- coding: utf-8 -*-
import locale 
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

class Receipt(object):

      def __init__(self, num_receipt, locality, amount, date_issue, maturity,
                   concept, payable, office, account_number, name_shipper, address,
                   population):

            self.num_receipt = num_receipt
            self.locality = locality
            self.amount = amount
            self.date_issue = date_issue
            self.maturity = maturity
            self.concept = concept
            self.payable = payable
            self.office = office
            self.account_number = account_number
            self.name_shipper = name_shipper
            self.address = address
            self.population = population

      def generate_pdf(self):

            locale.setlocale(locale.LC_ALL, '')
            c = canvas.Canvas("Recibo_" + str(self.num_receipt) + ".pdf", pagesize=A4)
            c.setLineWidth(.2)
            c.setFont('Helvetica', 9)
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

            c.setFont('Helvetica', 9)
            
            c.drawCentredString(140.428, 805.168, self.num_receipt)
            c.drawCentredString(285.714, 805.168, self.locality)
            c.drawCentredString(450.857, 805.168, self.amount)
            
            c.drawRightString(285.714, 776.72, self.date_issue)
            c.drawRightString(471.428, 776.72, self.maturity)
            
            c.drawRightString(457.143, 729.77, self.concept)
            
            c.drawString(107.143, 688, self.payable)
            c.drawRightString(314.285, 688, self.office)
            c.drawRightString(458, 688, self.account_number)
            
            c.drawString(107.143, 648.68, self.name_shipper)
            c.drawString(107.143, 634.46, self.address)
            c.drawString(107.143, 620.545, self.population)

            c.drawString(387.428, 640.46, "Andy Murray")
            c.save()




