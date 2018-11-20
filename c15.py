# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 11:14:35 2018

@author: ASUS
"""
import math
import cv2
import numpy as np
from c13 import MyProcess


class Psnr(MyProcess):

    def psnr_8bit(self, img1, img2):
        """
        Calculate the psnr of the two images of 8-bit, like jpg
    param img1: Figure 1 path
    param img2: Figure 2 path
    return: psnr value of two images
        """
        original = cv2.imread(img1, cv2.IMREAD_GRAYSCALE)
        contrast = cv2.imread(img2, cv2.IMREAD_GRAYSCALE)
        float32_original = original.astype(np.float32)
        float32_contrast = contrast.astype(np.float32)
        diff = cv2.absdiff(float32_contrast, float32_original)
        mse = np.mean(diff ** 2)
        
        if mse == 0:
            return 100
        else:
            PIXEL_MAX = 255.0
            return 20 * math.log10(PIXEL_MAX / math.sqrt(mse))

    def psnr_16bit(self, img1, img2):
        """
        Calculate the psnr of the two images of 16-bit, like tiff
    param img1: Figure 1 path
    param img2: Figure 2 path
    return: psnr value of two images
        """
        original = cv2.imread(img1, -1)
        contrast = cv2.imread(img2, -1)
        float32_original = original.astype(np.float64)
        float32_contrast = contrast.astype(np.float64)
        diff = cv2.absdiff(float32_contrast, float32_original)
        mse = np.mean(diff ** 2)
        if mse == 0:
            return 100
        else:
            PIXEL_MAX = 65535.0
            return 20 * math.log10(PIXEL_MAX / math.sqrt(mse))


