import cv2
import numpy as np

imagem = cv2.imread('./image/alan.jpg')


# definir o kernel de aguçamento
kernel_agucamento = np.array([[0, -1, 0], 
                             [-1, 5, -1],
                             [0, -1, 0]])


# aplicar filtro de aguçamento usando convolução
imagem_agucada = cv2.filter2D(imagem, -1, kernel_agucamento)

# mostrar a imagem original e a imagem aguçada
cv2.imshow('Imagem Original', imagem)
cv2.imshow('Imagem Aguçada', imagem_agucada)

# esperar por uma tecla e fechar as janelas
cv2.waitKey(0)
cv2.destroyAllWindows()