# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 23:20:19 2020

@author: malrawi



1- 
YAML Multi Documents
YAML format allows multiple documents to be embedded in a single file. They only have to be separated with a line containing triple-dash separator ---.

YAMLJSON
document: this is document 1
---
document: this is document 2

for details see https://gettaurus.org/docs/YAMLTutorial/


2- To check the correctness of the ymal file use:
https://github.com/adrienverge/yamllint

3- https://www.xmlvalidation.com/


https://stackabuse.com/reading-and-writing-xml-files-in-python/

import xml.etree.ElementTree as ET

# create the file structure
data = ET.Element('data')
items = ET.SubElement(data, 'items')
item1 = ET.SubElement(items, 'item')
item2 = ET.SubElement(items, 'item')
item1.set('name','item1')
item2.set('name','item2')
item1.text = 'item1abc'
item2.text = 'item2abc'

# create a new XML file with the results
mydata = ET.tostring(data)
myfile = open("items2.xml", "w")
myfile.write(mydata)

https://stackoverflow.com/questions/52499959/read-modify-the-xml-save-it-in-a-new-xml-using-python


"""


from ddoif_utils import read_yaml_as_dict, yaml_to_xml

save_as_xml=True

path= 'C:/MyPrograms/ddoif/'
yaml_fname = 'ddoif.yaml'
xml_fname = 'ddoif.xml' 


yaml_to_xml(yaml_fname, xml_fname, ids=False)

# yaml_dict = read_yaml_as_dict(path+yaml_fname)
# print(yaml_dict)
# yaml_to_xml(yaml_fname, xml_fname)






# # Output plain YAML
# with open("ddoif.yaml") as f:
#     root = xmlplain.obj_from_yaml(f)
#     # xmlplain.obj_to_yaml(root, f)
# with open("example-1.xml", 'w') as outf: 
#     xmlplain.xml_to_obj(root)
    


# # Read to plain object
# 
#   root = xmlplain.xml_to_obj(inf, strip_space=True, fold_dict=True)

