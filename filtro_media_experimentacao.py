import cv2
import numpy as np
import matplotlib.pyplot as plt

imagem = cv2.imread('./image/alan.jpg', cv2.IMREAD_GRAYSCALE)

filtro_3x3 = cv2.blur(imagem, (3, 3))

filtro_5x5 = cv2.blur(imagem, (5, 5))

filtro_7x7 = cv2.blur(imagem, (7, 7))

plt.figure(figsize=(15, 10))

plt.subplot(2, 2, 1)
plt.imshow(imagem, cmap='gray')
plt.title('Imagem Original')
plt.axis('off')

plt.subplot(2, 2, 2)
plt.imshow(filtro_3x3, cmap='gray')
plt.title('Filtro de Média 3x3')
plt.axis('off')

plt.subplot(2, 2, 3)
plt.imshow(filtro_5x5, cmap='gray')
plt.title('Filtro de Média 5x5')
plt.axis('off')


plt.subplot(2, 2, 4)
plt.imshow(filtro_7x7, cmap='gray')
plt.title('Filtro de Média 7x7')
plt.axis('off')

plt.show()