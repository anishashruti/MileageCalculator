import numpy as np
from PIL import Image
from matplotlib import pyplot as plt

# original image
dashboard = Image.open('car_dashboard.jpg')
plt.figure(figsize=(8, 8))
plt.subplot(3, 3, 1)
plt.imshow(np.array(dashboard), cmap='gray')
plt.title("original image")

# grayscaling
dashboard_gray = dashboard.convert('L')
plt.subplot(3, 3, 2)
plt.imshow(np.array(dashboard_gray), cmap='gray')
plt.title("Grayscale image")

# getting ROI
crop_dashboard = dashboard_gray.crop((370, 320, 480, 450))
plt.subplot(3, 3, 3)
plt.imshow(np.array(crop_dashboard), cmap='gray')
plt.title("ROI image")

# blurred_image = cv2.GaussianBlur(np.array(dashboard), (3, 3), 0)
plt.tight_layout()
plt.show()
