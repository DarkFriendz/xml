#Assets
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from files.lista import Empresa
from datetime import datetime

def mm2p(milimetros):
    return milimetros/0.352777

tamanho = [A4[0]-mm2p(10), A4[1]-mm2p(10)]

data = datetime.now()
Templatedata = datetime.strftime(data, "%d%m%Y%H%M%S")
data = datetime.strftime(data, "%d/%m/%Y - %H:%M:%S")

CV = "PMWOMG4AW"

countLines = 1

#list
for Tables in Empresa['Lista']:
    if countLines >= 30:
        PDFS = PDFS+1
        countLines=1
    countLines = countLines+1

PDFS = countLines

for PDF in PDFS:
    #write - Escrever
    cnv = canvas.Canvas(f"Template{PDF}.pdf", pagesize=A4)

    #Your Company - Sua Empresa
    cnv.setFontSize(6)
    cnv.drawString(mm2p(10), tamanho[1]+mm2p(1), "Empresa")
    cnv.rect(mm2p(10), tamanho[1], (tamanho[0]-mm2p(92)), -40)

    #Logo Company - logo da Empresa
    cnv.drawImage("imgs/saude.png", mm2p(10)+mm2p(0.2), tamanho[1]-mm2p(0.2), 120, -38.8)

    #Your Companie Info - Informações da sua empresa
    cnv.setFontSize(8)
    cnv.drawString(mm2p(55), tamanho[1]-mm2p(3.2), "Empresa Segurança da Saude LTDA")
    cnv.setFontSize(6)
    cnv.drawString(mm2p(55), tamanho[1]-mm2p(6.5), "Rua XXXXX XXXXXX XXX, 000 - (00) 0000-0000")
    cnv.drawString(mm2p(55), tamanho[1]-mm2p(9.5), "São José - SC - XXXXXXXXXXXXXX - 00000-000")
    cnv.drawString(mm2p(55), tamanho[1]-mm2p(12.5), "CNPJ: 00.000.000/0000-00 CMC: 0000000")

    #NF Info - NF Informações
    cnv.rect(tamanho[0], tamanho[1], -(tamanho[0]-mm2p(120)), -40)
    cnv.setFontSize(8)
    cnv.drawString(mm2p(122), tamanho[1]-mm2p(3.2), "Nota Fiscal Eletrônica de Prestação de Serviços")
    cnv.drawString(mm2p(122), tamanho[1]-mm2p(6.2), "Número: 10000")
    cnv.drawString(mm2p(122), tamanho[1]-mm2p(9.2), f"Emissão: {data}")
    cnv.drawString(mm2p(122), tamanho[1]-mm2p(12.2), f"Código de Verificação: {CV}")

    #Requested company - Empresa solicitada
    cnv.setFontSize(6)
    cnv.drawString(mm2p(10), tamanho[1]-mm2p(17), "Dados Tomador")
    cnv.rect(mm2p(10), tamanho[1]-mm2p(18), tamanho[0]-mm2p(10), -50)
    cnv.line(mm2p(10), tamanho[1]-mm2p(24), tamanho[0], tamanho[1]-mm2p(24))
    cnv.line(tamanho[0]-mm2p(25), tamanho[1]-mm2p(18), tamanho[0]-mm2p(25), tamanho[1]-mm2p(35.8))
    cnv.line(tamanho[0]-mm2p(65), tamanho[1]-mm2p(24), tamanho[0]-mm2p(65), tamanho[1]-mm2p(35.8))
    cnv.line(tamanho[0]-mm2p(75), tamanho[1]-mm2p(30), tamanho[0]-mm2p(75), tamanho[1]-mm2p(35.8))
    cnv.line(mm2p(10), tamanho[1]-mm2p(30), tamanho[0], tamanho[1]-mm2p(30))

    #Name/Corporate Name - Nome/Razão Social
    cnv.setFontSize(5)
    cnv.drawString(mm2p(12), tamanho[1]-mm2p(20), "Nome/Razão Social")
    cnv.setFontSize(8)
    cnv.drawString(mm2p(13), tamanho[1]-mm2p(22.8), f"{Empresa['name']}")

    #CFPS
    cnv.setFontSize(5)
    cnv.drawString(tamanho[0]-mm2p(23), tamanho[1]-mm2p(20), "CFPS")
    cnv.setFontSize(8)
    cnv.drawString(tamanho[0]-mm2p(22), tamanho[1]-mm2p(22.8), f"{Empresa['CFPS']}")

    #Address - Endereço
    cnv.setFontSize(5)
    cnv.drawString(mm2p(12), tamanho[1]-mm2p(26), "Endereço")
    cnv.setFontSize(8)
    cnv.drawString(mm2p(13), tamanho[1]-mm2p(28.8), f"{Empresa['endereco']}")

    #Neighborhood/District - Bairro/Distrito
    cnv.setFontSize(5)
    cnv.drawString(tamanho[0]-mm2p(63), tamanho[1]-mm2p(26), "Bairro/Distrito")
    cnv.setFontSize(8)
    cnv.drawString(tamanho[0]-mm2p(62), tamanho[1]-mm2p(28.8), f"{Empresa['bairro']}")

    #CEP
    cnv.setFontSize(5)
    cnv.drawString(tamanho[0]-mm2p(23), tamanho[1]-mm2p(26), "CEP")
    cnv.setFontSize(8)
    cnv.drawString(tamanho[0]-mm2p(22), tamanho[1]-mm2p(28.8), f"{Empresa['CEP']}")

    #County - Município
    cnv.setFontSize(5)
    cnv.drawString(mm2p(12), tamanho[1]-mm2p(32), "Município")
    cnv.setFontSize(8)
    cnv.drawString(mm2p(13), tamanho[1]-mm2p(34.8), f"{Empresa['municipio']}")

    #UF
    cnv.setFontSize(5)
    cnv.drawString(tamanho[0]-mm2p(73), tamanho[1]-mm2p(32), "UF")
    cnv.setFontSize(8)
    cnv.drawString(tamanho[0]-mm2p(72), tamanho[1]-mm2p(34.8), f"{Empresa['UF']}")

    #CNPJ/CPF/Others - CNPJ/CPF/Outros
    cnv.setFontSize(5)
    cnv.drawString(tamanho[0]-mm2p(63), tamanho[1]-mm2p(32), "CNPJ/CPF/Outros")
    cnv.setFontSize(8)
    cnv.drawString(tamanho[0]-mm2p(62), tamanho[1]-mm2p(34.8), f"{Empresa['CNPJ/CPF']}")

    #CMC
    cnv.setFontSize(5)
    cnv.drawString(tamanho[0]-mm2p(23), tamanho[1]-mm2p(32), "CMC")
    cnv.setFontSize(8)
    cnv.drawString(tamanho[0]-mm2p(22), tamanho[1]-mm2p(34.8), f"{Empresa['CMC']}")

    #Services - Serviços
    cnv.setFontSize(6)
    cnv.drawString(mm2p(10), tamanho[1]-mm2p(39), "Serviços")
    cnv.rect(mm2p(10), tamanho[1]-mm2p(40), tamanho[0]-mm2p(10), -15)
    cnv.line(mm2p(30), tamanho[1]-mm2p(40), mm2p(30), tamanho[1]-mm2p(159.9))
    cnv.setFontSize(7)
    cnv.drawString(mm2p(12), tamanho[1]-mm2p(43.5), "Cod. Atividade")
    cnv.line(mm2p(90), tamanho[1]-mm2p(40), mm2p(90), tamanho[1]-mm2p(159.9))
    cnv.drawString(mm2p(33), tamanho[1]-mm2p(43.5), "Descrição do Serviço")
    cnv.line(mm2p(101), tamanho[1]-mm2p(40), mm2p(101), tamanho[1]-mm2p(159.9))
    cnv.drawString(mm2p(93), tamanho[1]-mm2p(43.5), "CST")
    cnv.line(mm2p(111), tamanho[1]-mm2p(40), mm2p(111), tamanho[1]-mm2p(159.9))
    cnv.drawString(mm2p(104), tamanho[1]-mm2p(43.5), "Aliq")
    cnv.line(mm2p(111), tamanho[1]-mm2p(40), mm2p(111), tamanho[1]-mm2p(159.9))
    cnv.drawString(mm2p(112), tamanho[1]-mm2p(43.5), "Valor Unitário")
    cnv.line(mm2p(141), tamanho[1]-mm2p(40), mm2p(141), tamanho[1]-mm2p(159.9))
    cnv.drawString(mm2p(143), tamanho[1]-mm2p(43.5), "Unidade")
    cnv.line(mm2p(155), tamanho[1]-mm2p(40), mm2p(155), tamanho[1]-mm2p(159.9))
    cnv.drawString(mm2p(157), tamanho[1]-mm2p(43.5), "Valor Total")

    #Table

        

    cnv.line(mm2p(10), tamanho[1]-mm2p(45), mm2p(10), tamanho[1]-mm2p(160))
    cnv.line(tamanho[0], tamanho[1]-mm2p(45), tamanho[0], tamanho[1]-mm2p(160))

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
    