import requests
import json
import cv2
import numpy as np
from flask import Flask, render_template, jsonify,request
app = Flask(__name__)

# test for individual image.
car_cascade = cv2.CascadeClassifier('CarData/classifier/cascade.xml')
cap = cv2.VideoCapture('testimg/13.jpg')
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
 
@app.route("/api/imgprocess",methods=['POST','GET'])
def apiImgprocess():
    imgUrl = request.form['imgUrl']
    car_cascade = cv2.CascadeClassifier('CarData/classifier/cascade.xml')
    cap = cv2.VideoCapture(imgUrl)
    img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cars = car_cascade.detectMultiScale(gray, 1.3, 5)
    if len(cars) < 10:
        message = "Light traffic"
    elif len(cars)>10 and len(cars)<20:   
        message = "Medium Traffic" 
    else:
        message = "Heavy Traffic"
    data = {"message":message,"Count":len(cars)} 
    return jsonify(data)

@app.route("/", methods=["GET"])
def retreive():
    return render_template('index.html') 
if __name__ == '__main__':
   app.run(debug=True,host="0.0.0.0")






