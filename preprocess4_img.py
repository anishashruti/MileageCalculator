import cv2
import numpy as np
from PIL import Image, ImageEnhance, ImageOps
from matplotlib import pyplot as plt

'''
Order of preprocessing:
original
getting ROI
Thresholding
grayscale


'''
# original image
dashboard = Image.open('car_dashboard.jpg')
plt.figure(figsize=(8, 8))
plt.subplot(2, 2, 1)
plt.imshow(np.array(dashboard), cmap='gray')
plt.title("original image")

# getting ROI
crop_dashboard = dashboard.crop((370, 320, 480, 450))
plt.subplot(2, 2, 2)
plt.imshow(np.array(crop_dashboard), cmap='gray')
plt.title("ROI image")

# Thresholding
image_binary= ImageOps.invert(crop_dashboard)
plt.subplot(2, 2, 3)
plt.imshow(np.array(image_binary), cmap='gray')
plt.title("ROI image")

# grayscaling
dashboard_gray = image_binary.convert('L')
plt.subplot(2, 2, 4)
plt.imshow(np.array(dashboard_gray), cmap='gray')
plt.title("Grayscale image")

'''
#enhancer
enhancer = ImageEnhance.Contrast(blurred_image)
image_contrast=enhancer.enhace(2.0)
plt.subplot(3, 3, 5)
plt.imshow(np.array(image_contrast), cmap='gray')
plt.title("contrast adjustment")
'''

plt.tight_layout()
plt.show()
