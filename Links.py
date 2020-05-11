# -*- coding: utf-8 -*-
"""
Created on Tue May  5 14:15:25 2020

@author: malrawi

Links




"""

# JSON ot svg  https://vanya.jp.net/vtree/
# https://stackoverflow.com/questions/50846431/converting-a-yaml-file-to-python-json-object
# https://onlineyamltools.com/convert-yaml-to-json
# https://onlineyamltools.com/convert-yaml-to-xml
# http://yaml-online-parser.appspot.com/
# https://jsonformatter.org/json-parser
# yaml validator: http://www.yamllint.com/
# http://www.ic.gc.ca/eic/site/oca-bc.nsf/eng/ca02009.html#Washing 

# https://pypi.org/project/dicttoxml/
# https://rollout.io/blog/yaml-tutorial-everything-you-need-get-started/

''' 
1- YAML Multi Documents
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



'''



# YAML tags and Python types, and more in https://pyyaml.org/wiki/PyYAMLDocumentation
# The following table describes how nodes with different tags are converted to Python objects.

# YAML tag	Python type
# Standard YAML tags	
# !!null	None
# !!bool	bool
# !!int	int or long (int in Python 3)
# !!float	float
# !!binary	str (bytes in Python 3)
# !!timestamp	datetime.datetime
# !!omap, !!pairs	list of pairs
# !!set	set
# !!str	str or unicode (str in Python 3)
# !!seq	list
# !!map	dict
# Python-specific tags	
# !!python/none	None
# !!python/bool	bool
# !!python/bytes	(bytes in Python 3)
# !!python/str	str (str in Python 3)
# !!python/unicode	unicode (str in Python 3)
# !!python/int	int
# !!python/long	long (int in Python 3)
# !!python/float	float
# !!python/complex	complex
# !!python/list	list
# !!python/tuple	tuple
# !!python/dict	dict
# Complex Python tags	
# !!python/name:module.name	module.name
# !!python/module:package.module	package.module
# !!python/object:module.cls	module.cls instance
# !!python/object/new:module.cls	module.cls instance
# !!python/object/apply:module.f	value of f(...)
    

