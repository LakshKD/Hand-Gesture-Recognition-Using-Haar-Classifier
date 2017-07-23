import cv2
import numpy as np

img = cv2.imread('processed_hand.jpg')
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(img_gray, 127, 255,0)
_,contours,hierarchy = cv2.findContours(thresh,2,1)
cnt = contours[0]
count = 0
hull = cv2.convexHull(cnt,returnPoints = False)
defects = cv2.convexityDefects(cnt,hull)

for i in range(defects.shape[0]):
	s,e,f,d = defects[i,0]
	start = tuple(cnt[s][0])
	end = tuple(cnt[e][0])
	far = tuple(cnt[f][0])
	cv2.line(img,start,end,[0,255,0],2)
	cv2.circle(img,far,5,[0,0,255],-1)
	count = count + 1

print(count)
cv2.imwrite("hand2c.jpg",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
