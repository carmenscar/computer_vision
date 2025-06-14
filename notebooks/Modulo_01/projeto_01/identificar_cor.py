import cv2
import argparse
import numpy as np

# Inicializa a lista de amostras
samples = []


# Função callback para o evento do mouse
def callback(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        # Recupera as cores na localização do clique
        blue = frame[y, x, 0]
        green = frame[y, x, 1]
        red = frame[y, x, 2]
        # Adiciona a cor à lista de amostras
        samples.append([blue, green, red])
        # Calcula os limites inferior e superior
        lower_bound = np.amin(samples, axis=0)
        upper_bound = np.amax(samples, axis=0)
        print(f"Lower bound: {lower_bound}")
        print(f"Upper bound: {upper_bound}")
        # Desenha as informações na tela
        text = f"B: {blue}, G: {green}, R: {red}"
        cv2.putText(frame, text, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
        cv2.imshow('image', frame)

# Configura o argparse
parser = argparse.ArgumentParser(description='Script para extrair cores RGB de um video.')
parser.add_argument('-i', '--image', help='Caminho para o video.', required=True)
args = parser.parse_args()

# Carrega o primeiro frame do video
cap = cv2.VideoCapture(args.image)
ret, frame = cap.read()
if not ret:
    print(f"Não foi possível abrir o video: {args.image}")
    exit(1)

cv2.namedWindow('image')
cv2.setMouseCallback('image', callback)

# Exibe a imagem até que o usuário pressione 'q' ou 'esc'
while True:
    cv2.imshow('image', frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q') or key == 27:
        break

cap.release()
cv2.destroyAllWindows()
