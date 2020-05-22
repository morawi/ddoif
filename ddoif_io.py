# -*- coding: utf-8 -*-
"""
Created on Wed May 20 12:41:11 2020

@author: malrawi



"""





import json
import binascii

import numpy as np


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

def ddoif_write(ddoif_dict, media_buffer='', out_f='ATest.ddof'):
    dict_in_bytes, num_bytes = dict_to_binary(ddoif_dict)
    with open('ATest.ddof', 'wb') as file:   
        ddoif_header = b"\x89" + "DDOIF\r\n\x1A\n".encode('ascii') # 10 bytes signature / header
        file.write(ddoif_header) # the letters DDOIF, allowing a person to identify the format easily if it is viewed in a text editor
        reserved_bytes_for_futuer = 16
        rserved_bytes = (0).to_bytes(reserved_bytes_for_futuer, byteorder='big')   # getting  num_bytes = int.from_bytes(xx, 'big')
        file.write(rserved_bytes) # bytes reserved for future edditions, in case one needs to add more info to the header
        nm_bytes_of_ddoif_structure = (num_bytes).to_bytes(4, byteorder='big')   # getting  num_bytes = int.from_bytes(xx, 'big')                
        file.write(nm_bytes_of_ddoif_structure)
        file.write(dict_in_bytes)
        ''' Storing Media Files'''
        num_buffers = len(media_buffer['buffer'])
        file.write( (num_buffers).to_bytes(2, byteorder='big') )        
        for i in range(num_buffers):  
            buffer_name = media_buffer['media_format'][i] 
            buffer_name = string_to_8_bytes(buffer_name) # to be stored into 8 bytes 
            file.write(buffer_name)
            buffer = media_buffer['buffer'][i]
            CRC_buffer = (binascii.crc32(buffer)).to_bytes(4, byteorder='big')
            file.write(CRC_buffer) # 4 bytes            
            nm_bytes_of_buffer = (len(buffer)).to_bytes(4, byteorder='big')
            file.write(nm_bytes_of_buffer)
            file.write(buffer)            
        
        file.close()
        print('saved successfuly')
        

def ddoif_read(in_f='ATest.ddof'):
    with open('ATest.ddof', 'rb') as file:
        media_buffer={}; media_buffer['buffer'] = []; media_buffer['media_format'] = []  
        reserved_bytes_for_futuer = 16  
        is_ddoif = file.read(10) # the letters DDOIF, allowing a person to identify the format easily if it is viewed in a text editor
        if is_ddoif != b"\x89" + "DDOIF\r\n\x1A\n".encode('ascii'):
            print('Not a DDOIF file'); exit()
        dump = file.read(reserved_bytes_for_futuer) # bytes reserved for future edditions, in case one needs to add more info to the header
        if not dump: 
            print('Something went wrong in the reserved strucure, please check the file')
        nm_bytes_of_ddoif_structure = file.read(4)
        nm_bytes_of_ddoif_structure = int.from_bytes(nm_bytes_of_ddoif_structure, 'big')
        dict_in_bytes = file.read(nm_bytes_of_ddoif_structure)
        ddoif_dict = binary_to_dict(dict_in_bytes)
        
        num_buffers = int.from_bytes( file.read(2), 'big')
        
        for i in range(num_buffers): 
            media_format = file.read(8).decode(encoding='utf-8')
            media_buffer['media_format'].append( remove_space_from_string(media_format))
            CRC_buffer = file.read(4)
            nm_bytes_of_buffer = int.from_bytes( file.read(4), 'big')
            buffer = file.read(nm_bytes_of_buffer)            
            # if CRC_buffer != (binascii.crc32(buffer)).to_bytes(4, byteorder='big'): print('problem in CRC'); exit()
            buffer = np.frombuffer(buffer, dtype=np.uint8)
            media_buffer['buffer'].append(buffer)            
            
        file.close()
        print('laoded successfuly')
        
        
        return ddoif_dict, media_buffer
    

