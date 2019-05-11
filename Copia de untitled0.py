#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 11:03:35 2019

@author: lauramelisatorooquendo
"""

import numpy as np
import cv2

# Load an color image in grayscale
img = cv2.imread('lena.jpg',0)

blur = cv2.blur(img,(5,5)) # Aplicar filtro de suavizado a la imagen

cv2.imshow('image',img)
cv2.imshow('filtrada',blur)
cv2.waitKey(0)
cv2.destroyAllWindows()