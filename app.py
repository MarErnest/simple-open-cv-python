import cv2
import glob

# Gather Images
images = glob.glob("*.jpg")

# Resize Image
for image in images:
  rawImage = cv2.imread(image, 0)
  resizedImage = cv2.resize(rawImage, (100, 50))
  cv2.imshow(image, rawImage)
  cv2.waitKey(500)
  cv2.destroyAllWindows()
  cv2.imwrite('resized_' + image, resizedImage)

print("Done without errors...")