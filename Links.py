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
# https://stackoverflow.com/questions/3790454/how-do-i-break-a-string-over-multiple-lines

''' 

# very important on fabric make and types
https://www.textileschool.com/171/textile-fabric-types-comprehensive-list-of-textile-fabrics/ 

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


"""


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
    



''' 
to get to bytes you can use json.dumps(variables).encode('utf-8') 
then to convert back from bytes you can use json.loads(s.decode('utf-8'))

read(file, 'ab') or 'rb+'  , but seems 'r+b' for python2
'ab' forces all writes to happen at the end of the file. You probably want 'r+b'.


https://stackoverflow.com/questions/40890697/python3-reading-a-binary-file-4-bytes-at-a-time-and-xor-it-with-a-4-byte-long-k
https://stackoverflow.com/questions/4388201/how-to-seek-and-append-to-a-binary-file-in-python


using seek:
    
    NOTE : Remember new bytes over write previous bytes

As per python 3 syntax

with open('myfile.dat', 'wb') as file:
    b = bytearray(b'This is a sample')
    file.write(b)

with open('myfile.dat', 'rb+') as file:
    file.seek(5)
    b1 = bytearray(b'  text')
    #remember new bytes over write previous bytes
    file.write(b1)

with open('myfile.dat', 'rb') as file:
    print(file.read())
OUTPUT

b'This   textample'
remember new bytes over write previous bytes


'''

'''

def dict_to_binary(the_dict):
    str = json.dumps(the_dict)
    binary = ' '.join(format(ord(letter), 'b') for letter in str)
    return binary


def binary_to_dict(the_binary):
    jsn = ''.join(chr(int(x, 2)) for x in the_binary.split())
    d = json.loads(jsn)  
    return d

bin = dict_to_binary(my_dict)
print (bin)

dct = binary_to_dict(bin)
print( dct)

will give the output

1111011 100010 1101011 100010 111010 100000 1011011 110001 101100 100000 110010 101100 100000 110011 1011101 1111101

{u'key': [1, 2, 3]}

'''