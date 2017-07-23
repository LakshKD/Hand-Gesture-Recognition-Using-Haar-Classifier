# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 11:31:17 2016

@author: abhishek
"""
import generateBox as gb
import cv2
import binarize as b
import imgcreatebase as i
import draw_contours as dc
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
img = cv2.imread('hand.jpg')
sz = 4
h,w = img.shape[:2]
img = img[3:h-6,3:w-6]
rects = gb.generateCenterBox(img, 3, sz)
imgs = b.img_binarizer(img, findmedian(img, rects, sz))
'''cv2.imshow('1', i.sumAndBlurImg(imgs))'''
d = i.sumAndBlurImg(imgs)
print d
cv2.imwrite("processed_hand.jpg",i.sumAndBlurImg(imgs))
im = cv2.imread('processed_hand.jpg')
#print im
imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
#print imgray
modified_img = dc.draw_contour(im,imgray)
cv2.imshow('1',modified_img)
cv2.imwrite("Contour_hand.jpg",modified_img)
cv2.waitKey(100000)


#---------------------------------------------testing------------------------------------------------
    



