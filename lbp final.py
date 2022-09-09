import cv2
face_cascade=cv2.CascadeClassifier("lbpcascade_frontalface.xml")
img=cv2.imread("img3.jpg")
#resize=cv2.resize(img,(int (img.shape[1]/2), int (img.shape[0]/2)))
grayimage=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces=face_cascade.detectMultiScale(grayimage,1.1,7)
for x,y,w,h in faces:
    img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)

cv2.imshow("abc",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
#print (img.shape[1])