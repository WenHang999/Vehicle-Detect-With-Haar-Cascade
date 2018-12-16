import json
import cv2
# Individual image test.
# place image here  
cap = cv2.VideoCapture('folder/image.jpg')

car_cascade = cv2.CascadeClassifier('CarData/classifier/cascade.xml') 
ret, img = cap.read()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cars = car_cascade.detectMultiScale(gray, 1.3, 5)
for (x,y,w,h) in cars:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()







