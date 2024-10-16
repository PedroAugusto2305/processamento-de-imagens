import cv2
import numpy as np
import matplotlib.pyplot as plt

imagem = cv2.imread('./image/alan.jpg', cv2.IMREAD_GRAYSCALE)

sobel_x = cv2.Sobel(imagem, cv2.CV_64F, 1, 0, ksize=3)

sobel_y = cv2.Sobel(imagem, cv2.CV_64F, 0, 1, ksize=3)

sobel_x = cv2.convertScaleAbs(sobel_x)
sobel_y = cv2.convertScaleAbs(sobel_y)

sobel_combinado = cv2.addWeighted(sobel_x, 0.5, sobel_y, 0.5, 0)

plt.figure(figsize=(10, 6))

plt.subplot(1, 3, 1)
plt.title('Imagem Original')
plt.imshow(imagem, cmap='gray')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.title('Filtro Sobel X')
plt.imshow(sobel_x, cmap='gray')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.title('Filtro Sobel Y')
plt.imshow(sobel_y, cmap='gray')
plt.axis('off')

plt.figure()
plt.title('Sobel Combinado')
plt.imshow(sobel_combinado, cmap='gray')
plt.axis('off')

plt.show()

