#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 14:17:53 2018

@author: hrishi
"""

# librarry import
#import numpy as np
import cv2

# read Image
colorImage = cv2.imread('SampleImages/picture.jpg', 1)

# get image size
height = colorImage.shape[0]
width = colorImage.shape[1]

# Draw rectangnle 
cv2.rectangle(colorImage, (170,225), (235,290),(0,0,255),2 ,0)

# Draw circle 
cv2.circle(colorImage, (200,260), 125,(255,0,0), 2 ,0)


# get center of image
py = (height/2)
px = (width/2)

# Draw line 
cv2.line(colorImage, (px,0), (px, height),(0,255,0),2 ,0)
cv2.line(colorImage, (0,py), (width, py),(0,255,0),2 ,0)


# Draw line 
cv2.putText(colorImage,'Center', (px,py),cv2.FONT_HERSHEY_PLAIN,2,(0,0,0),2,cv2.LINE_AA)

# display image
cv2.imshow('Color Image', colorImage)

# keep image open until program is stopped
cv2.waitKey(0)

# close all associated windows
cv2.destroyAllWindows()

# save grayscale image

