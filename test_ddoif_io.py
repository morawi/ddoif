# -*- coding: utf-8 -*-
"""
Created on Fri May 22 01:31:52 2020

@author: malrawi
"""

from ddoif_utils import read_yaml_as_dict
import cv2
import pywavefront
from ddoif_io import ddoif_read, ddoif_write
from matplotlib import pyplot as plt


ddoif_dict = read_yaml_as_dict('ddoif_dictionary.yaml')

#x = pywavefront.Wavefront('C:/Users/msalr/Desktop/testing_images/dress_flower.obj', \
#                               strict=False, encoding="utf-8", parse=True, cache=True)

path = "C:/Users/msalr/Desktop/CIKM20/"
image_names = ("jacket_back_human.jpg", 
               "jacket_back_side_human.jpg",
               "jacket_back_sleeve.jpg", 
               "jacket_back_view.jpg",
               "jacket_cuffs_view.jpg",
               "jacket_front_human.jpg",
               "jacket_front_side_human.jpg",
               "jacket_front_view.jpg",
               "jacket_frontal_buttons.jpg",
               "jacket_frontal_pocket.jpg")

media_buffer={}
media_buffer['buffer'] = []; 
media_buffer['media_format'] = []
for i, img_name in enumerate(image_names):
    img = cv2.imread(path +img_name)
    # encode
    media_format = "JPG" # png, bmp
    is_success, buffer = cv2.imencode("."+ media_format, img)
    if not is_success:
        print('unable to read image')
        exit()    
    
    # fill the buffer with different media buffers  
    media_buffer['buffer'].append(buffer)
    media_buffer['media_format'].append(media_format.upper())    
    
ddoif_write(ddoif_dict, media_buffer = media_buffer, out_f='Jacket.ddof')       
ddoif_dict2, media_buffer2= ddoif_read(in_f='Jacket.ddof')# to Decode the image, 
img2 = cv2.imdecode(media_buffer2['buffer'][0], flags=-1) # Return the loaded image as is (with alpha channel).
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

plt.figure(); plt.imshow(img2)





