import cv2
import numpy as np
import math as m

def mod(a) :
	return m.sqrt(a[0]**2 + a[1]**2)

def find_angle(s,f,e) :
	s = np.array(np.float32(s))
	e = np.array(np.float32(e))
	f = np.array(np.float32(f))
	a = s-f
	b = e-f
	a = a/mod(a)
	b = b/mod(b)
	dot = np.dot(a, b)
	return m.acos(dot)*180/m.pi

#print(find_angle([1,1], [0,0], [0,1]))

def find_contour_and_convexity_defect(im,imgray):
	ret,thresh = cv2.threshold(imgray,127,255,0)
	_,contours,hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	c = [len(c) for c in contours]
	im = cv2.drawContours(im, [contours[c.index(max(c))]], 0, (0,255,0), 1)
	cnt = [contours[c.index(max(c))]][0]
	hull = cv2.convexHull(cnt,returnPoints = False)
	defects = cv2.convexityDefects(cnt,hull)
	count = 0
	for i in range(defects.shape[0]):
		s,e,f,d = defects[i,0]
		start = tuple(cnt[s][0])
		end = tuple(cnt[e][0])
		far = tuple(cnt[f][0])
		cv2.line(im,start,end,[0,255,0],2)
		angle = (find_angle(list(cnt[s][0]), list(cnt[f][0]), (cnt[e][0])))		
		if(angle < 90) :
			count += 1
			#cv2.circle(im,start,5,[0,255,255],-1)
			#cv2.circle(im,end,5,[0,255,255],-1)
			#cv2.circle(im,far,5,[0,0,255],-1)
	return (im, count)


"""
im = cv2.imread('processed_hand.jpg')
imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
modified_img = draw_contour(im,imgray)
'''ret,thresh = cv2.threshold(imgray,127,255,0)'''
'''_,contours, hierarchy = cv2.findContours(imgray,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)'''
cv2.imwrite("Contour_hand.jpg",modified_img)
'''img = cv2.drawContours(im,contours,-1,(0,255,0),2)'''
'''cv2.imwrite("abc.jpg",img)'''
"""
