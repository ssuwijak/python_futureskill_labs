import cv2

vdoCapture = cv2.VideoCapture(0)
# vdoCapture = cv2.VideoCapture("demo.mp4")

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

while True:
    ret, frames = vdoCapture.read()
    grayScaleFrame = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
    detectedFaces = face_cascade.detectMultiScale(grayScaleFrame)
    
    for x, y, w, h in detectedFaces:
        cv2.rectangle(frames, (x,y), (x+w, y+h), (0,255,0), 2)
    
    cv2.imshow("Video Face Detection ... press 'q' to exit", frames)
    
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    
vdoCapture.release()
cv2.destroyAllWindows()
quit()
