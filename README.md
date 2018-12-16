# Vehicle Detect With Haar Cascade
This application make use of haar cascade classifier in opencv-python to detect the vehicle in images. 
required:
  - python: version 3.7
  - opencv-python: version 3.4.4.19
  - google map api
  - traffic image (https://data.gov.sg/dataset/traffic-images)
  - Image for cascade training:
    3217 positve and 1301 negative(http://funvision.blogspot.com/2016/11/computer-vision-car-dataset-for-opencv.html)

traffic.py is the main code where each image is processed on number of vehicles detected.
IndividualImageTest.py is to test individual image on exactly where the detected vehicle in image.
cascade.xml inside cardata/classifier are self-trained and may have accuracy issues, it does not work well in following condition: night,small vehicle image and etc.
