import cv2
face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
img=cv2.imread("IMG-20191228-WA0010.jpg")
# IMG-20191228-WA0010.jpg,IMG-20220106-WA0019.jpg
grayimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
face=face_cascade.detectMultiScale(grayimg,1.1,7)
for x,y,w,h in face:
    img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
cv2.imshow("Gray",img)
cv2.waitKey(10000)
cv2.destroyAllWindows()

#for video

# face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
# # img=cv2.imread("IMG-20200106-WA0019.jpg")
# # IMG-20191228-WA0010.jpg,IMG-20220106-WA0019.jpg
# cap=cv2.VideoCapture(0)
# while True:
#     check,img=cap.read()
#     print(img)
#     grayimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#     face=face_cascade.detectMultiScale(grayimg,1.1,7)
#     for (x,y,w,h) in face:
#         img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
#     cv2.imshow("img",img)
#     k=cv2.waitKey(30) & 0xff
#     if k==27:
#         break
# cap.release()
# cv2.destroyAllWindows()