import cv2
img_file='car_image.jpg'
car_classifier_file = 'car_detector.xml'
car_tracker = cv2.CascadeClassifier(car_classifier_file)
img = cv2.imread(img_file)
b_n_w =cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cars = car_tracker.detectMultiScale(b_n_w)
print(cars)
for (x, y, w, h) in cars:
    cv2.rectangle(img, (x, y), (x+w,y+h), (0, 0, 255), 2)
cv2.imshow('Car Detection Result', img)
cv2.waitKey() 
