from PIL import Image
from pytesser import *
import cv2

img = cv2.imread('2_1.jpg')
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

for i in xrange(len(img)):
	for j in xrange(len(img[i])):
		if int(img[i][j]) > 80:
			img[i][j] = 255
		else:
			img[i][j] = 0

# cv2.namedWindow('image', cv2.WINDOW_NORMAL)
# cv2.imshow('image',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

img = img[500:1000, 1100:1400]

cv2.imwrite('new.jpg', img)

im = Image.open('new.jpg')
text = image_to_string(im)
text = image_file_to_string('new.jpg')
text = image_file_to_string('new.jpg', graceful_errors=True)
print "---------------------------------------------------------\n"
print text