import cv2 

cap = cv2.VideoCapture(0)

ret, frame = cap.read() 
frame = cv2.resize(frame, (640, 360))

cv2.imshow('newFrame', frame)

cv2.waitKey(0)

cap.release() 
cv2.destroyAllWindows() 
