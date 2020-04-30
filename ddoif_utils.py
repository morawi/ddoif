# -*- coding: utf-8 -*-
"""

Created on Tue Apr 28 23:15:17 2020

@author: malrawi


"""

import dicttoxml
import yaml
import json

def save_dict_to_xml(fname, yaml_dict):    
    xml_obj = dicttoxml.dicttoxml(yaml_dict)
    with open("myxmlfile.xml", "wb") as fp:
        fp.write(xml_obj)
    
def read_yaml_as_dict(fname):
    with open(fname) as fp:
        # The FullLoader parameter handles the conversion from YAML
        # scalar values to Python the dictionary format
        ddoif_dict = yaml.load(fp, Loader=yaml.FullLoader)
        
    return ddoif_dict

    
def yaml_to_xml(yaml_fname, xml_fname):
    yaml_dict = read_yaml_as_dict(yaml_fname)
    save_dict_to_xml(xml_fname, yaml_dict)


def yaml_to_json(yaml_fname, json_fname):
    yaml_dict = read_yaml_as_dict(yaml_fname)
    with open(json_fname, 'w') as fp:
        json.dump(yaml_dict, fp)

      

    

        
        