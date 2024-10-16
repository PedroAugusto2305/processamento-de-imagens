import cv2
import numpy as np
import matplotlib.pyplot as plt

# carregando a imagem em tons de cinza
imagem = cv2.imread('./image/alan.jpg', cv2.IMREAD_GRAYSCALE)

# aplicando filtro Laplaciano
laplaciano = cv2.Laplacian(imagem, cv2.CV_64F)

# mostrar a imagem original e a imagem com o filtro aplicado lado a lado
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.title('Imagem original')
plt.imshow(imagem, cmap='gray')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title('Filtro Laplaciano')
plt.imshow(laplaciano, cmap='gray')
plt.axis('off')


plt.tight_layout()
plt.show()