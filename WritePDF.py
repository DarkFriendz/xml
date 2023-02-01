#Assets
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from lista import lista

def mm2p(milimetros):
    return milimetros/0.352777

tamanho = [A4[0]-mm2p(10), A4[1]-mm2p(5)]

#write
cnv = canvas.Canvas("Template.pdf", pagesize=A4)
cnv.setFontSize(9)

#Info
cnv.rect(tamanho[0], tamanho[1], -200, -60)
cnv.rect(tamanho[0]/18, tamanho[1], 330, -60)

#Dados Tomador
cnv.rect(tamanho[0]/18, tamanho[1]/1.10, 535, -60)

#Table Serviços
cnv.rect(tamanho[0]/18, tamanho[1]/1.22, 535, -20)

#Table
cnv.drawString(tamanho[0]/18, tamanho[1]/1.214, "Serviços")
cnv.line(tamanho[0]/18, tamanho[1]/1.22, tamanho[0]/18, tamanho[1]/2.2)

#Table ID
cnv.line(tamanho[0]/6, tamanho[1]/1.22, tamanho[0]/6, tamanho[1]/2.2)
cnv.drawString(tamanho[0]/11, tamanho[1]/1.245, "Cod.")

#Table Description
cnv.line(tamanho[0]/2.4, tamanho[1]/1.22, tamanho[0]/2.4, tamanho[1]/2.2)
cnv.drawString(tamanho[0]/4.6, tamanho[1]/1.245, "Descrição do Seviço")

#Table CST
cnv.line(tamanho[0]/2.1, tamanho[1]/1.22, tamanho[0]/2.1, tamanho[1]/2.2)
cnv.drawString(tamanho[0]/2.34, tamanho[1]/1.245, "CST.")

#Table Aliq
cnv.line(tamanho[0]/1.87, tamanho[1]/1.22, tamanho[0]/1.87, tamanho[1]/2.2)
cnv.drawString(tamanho[0]/2.04, tamanho[1]/1.245, "Aliq.")

#Table Valor Unitario
cnv.line(tamanho[0]/1.35, tamanho[1]/1.22, tamanho[0]/1.35, tamanho[1]/2.2)
cnv.drawString(tamanho[0]/1.7, tamanho[1]/1.245, "Valor unitário")

#Table Quantidade
cnv.line(tamanho[0]/1.25, tamanho[1]/1.22, tamanho[0]/1.25, tamanho[1]/2.2)
cnv.drawString(tamanho[0]/1.33, tamanho[1]/1.245, "Qnt.")

#Table Valor Total
cnv.line(tamanho[0], tamanho[1]/1.22, tamanho[0], tamanho[1]/2.2)
cnv.drawString(tamanho[0]/1.16, tamanho[1]/1.245, "Valor Total")

#Table Lines
for num in range(0, len(lista)):
    #Table ID
    cnv.line(tamanho[0]/6, tamanho[1]/(1.29+(0.035*num)), tamanho[0]/6, tamanho[1]/(1.29+(0.035*num)))
    cnv.drawString(tamanho[0]/16.9, tamanho[1]/(1.28+(0.035*num)), f"{lista[num]['id']}")

    #Table Description
    cnv.line(tamanho[0]/2.4, tamanho[1]/(1.29+(0.035*num)), tamanho[0]/2.4, tamanho[1]/(1.29+(0.035*num)))
    cnv.setFontSize(6)
    cnv.drawString(tamanho[0]/5.8, tamanho[1]/(1.28+(0.035*num)), f"{lista[num]['description']}")
    cnv.setFontSize(9)

    #Table CST
    cnv.line(tamanho[0]/2.1, tamanho[1]/(1.29+(0.035*num)), tamanho[0]/2.1, tamanho[1]/(1.29+(0.035*num)))
    cnv.drawString(tamanho[0]/2.26, tamanho[1]/(1.28+(0.035*num)), f"{lista[num]['cst']}")

    #Table Aliq
    cnv.line(tamanho[0]/1.87, tamanho[1]/(1.29+(0.035*num)), tamanho[0]/1.87, tamanho[1]/(1.29+(0.035*num)))
    cnv.drawString(tamanho[0]/2.04, tamanho[1]/(1.28+(0.035*num)), f"{lista[num]['aliq']}0")

    #Table Valor Unitario
    cnv.line(tamanho[0]/1.35, tamanho[1]/(1.29+(0.035*num)), tamanho[0]/1.35, tamanho[1]/(1.29+(0.035*num)))
    cnv.drawString(tamanho[0]/1.85, tamanho[1]/(1.28+(0.035*num)), f"R$ {lista[num]['vu']}0")

    #Table Quantidade
    cnv.line(tamanho[0]/1.25, tamanho[1]/(1.29+(0.035*num)), tamanho[0]/1.25, tamanho[1]/(1.29+(0.035*num)))
    cnv.drawString(tamanho[0]/1.34, tamanho[1]/(1.28+(0.035*num)), f"{lista[num]['amount']}")

    #Table Valor Total
    cnv.line(tamanho[0], tamanho[1]/(1.29+(0.035*num)), tamanho[0], tamanho[1]/(1.29+(0.035*num)))
    cnv.drawString(tamanho[0]/1.24, tamanho[1]/(1.28+(0.035*num)), f"R$ {lista[num]['vt']}0")
    cnv.line(tamanho[0]/18, tamanho[1]/(1.29+(0.035*num)), tamanho[0], tamanho[1]/(1.29+(0.035*num)))
    

#Table End
cnv.line(tamanho[0]/18, tamanho[1]/2.2, tamanho[0], tamanho[1]/2.2)

#Outros Impostos
cnv.rect(tamanho[0]/18, tamanho[1]/2.28, 535, -100)

#Valor
cnv.rect(tamanho[0]/18, tamanho[1]/3.3, 535, -30)

#Dados Adicionais
cnv.rect(tamanho[0]/18, tamanho[1]/4, 535, -100)

#Expecificações
cnv.rect(tamanho[0]/18, tamanho[1]/8.8, 535, -80)

cnv.save()