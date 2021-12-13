import xml.dom.minidom as md

def xml_parse():
    path="breakfast_menu.xml"
    file1=md.parse(path)
    name = file1.getElementsByTagName("breakfast_menu")[0]
    print("The value of a tag before changing: ", file1.firstChild.tagName)
    name.tagName="dinner_menu"
    path2="dinner_menu.xml"
    file1.writexml(open(path2, "w"))
    file2 = md.parse(path2)
    print("The value of a tag after changing: ", file2.firstChild.tagName)

xml_parse()