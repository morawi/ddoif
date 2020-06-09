# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 23:20:19 2020

@author: malrawi


"""


from ddoif_utils import yaml_to_xml, read_yaml_as_dict, yaml_to_json

path= 'C:/MyPrograms/ddoif/'
yaml_fname = 'ddoif_dictionary.yaml'
xml_fname = 'ddoif_dictionary.xml' 
json_fname= 'ddoif_dictionary.json'

yaml_to_json(yaml_fname, json_fname)

yaml_to_xml(yaml_fname, xml_fname, ids=False)

x = read_yaml_as_dict(path+yaml_fname)
# print(yaml_dict)



