import cv2

imgPath = "people.jpg"
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
img = cv2.imread(imgPath)
grayScaleImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
detectedFaces = face_cascade.detectMultiScale(grayScaleImage)

for x, y, w, h in detectedFaces:
    fra = cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)
    cv2.imshow("Face Detection", img)
    cv2.waitKey(200)

# print("Face Detection was done !!!")

while True:
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()
quit()