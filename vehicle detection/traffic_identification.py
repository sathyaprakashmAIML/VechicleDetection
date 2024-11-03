import cv2
import imutils
cascade='cars.xml'
cascade_classifier=cv2.CascadeClassifier(cascade)
cam=cv2.VideoCapture(0)
while True:
    a,img=cam.read()
    resize=imutils.resize(img,width=1000,height=1000)
    gray=cv2.cvtColor(resize,cv2.COLOR_BGR2GRAY)
    cars=cascade_classifier.detectMultiScale(gray,1.1,4)
    for x,y,w,h in cars:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.imshow('Frame',img)    
    b=str(len(cars))
    a=int(b)
    if a>8:
        print('traffic')
    else:
        print('no traffic')
    if cv2.waitKey(10)==27:
        break
cam.release()
cv2.destroyAllWindows()
                      















                      
                      
                      
