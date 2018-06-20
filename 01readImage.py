#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 13:36:32 2018

@author: hrishi
"""

# librarry import
#import numpy as np
import cv2

# read Image
colorImage = cv2.imread('SampleImages/picture.jpg', 1)
grayImage = cv2.imread('SampleImages/picture.jpg', 0)


# display image
cv2.imshow('Color Image', colorImage)
cv2.imshow('Gray Image', grayImage)

# keep image open until program is stopped
cv2.waitKey(0)

# close all associated windows
cv2.destroyAllWindows()

# save grayscale image

cv2.imwrite('SampleImages/pictureGray.jpg', grayImage)