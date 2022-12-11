#!/usr/bin/env python
# coding: utf-8

# In[9]:


from pathlib import Path
from matplotlib import pyplot as plt
import numpy as np
import cv2
import glob


# In[10]:


### Source of the hiragana images
source = Path('C:/Users/andma/OneDrive/Documenti/hiragana images/hiragana_images')
source_str = 'C:/Users/andma/OneDrive/Documenti/hiragana images/hiragana_images'


# In[3]:


### Obtaining the complete paths of all source images
subdirect = [x for x in source.iterdir() if x.is_dir()]

subdirect_string = [str(path) for path in subdirect]

source_images = [glob.glob(path + '/*.jpg') for path in subdirect_string]

images_path = []
for lists in source_images:
    for path in lists:
        images_path.append(path)


# In[21]:


subdirect = [x for x in source.iterdir() if x.is_dir()]

subdirect_string = [str(path) for path in subdirect]

for subfolder in subdirect_string:
    
    source_images = [glob.glob(subfolder + '/*.jpg')]  
    images_path = []
    for lists in source_images:
        for path in lists:
            images_path.append(path)
        
    for image in images_path:
        
        kana = cv2.imread(image) 
    
        #### Adding 1 pixel padding to the bottom of the images to obtain 84x84 pixels images
        padded_image = cv2.copyMakeBorder(kana, 0, 0, 1, 0, cv2.BORDER_CONSTANT)
        
        cv2.imwrite(image,padded_image) 

