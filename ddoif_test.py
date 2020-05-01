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


"""


from ddoif_utils import read_yaml_as_dict, save_dict_to_xml

save_as_xml=True

path= 'C:/MyPrograms/ddoif/'
yaml_fname = 'ddoif.yaml'
xml_fname = 'ddoif.xml' 

yaml_dict = read_yaml_as_dict(path+yaml_fname)
print(yaml_dict)
if save_as_xml:
    save_dict_to_xml(path+xml_fname, yaml_dict)



