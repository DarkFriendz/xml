#Assets
import xml.etree.ElementTree as ET

xml_doc = ET.Element('root')

product = ET.SubElement(xml_doc, 'product')
ET.SubElement(product, 'item', id='product-id', price="35.00", currency='$').text = 'Seguro de vida'
ET.SubElement(product, 'brand', model="daiojdau9hdauwrghayui").text = "Plano 1"

tree = ET.ElementTree(xml_doc)
tree.write('files/template.xml', encoding='utf-8', xml_declaration=True)