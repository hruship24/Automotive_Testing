import xml.etree.ElementTree as ET
import os


def write_xml(filename):
    # create root element
    root = ET.Element("data")

    person1 = ET.SubElement(root, 'person')
    name1 = ET.SubElement(person1, 'name')
    name1.text = 'Hrushi pawar'
    age1 = ET.SubElement(person1, 'age')
    age1.text = '24'

    person2 = ET.SubElement(root, 'person')
    name2 = ET.SubElement(person2, 'name')
    name2.text = 'abc xyz'
    age2 = ET.SubElement(person2, 'age')
    age2.text = '23'

    # create XML tree
    tree = ET.ElementTree(root)

    # write xml data to file
    tree.write(filename)


def read_xml(filename):
    # parse xml tree
    tree = ET.parse(filename)
    root = tree.getroot()

    # extract data from xml
    for person in root.findall("person"):
        name = person.find("name").text
        age = person.find("age").text
        print(f"Name: {name}, Age: {age}")


def delete_xml(filename):
    if os.path.exists(filename):
        os.remove(filename)
        print(f"{filename} deleted successfully")
    else:
        print(f"{filename} does not exist")


if __name__ == "__main__":
    filename = "data.xml"
    write_xml(filename)
    print("Data read from xml file : ")
    read_xml(filename)
    # delete_xml(filename)