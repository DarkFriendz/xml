#Assets
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from files.lista import lista

def mm2p(milimetros):
    return milimetros/0.352777

tamanho = [A4[0]-mm2p(10), A4[1]-mm2p(10)]

#write - Escrever
cnv = canvas.Canvas("Template.pdf", pagesize=A4)

#Your Company - Sua Empresa
cnv.setFontSize(6)
cnv.drawString(mm2p(10), tamanho[1]+mm2p(1), "Empresa")
cnv.rect(mm2p(10), tamanho[1], (tamanho[0]-mm2p(92)), -40)
cnv.rect(tamanho[0], tamanho[1], -(tamanho[0]-mm2p(120)), -40)

#Requested company - Empresa solicitada
cnv.setFontSize(6)
cnv.drawString(mm2p(10), tamanho[1]-mm2p(17), "Dados Tomador")
cnv.line(mm2p(10), tamanho[1]-mm2p(24), tamanho[0], tamanho[1]-mm2p(24))
cnv.line(tamanho[0]-mm2p(25), tamanho[1]-mm2p(18), tamanho[0]-mm2p(25), tamanho[1]-mm2p(35.8))

#Name/Corporate Name - Nome/Razão Social
cnv.setFontSize(5)
cnv.drawString(mm2p(12), tamanho[1]-mm2p(20), "Nome/Razão Social")

#CFPS
cnv.drawString(tamanho[0]-mm2p(23), tamanho[1]-mm2p(20), "CFPS")

cnv.line(tamanho[0]-mm2p(65), tamanho[1]-mm2p(24), tamanho[0]-mm2p(65), tamanho[1]-mm2p(35.8))

#Address - Endereço
cnv.drawString(mm2p(12), tamanho[1]-mm2p(26), "Endereço")

#Neighborhood/District - Bairro/Distrito
cnv.drawString(tamanho[0]-mm2p(63), tamanho[1]-mm2p(26), "Bairro/Distrito")

#CEP
cnv.drawString(tamanho[0]-mm2p(23), tamanho[1]-mm2p(26), "CEP")

cnv.line(tamanho[0]-mm2p(75), tamanho[1]-mm2p(30), tamanho[0]-mm2p(75), tamanho[1]-mm2p(35.8))

#County - Município
cnv.drawString(mm2p(12), tamanho[1]-mm2p(32), "Município")

#UF
cnv.drawString(tamanho[0]-mm2p(73), tamanho[1]-mm2p(32), "UF")

#CNPJ/CPF/Others - CNPJ/CPF/Outros
cnv.drawString(tamanho[0]-mm2p(63), tamanho[1]-mm2p(32), "CNPJ/CPF/Outros")

#CMC
cnv.drawString(tamanho[0]-mm2p(23), tamanho[1]-mm2p(32), "CMC")

cnv.line(mm2p(10), tamanho[1]-mm2p(30), tamanho[0], tamanho[1]-mm2p(30))
cnv.setFontSize(9)
cnv.rect(mm2p(10), tamanho[1]-mm2p(18), tamanho[0]-mm2p(10), -50)

#Services - Serviços
cnv.setFontSize(6)
cnv.drawString(mm2p(10), tamanho[1]-mm2p(39), "Serviços")
cnv.line(mm2p(30), tamanho[1]-mm2p(40), mm2p(30), tamanho[1]-mm2p(45.1))
cnv.setFontSize(7)
cnv.drawString(mm2p(12), tamanho[1]-mm2p(43.5), "Cod. Atividade")
cnv.line(mm2p(90), tamanho[1]-mm2p(40), mm2p(90), tamanho[1]-mm2p(45.1))
cnv.drawString(mm2p(33), tamanho[1]-mm2p(43.5), "Descrição do Serviço")
cnv.line(mm2p(101), tamanho[1]-mm2p(40), mm2p(101), tamanho[1]-mm2p(45.1))
cnv.drawString(mm2p(93), tamanho[1]-mm2p(43.5), "CST")
cnv.line(mm2p(111), tamanho[1]-mm2p(40), mm2p(111), tamanho[1]-mm2p(45.1))
cnv.drawString(mm2p(104), tamanho[1]-mm2p(43.5), "Aliq")
cnv.line(mm2p(111), tamanho[1]-mm2p(40), mm2p(111), tamanho[1]-mm2p(45.1))
cnv.drawString(mm2p(112), tamanho[1]-mm2p(43.5), "Valor Unitário")
cnv.line(mm2p(141), tamanho[1]-mm2p(40), mm2p(141), tamanho[1]-mm2p(45.1))
cnv.drawString(mm2p(143), tamanho[1]-mm2p(43.5), "Unidade")
cnv.line(mm2p(155), tamanho[1]-mm2p(40), mm2p(155), tamanho[1]-mm2p(45.1))
cnv.drawString(mm2p(157), tamanho[1]-mm2p(43.5), "Valor Total")

#Table

cnv.rect(mm2p(10), tamanho[1]-mm2p(40), tamanho[0]-mm2p(10), -15)
cnv.setFontSize(6)
cnv.line(mm2p(10), tamanho[1]-mm2p(45), mm2p(10), tamanho[1]-mm2p(160))
cnv.line(tamanho[0], tamanho[1]-mm2p(45), tamanho[0], tamanho[1]-mm2p(160))
cnv.setFontSize(9)

#End Line of Services - linha final dos serviços
cnv.line(mm2p(10), tamanho[1]-mm2p(160), tamanho[0], tamanho[1]-mm2p(160))

#Summary - Resumo
cnv.setFontSize(6)
cnv.drawString(mm2p(10), tamanho[1]-mm2p(163), "Resumo")
cnv.rect(mm2p(10), tamanho[1]-mm2p(164), tamanho[0]-mm2p(10), -20)
cnv.setFontSize(5)
cnv.drawString(mm2p(12), tamanho[1]-mm2p(166), "Base Cálculo ISSQN")
cnv.line(mm2p(48), tamanho[1]-mm2p(164), mm2p(48), tamanho[1]-mm2p(171))
cnv.drawString(mm2p(50), tamanho[1]-mm2p(166), "Valor ISSQN")
cnv.line(mm2p(86), tamanho[1]-mm2p(164), mm2p(86), tamanho[1]-mm2p(171))
cnv.drawString(mm2p(88), tamanho[1]-mm2p(166), "Base Cálculo ISSQN Subst.")
cnv.line(mm2p(124), tamanho[1]-mm2p(164), mm2p(124), tamanho[1]-mm2p(171))
cnv.drawString(mm2p(126), tamanho[1]-mm2p(166), "Valor ISSQN Subst.")
cnv.line(mm2p(162), tamanho[1]-mm2p(164), mm2p(162), tamanho[1]-mm2p(171))
cnv.drawString(mm2p(164), tamanho[1]-mm2p(166), "Descontos")

cnv.setFontSize(9)

#Other Taxes - Outros Impostos
cnv.setFontSize(6)
cnv.drawString(mm2p(10), tamanho[1]-mm2p(174), "Outros Impostos")
cnv.rect(mm2p(10), tamanho[1]-mm2p(175), tamanho[0]-mm2p(10), -80)
cnv.setFontSize(9)

#Valor Total - Amount

cnv.setFontSize(6)
cnv.drawString(mm2p(10), tamanho[1]-mm2p(206), "Valor Total")
cnv.rect(mm2p(10), tamanho[1]-mm2p(207), tamanho[0]-mm2p(10), -20)
cnv.setFontSize(5)
cnv.drawString(mm2p(12), tamanho[1]-mm2p(209), "Valor Total dos Serviços")
cnv.line(tamanho[0]/2+mm2p(2), tamanho[1]-mm2p(207), tamanho[0]/2+mm2p(2), tamanho[1]-mm2p(214))
cnv.drawString(tamanho[0]/2+mm2p(4), tamanho[1]-mm2p(209), "Valor Total da Nota")

#Additional Data - Dados Adcionais

cnv.setFontSize(6)
cnv.drawString(mm2p(10), tamanho[1]-mm2p(217), "Dados Adcionais")
cnv.rect(mm2p(10), tamanho[1]-mm2p(218), tamanho[0]-mm2p(10), -80)
cnv.setFontSize(9)

#Final Data - Dados Final
cnv.setFontSize(6)
cnv.drawString(mm2p(10), tamanho[1]-mm2p(250), "Dados Finais")
cnv.rect(mm2p(10), tamanho[1]-mm2p(251), tamanho[0]-mm2p(10), -80)

'''
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

VT = 0.0

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
  
    VT = VT+lista[num]['vt']

#Table End
cnv.line(tamanho[0]/18, tamanho[1]/2.2, tamanho[0], tamanho[1]/2.2)

#Outros Impostos
cnv.rect(tamanho[0]/18, tamanho[1]/2.28, 535, -100)

#Valor
cnv.rect(tamanho[0]/18, tamanho[1]/3.3, 535, -30)
cnv.line(tamanho[0]/2, tamanho[1]/3.3, tamanho[0]/2, tamanho[1]/3.75)
cnv.drawString(tamanho[0]/1.95, tamanho[1]/3.26, f"Valor Total")
cnv.drawString(tamanho[0]/1.95, tamanho[1]/3.55, f"R$ {VT}0")

#Dados Adicionais
cnv.rect(tamanho[0]/18, tamanho[1]/4, 535, -100)

#Expecificações
cnv.rect(tamanho[0]/18, tamanho[1]/8.8, 535, -80)'''

cnv.save()