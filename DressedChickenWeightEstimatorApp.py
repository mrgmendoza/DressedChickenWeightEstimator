import cv2


imageSrc = 'images/chicken.jpg'
image = cv2.imread(imageSrc)
grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(grayImage, (3, 3), 0)
ref, binaryImage = cv2.threshold(blur, 200, 255, cv2.THRESH_BINARY)

if image is not None:
    cv2.imshow("V's image", binaryImage)
elif image is None:
    print("error!")

k = cv2.waitKey(0)
cv2.destroyAllWindows()
