import numpy as np
import cv2

car_cascade = cv2.CascadeClassifier("training/cascade.xml") # carrega o HaarCascade treinado para detecção de mascaras

img = cv2.imread("positives/withmask_1.jpg") # testes com imagens positivas
height, width, c = img.shape # altura e largura da imagem
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # converte a imagem para escala de cinza
objetos = car_cascade.detectMultiScale(gray, 1.01, 5) # coordenadas dos objetos identificados

print(objetos) # print das coordenadas

n = 1
for (x,y,w,h) in objetos:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2) # desenha um retangulo para cada mascara identificada
    cv2.putText(img, str(f"Mask #{n}"), (x, y-5), cv2.FONT_HERSHEY_DUPLEX, 0.4, (0, 0, 255), 1) # texto para a contagem de mascaras identificadas
    n += 1

cv2.imshow('Mask Recognition', img)
cv2.waitKey(0)
cv2.destroyAllWindows()