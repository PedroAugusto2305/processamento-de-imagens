import cv2
import numpy as np
import matplotlib.pyplot as plt

imagem = cv2.imread('./image/alan.jpg', cv2.IMREAD_GRAYSCALE)


mediana_5 = cv2.medianBlur(imagem, 5)  
mediana_11 = cv2.medianBlur(imagem, 15)  
mediana_21 = cv2.medianBlur(imagem, 25)  

# Mostrar as imagens com matplotlib
plt.figure(figsize=(15, 10))


plt.subplot(2, 2, 1)
plt.imshow(imagem, cmap='gray')
plt.title("Imagem Original")
plt.axis("off")


plt.subplot(2, 2, 2)
plt.imshow(mediana_5, cmap='gray')
plt.title("Filtro de Mediana 5x5")
plt.axis("off")


plt.subplot(2, 2, 3)
plt.imshow(mediana_11, cmap='gray')
plt.title("Filtro de Mediana 15x15")
plt.axis("off")


plt.subplot(2, 2, 4)
plt.imshow(mediana_21, cmap='gray')
plt.title("Filtro de Mediana 25x25")
plt.axis("off")

plt.show()
