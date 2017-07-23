import Image
import cv2
import numpy as np
def sumAndBlurImg(img):
	a, b = img[0].shape
	pixels = np.zeros((a, b))
	for i in range(0, a):
		for j in range(0, b):
			c = 0
			for k in range(0, len(img)):
				if(img[k][i,j] == 255 ):
					c += 1
			if(c > len(img)/2) :
				pixels[i, j] = 255
	
	pixels = cv2.blur(pixels,(5,5))
	return pixels

	




