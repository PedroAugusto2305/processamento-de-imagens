import cv2
import numpy as np
import matplotlib.pyplot as plt

imagem = cv2.imread('./image/alan.jpg', cv2.IMREAD_GRAYSCALE)


mediana_3 = cv2.medianBlur(imagem, 3)  
mediana_7 = cv2.medianBlur(imagem, 7)  

# Mostrar as imagens com matplotlib
plt.figure(figsize=(15, 10))

plt.subplot(2, 2, 1)
plt.imshow(imagem, cmap='gray')
plt.title("Imagem Original")
plt.axis("off")

plt.subplot(2, 2, 2)
plt.imshow(mediana_3, cmap='gray')
plt.title("Filtro de Mediana 3x3")
plt.axis("off")

plt.subplot(2, 2, 3)
plt.imshow(mediana_7, cmap='gray')
plt.title("Filtro de Mediana 7x7")
plt.axis("off")

plt.show()
