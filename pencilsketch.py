import cv2
img_location='C:/Users/EXAM1001/Desktop/'
filename='dog.jpg'
img=cv2.imread(img_location+filename)


#convert to greyscale
#images are read as NumPy arrays, and their channels are represented in BGR (Blue, Green, Red) order rather than the more common RGB (Red, Green, Blue) order
gray_image=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#INVERT THE IMAGE
inverted_gray_image=255-gray_image


#BLUR IMAGE BY GAUSSIAN FUNCTION
blurred_img=cv2.GaussianBlur(inverted_gray_image, (21,21), 0)

#INVERT BLUR IMAGE
inverted_blur_img=255-blurred_img

#PENCIL SKETCH
pencil_sketch_img=cv2.divide(gray_image, inverted_blur_img, scale=256.0)

#TO SHOW IMG
cv2.imshow('Original Image',img)
cv2.imshow('New Image2',gray_image)
cv2.imshow('New Image',inverted_gray_image)
cv2.imshow('New Image3',blurred_img)
cv2.imshow('New Image4',inverted_blur_img)
cv2.imshow('New Image5',pencil_sketch_img)
cv2.waitKey(0)
