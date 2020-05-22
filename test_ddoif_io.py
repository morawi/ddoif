# -*- coding: utf-8 -*-
"""
Created on Fri May 22 01:31:52 2020

@author: malrawi
"""

from ddoif_utils import read_yaml_as_dict
import cv2
import pywavefront
from ddoif_io import ddoif_read, ddoif_write



ddoif_dict = read_yaml_as_dict('ddoif_dictionary.yaml')

obj_3D = pywavefront.Wavefront('C:/Users/msalr/Desktop/testing_images/Tshirt.obj', \
                               strict=False, encoding="utf-8", parse=True, cache=True)

img = cv2.imread("C:/Users/msalr/Desktop/testing_images/didi 2.png")
# encode
media_format = "JPG-LS" # png, bmp
is_success, buffer = cv2.imencode("."+ media_format, img)
if not is_success:
    print('unable to read image')
    exit()    

# fill the buffer with different media buffers
media_buffer={}
media_buffer['buffer'] = []; media_buffer['media_format'] = []
media_buffer['buffer'].append(buffer)
media_buffer['media_format'].append(media_format.upper())

# experiment, adding it twice
media_buffer['buffer'].append(buffer)
media_buffer['media_format'].append(media_format.upper())

ddoif_write(ddoif_dict, media_buffer = media_buffer)
ddoif_dict2, media_buffer2= ddoif_read()
# to Decode the image, 
img2 = cv2.imdecode(media_buffer2['buffer'][0], flags=-1) # Return the loaded image as is (with alpha channel).




