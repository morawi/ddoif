# -*- coding: utf-8 -*-
"""
Created on Wed May 20 12:41:11 2020

@author: malrawi



"""




from ddoif_utils import read_yaml_as_dict
import json
import binascii
import cv2


def dict_to_binary(the_dict):
    dict_in_bytes = json.dumps(the_dict).encode('utf-8')
    num_of_bytes= len(dict_in_bytes) # seems this is important step to remove the tuple!
    return dict_in_bytes, num_of_bytes

def binary_to_dict(dict_in_binary):
    the_dict = json.loads(dict_in_binary.decode('utf-8'))
    return the_dict

def string_to_8_bytes(s):
    s8 = "_"*(8-len(s)) + s
    s8 = bytes(s8, 'utf-8', 'big')
    return s8
def remove_space_from_string(s):
    s= s.replace('_', '') 
    return s

def ddoif_write(dict_in_bytes, media_buffer='', out_f='ATest.ddof'):
    with open('ATest.ddof', 'wb') as file:   
        ddoif_header = b"\x89" + "DDOIF\r\n\x1A\n".encode('utf-8') # 10 bytes signature / header
        file.write(ddoif_header) # the letters DDOIF, allowing a person to identify the format easily if it is viewed in a text editor
        reserved_bytes_for_futuer = 16
        rserved_bytes = (0).to_bytes(reserved_bytes_for_futuer, byteorder='big')   # getting  num_bytes = int.from_bytes(xx, 'big')
        file.write(rserved_bytes) # bytes reserved for future edditions, in case one needs to add more info to the header
        nm_bytes_of_ddoif_structure = (len(dict_in_bytes)).to_bytes(4, byteorder='big')   # getting  num_bytes = int.from_bytes(xx, 'big')                
        file.write(nm_bytes_of_ddoif_structure)
        file.write(dict_in_bytes)
        ''' Storing Media Files'''
        for i in range(len(media_buffer['buffer'])):  
            buffer_name = media_buffer['media_name'][i] 
            buffer_name = string_to_8_bytes(buffer_name) # to be stored into 8 bytes 
            file.write(buffer_name)
            buffer = media_buffer['buffer'][i]
            CRC_buffer = (binascii.crc32(buffer)).to_bytes(4, byteorder='big'); 
            file.write(CRC_buffer) # 4 bytes            
            nm_bytes_of_buffer = (len(buffer)).to_bytes(4, byteorder='big')
            file.write(nm_bytes_of_buffer)
            file.write(buffer)            
        
        file.close()
        print('saved successfuly')
        

def ddoif_read(in_f='ATest.ddof'):
    with open('ATest.ddof', 'rb') as file:            
        reserved_bytes_for_futuer = 16  
        is_ddoif = file.read(5) # the letters DDOIF, allowing a person to identify the format easily if it is viewed in a text editor
        if is_ddoif != bytes('DDOIF', 'utf-8'):
            print('Not a DDOIF file'); exit()
        dump = file.read(reserved_bytes_for_futuer) # bytes reserved for future edditions, in case one needs to add more info to the header
        if not dump: 
            print('Something went wrong in the reserved strucure, please check the file')
        nm_bytes_of_ddoif_structure = file.read(4)
        if nm_bytes_of_ddoif_structure:
            nm_bytes_of_ddoif_structure = int.from_bytes(nm_bytes_of_ddoif_structure, 'big')
        else:
            print('could  not read bytes')
            exit()          
            
        dict_in_bytes = file.read(nm_bytes_of_ddoif_structure)
        file.close()
        print('laoded successfuly')
        ddoif_dict = binary_to_dict(dict_in_bytes)
        
        return ddoif_dict
    


# my_dict = {'key' : [1,2,3]}
my_dict = read_yaml_as_dict('ddoif_dictionary.yaml')
dict_in_bytes, num_of_bytes = dict_to_binary(my_dict)

img = cv2.imread(r"C:/Users/msalr/Desktop/testing_images/didi 2.png")
# encode
media_format = "png"
is_success, buffer = cv2.imencode("."+ media_format, img)
if not is_success:
    print('unable to read image')
    exit()    

# fill the buffer with different media buffers
media_buffer={}
media_buffer['buffer'] = []; media_buffer['media_name'] = []
media_buffer['buffer'].append(buffer)
media_buffer['media_name'].append(media_format.upper())

# experiment, adding it twice
media_buffer['buffer'].append(buffer)
media_buffer['media_name'].append(media_format.upper())

ddoif_write(dict_in_bytes, media_buffer = media_buffer)
xx= ddoif_read()


# to Decode the image, 
img2 = cv2.imdecode(buffer, flags=-1) # Return the loaded image as is (with alpha channel).






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