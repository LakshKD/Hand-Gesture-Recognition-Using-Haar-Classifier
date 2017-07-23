# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 11:31:17 2016

@author: abhishek
"""
import numpy as np
import generateBox as gb
import cv2
import binarize as b
import imgcreatebase as i
import find_contour_and_convexity_defect as dc
def findmedian(image,boxes,size):
    lst=[]
    for corner in boxes:
        red=[]
        green=[]
        blue=[]
        l=[]
        for yval in range(corner['topy'],corner['topy']+size):
                for xval in range(corner['topx'],corner['topx']+size):
                    red.append(image[xval][yval][0])
                    green.append(image[xval][yval][1])
                    blue.append(image[xval][yval][2])
        red.sort()
        green.sort()
        blue.sort()
        retind=(len(red)+1)/2
        l.append(red[retind])
        l.append(green[retind])
        l.append(blue[retind])
        lst.append(l)
    return lst


#--------------------------------------------testing-------------------------------------------------
def matToImg(im, img) :
    imc = np.zeros_like(img)
    imc[:,:,0] = im
    imc[:,:,1] = im
    imc[:,:,2] = im
    im = imc
    return im
def preprocessImage(img) :
    #print img
    sz = 4
    h,w,_ = img.shape
    img = img[3:h-h/5,3:w-6]
    img = cv2.resize(img, (50, 50))
    rects = gb.generateCenterBox(img, 3, sz)
    imgs = b.img_binarizer(img, findmedian(img, rects, sz))
    im = i.sumAndBlurImg(imgs)
    im = matToImg(im, img)
    imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    #==========================================================#
    (modified_img, cnt) = dc.find_contour_and_convexity_defect(im, imgray)
    modified_img = cv2.resize(modified_img, (w-9, h-h/5-3))
    return (modified_img, cnt)
#---------------------------------------------testing------------------------------------------------
    



