import cv2
import numpy as np
import matplotlib.pyplot as plt

imagem = cv2.imread('./image/alan.jpg', cv2.IMREAD_GRAYSCALE)

filtro_7x7 = cv2.blur(imagem, (7, 7))

filtro_15x15 = cv2.blur(imagem, (15, 15))

filtro_25x25 = cv2.blur(imagem, (25, 25))

plt.figure(figsize=(15, 10))

plt.subplot(2, 2, 1)
plt.imshow(imagem, cmap='gray')
plt.title('Imagem Original')
plt.axis('off')

plt.subplot(2, 2, 2)
plt.imshow(filtro_7x7, cmap='gray')
plt.title('Filtro de Média 7x7')
plt.axis('off')

plt.subplot(2, 2, 3)
plt.imshow(filtro_15x15, cmap='gray')
plt.title('Filtro de Média 15x15')
plt.axis('off')


plt.subplot(2, 2, 4)
plt.imshow(filtro_25x25, cmap='gray')
plt.title('Filtro de Média 25x25')
plt.axis('off')

plt.show()