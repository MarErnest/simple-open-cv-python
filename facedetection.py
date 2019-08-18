import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
faceImage = cv2.imread("photo.jpg")
faceImageGrey = cv2.cvtColor(faceImage, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(
  faceImageGrey, 
  scaleFactor=1.05,
  minNeighbors=5
)

for x, y, w, h in faces:
  img = cv2.rectangle(faceImage, (x, y), (x + w, y + h), (0, 255, 0), 3)

cv2.imshow("Gray", faceImage)
cv2.waitKey(0)
cv2.destroyAllWindows()