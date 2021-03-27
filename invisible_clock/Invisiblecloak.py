#Importing Libraries
import cv2
import numpy as np
import time



print("""
get aside of camera, let the system capture your background
    """)
cap = cv2.VideoCapture(0)


time.sleep(5)
c = 0 #count
background=0

#  taking backgrounf
for i in range(50):

while(cap.isOpened()):
	ret, img = cap.read()
	if not ret:
		break
	c=c+1
	
	# Converting the color space from BGR to HSV #HSV=Hue Saturation Value(Hue changes for colour but saturation and value remains same for a range)
	hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

	# Generating mask to detect blue color
	lowerblue_ = np.array([94, 80, 2])
	upperblue_ = np.array([126, 255, 255])
	mask1 = cv2.inRange(hsv,lowerblue_,upperblue_)

	lowerblue_ = np.array([130,80,2])
	upperblue_ = np.array([140,255,255])
	mask2 = cv2.inRange(hsv,lowerblue_,upperblue_)

	mask1 = mask1+mask2 #covering background with mask

	# Refining the mask corresponding to the detected blue color
	mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, np.ones((3,3),np.uint8),iterations=2)
	mask1 = cv2.dilate(mask1,np.ones((3,3),np.uint8),iterations = 1)
	mask2 = cv2.bitwise_not(mask1)

	# Creating the final 
	res1 = cv2.bitwise_and(background,background,mask=mask1) #performing bitwise And
	res2 = cv2.bitwise_and(img,img,mask=mask2)
	final_output = cv2.addWeighted(res1,1,res2,1,0)

	cv2.imshow('Magical !!!',final_output) #imshow to see the result
	k = cv2.waitKey(10)
	if k == 27: #press esc key to quit
		break
cv2.destroyAllWindows() #Destroys all windows(quit)

