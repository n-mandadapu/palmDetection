import cv2
frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10,150)
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")



while True:
    success, img = cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face = faceCascade.detectMultiScale(imgGray, 1.1, 4)

    for (x, y, w, h) in face:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    cv2.imshow("Result", img)
    cv2.imshow("Result1", imgGray)
    if cv2.waitKey(1) and 0xFF == ord('q'):
        break