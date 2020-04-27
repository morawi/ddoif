# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 01:16:08 2020

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


import yaml

with open(r'C:/MyPrograms/ddoif/ddoif.yaml') as file:
    # The FullLoader parameter handles the conversion from YAML
    # scalar values to Python the dictionary format
    ddoif_dict = yaml.load(file, Loader=yaml.FullLoader)
    file.close()

print(ddoif_dict['clothing']['skirt']['type'])


