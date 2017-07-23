import cv2
import numpy as np

def creatDict(x, y) :
	box = {}
	box['topx'] = x
	box['topy'] = y
	return box

def generateCenterBox(img, factor, sz) :
	w, h, channels = img.shape
	sw = w/factor
	sh = h/factor
	mtopx = w/2-sw/2
	mtopy = h/2-sh/2
	listOfBoxes = []
	listOfBoxes.append(creatDict(mtopx, mtopy))
	listOfBoxes.append(creatDict(w/2-sz/2, mtopy))
	listOfBoxes.append(creatDict(w/2+sw/2-sz, mtopy))
	listOfBoxes.append(creatDict(mtopx, h/2-sz/2))
	listOfBoxes.append(creatDict(w/2-sz/2, h/2-sz/2))
	listOfBoxes.append(creatDict(w/2+sw/2-sz, h/2-sz/2))
	listOfBoxes.append(creatDict(mtopx, h/2+sh/2-sz/2))
	listOfBoxes.append(creatDict(w/2-sz/2, h/2+sh/2-sz))
	listOfBoxes.append(creatDict(w/2+sw/2-sz, h/2+sh/2-sz))
	return listOfBoxes

#-----------------------------------------------------testing-----------------------------------------

img = cv2.imread('star.png')
color = (0, 255, 0)
sz = 4
rects = generateCenterBox(img, 8, sz)
for dict in rects :
	cv2.rectangle(img, (dict['topx'], dict['topy']), (dict['topx']+sz, dict['topy']+sz), color, 1)
#cv2.imshow('1', img)
#cv2.waitKey(100000)
#-----------------------------------------------------testing-----------------------------------------
