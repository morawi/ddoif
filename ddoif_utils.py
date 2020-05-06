# -*- coding: utf-8 -*-
"""

Created on Tue Apr 28 23:15:17 2020

@author: malrawi



"""

import dicttoxml
# import yaml
import ruamel.yaml
import json

    
def read_yaml_as_dict(fname):
    with open(fname) as fp:
        # The FullLoader parameter handles the conversion from YAML
        # scalar values to Python the dictionary format
        # ddoif_dict = yaml.load(fp, Loader=yaml.FullLoader) 
        # ddoif_dict = yaml.safe_load(fp)

        yaml = ruamel.yaml.YAML(typ='safe') # this is claimed to be the safest way to load yaml  https://stackoverflow.com/questions/50846431/converting-a-yaml-file-to-python-json-object
        ddoif_dict = yaml.load(fp)
    return ddoif_dict

    
def yaml_to_xml(yaml_fname, xml_fname, ids=False):
    yaml_dict = read_yaml_as_dict(yaml_fname)    
    xml_obj = dicttoxml.dicttoxml(yaml_dict, custom_root='ddoif', attr_type=False, ids=ids)
    print('Converting to xml using dicttoxml version -- ', dicttoxml.__version__)
    # print_xml(xml_obj)
    
    with open(xml_fname, "wb") as fp:
        fp.write(xml_obj)
    

def yaml_to_json(yaml_fname, json_fname):
    yaml_dict = read_yaml_as_dict(yaml_fname)
    with open(json_fname, 'w') as fp:
        json.dump(yaml_dict, fp, indent=True, )

def print_xml(xml_obj): # xml_obj = dicttoxml.dicttoxml(yaml_dict, custom_root='ddoif', attr_type=False)
    from xml.dom.minidom import parseString
    dom = parseString(xml_obj)
    print(dom.toprettyxml())
    
      

    

        
        