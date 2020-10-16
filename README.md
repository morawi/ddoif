# DDOIF - Digital Data Organization and Exchange in Fashion

## Towards a standaridized look of fashion data
The fashion industry is looking forward to use artificial intelligence technologies to enhance their processes, services, and applications. Although the amount of fashion data currently in use is increasing, there is a large gap in data exchange between the fashion industry and the related AI companies, not to mention the different structure used for each fashion dataset. As a result, AI companies are relying on manually annotated fashion data to build different applications. Furthermore, as of this writing, the terminology, vocabulary and methods of data representation used to denote fashion items are still ambiguous and confusing. Hence, it is clear that the fashion industry and AI companies will benefit from a protocol that allows them to exchange and organise fashion information in a unified way. To achieve this goal we aim (1) to define a protocol called DDOIF that will allow interoperability of fashion data; (2) for DDOIF to contain diverse entities including extensive information on clothing and accessories attributes in the form of text and various media formats; and (3)To design and implement an API that includes, among other things, functions for importing and exporting a file built according to the DDOIF protocol that stores all information about a single item of clothing. To this end, we identified over 1000 class and subclass names used to name fashion items and use them to build the DDOIF dictionary. We make DDOIF publicly available to all interested users and developers and look forward to engaging more collaborators to improve and enrich it.

For more details see https://arxiv.org/abs/2009.03005 


![symbol](https://github.com/morawi/ddoif/blob/master/figures/symbol.svg)


## Objective:
Enable interoperable data exchange within and between Fashion Industry and AI companies

## Python 3.7

## Dependencies:
- https://pypi.org/project/PyYAML/
- https://pypi.org/project/ruamel.yaml/
- https://pypi.org/project/dicttoxml/
- https://pypi.org/project/opencv-python/
- https://pypi.org/project/PyWavefront/
- https://pypi.org/project/pyglet/

## DDOIF Manual 
The manual conains important information about the DDOIF file structure and API usage. It demonstrates the functions that can be used to handle a ".ddof" file. See 
[Manual](https://github.com/morawi/ddoif/blob/master/Manual/) folder for details 

## Fashion classes according to DDOIF dictionary are graphically shown below.

## DDOIF-Classes
![DDOIF-classes](https://github.com/morawi/ddoif/blob/master/figures/ddoif.svg)



## Anatomy-Class
![Anatomy-class](https://github.com/morawi/ddoif/blob/master/figures/anatomy.svg)

## Clothing-Class
![Clothing-class](https://github.com/morawi/ddoif/blob/master/figures/clothing_classes.svg)



## Accessory-Class
![Accessory-classes](https://github.com/morawi/ddoif/blob/master/figures/accessory_class.svg)

## Footwear-Class
![Footwear-Classes](https://github.com/morawi/ddoif/blob/master/figures/footwear_class.svg)


Fabric-Class             |  Care-Class                         
:-------------------------:|:-------------------------:
![](https://github.com/morawi/ddoif/blob/master/figures/fabric_class.svg) | ![](https://github.com/morawi/ddoif/blob/master/figures/care.svg)  
  


Media-Class             |  Color-Class             |  Post-processing-Class              |  Pattern-Class              |  Material-Class             
:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:
![](https://github.com/morawi/ddoif/blob/master/figures/media.svg) | ![](https://github.com/morawi/ddoif/blob/master/figures/color.svg)  | ![](https://github.com/morawi/ddoif/blob/master/figures/post-processing.svg)  | ![](https://github.com/morawi/ddoif/blob/master/figures/pattern.svg)  | ![](https://github.com/morawi/ddoif/blob/master/figures/material_class.svg)  
  
Sustainability-Class             |  Personal-Characteristics-Class             |  Size-n-Fit-Class              |  Annotation-Class              |  Information-Class             
:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:
![](https://github.com/morawi/ddoif/blob/master/figures/sustainability.svg) | ![](https://github.com/morawi/ddoif/blob/master/figures/personal_char.svg)  | ![](https://github.com/morawi/ddoif/blob/master/figures/sizenfit.svg)  | ![](https://github.com/morawi/ddoif/blob/master/figures/annotation.svg)  | ![](https://github.com/morawi/ddoif/blob/master/figures/info.svg)  





