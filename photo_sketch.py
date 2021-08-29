#Let's import required libraries
import cv2
import scipy.ndimage

#Read the image
Path = r"C:\Users\Prashant Srivastava\Desktop\Krish Projects\Photo Sketching\sketch.jpg"
img = cv2.imread(Path)
img = cv2.resize(img,(1400,800))

#Convert to grayscale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Invert the image
inverted_image = 225 - img_gray

#Apply blur
blur= scipy.ndimage.filters.gaussian_filter(inverted_image,sigma=5)
final =  cv2.addWeighted(blur,1,img_gray,1,0)


#Let's display original image
cv2.imshow("original",img)
#Let's display results
cv2.imshow("result",final)
cv2.waitKey(0)
