"""
This module contains a script to extract RGB colors from a video using OpenCV.

The script opens a video file and displays its frames. When the user clicks on a pixel in the frame, the script
extracts the RGB color of that pixel and adds it to a list of color samples. Then, the script calculates the lower
and upper bounds of the color range based on the samples and displays the color information on the frame.

!Important:
To run this module, it is essential that 'opencv-python-headless' is **not** installed.
If you encounter the error:
    '(-2:Unspecified error) The function is not implemented.'
it usually means that GUI support is missing due to 'opencv-python-headless' being present,
which may have been installed as an indirect dependency.

One common source of this issue is the `supervision` package, which is used in other projects from this course.
It may bring in 'opencv-python-headless' when installed via Poetry.

Recommended steps to avoid this issue:
1. Comment out its line in the `pyproject.toml` file.
2. If the virtual environment is already created and `supervision` was installed:
   - Remove the virtual environment (e.g., `rm -rf .venv`)
   - Comment out the `supervision` dependency in `pyproject.toml`
   - Run `poetry install` again to recreate the environment without installing `opencv-python-headless`.

Usage:
    python identificar_cor.py -i <video_file>

Arguments:
    -i (--image): Path to the video file.

Example:
    python identificar_cor.py -i video.mp4
"""
import argparse
import cv2
import numpy as np

# Inicializa a lista de amostras
samples = []

# Variável global para o frame atual (vai ser atualizado no loop)
frame = None

def callback(event, x, y, flags, param):
    global frame, samples
    if event == cv2.EVENT_LBUTTONDOWN:
        blue = frame[y, x, 0]
        green = frame[y, x, 1]
        red = frame[y, x, 2]
        samples.append([blue, green, red])
        lower_bound = np.amin(samples, axis=0)
        upper_bound = np.amax(samples, axis=0)
        print(f'Lower bound: {lower_bound}')
        print(f'Upper bound: {upper_bound}')
        text = f'B: {blue}, G: {green}, R: {red}'
        cv2.putText(frame, text, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
        cv2.imshow('image', frame)

def main():
    global frame

    parser = argparse.ArgumentParser(description='Script para extrair cores RGB de um video.')
    parser.add_argument('-i', '--image', help='Caminho para o video.', required=True)
    args = parser.parse_args()

    cap = cv2.VideoCapture(args.image)
    if not cap.isOpened():
        print(f'Não foi possível abrir o video: {args.image}')
        exit(1)

    cv2.namedWindow('image')
    cv2.setMouseCallback('image', callback)

    while True:
        ret, frame = cap.read()
        if not ret:
            print('Fim do vídeo ou erro na leitura do frame.')
            break

        cv2.imshow('image', frame)
        key = cv2.waitKey(3) & 0xFF  # 30ms delay para vídeo mais fluido
        if key == ord('q') or key == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
