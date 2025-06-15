"""
This script replaces the green background in a video (chroma key) with a selected background video or image.

Usage:
    python projeto_01.py -i <input_video> -b <background_video_or_image>

Arguments:
    -i, --input        Path to the input video with green background.
    -b, --background   Path to the background video or image that will replace the green background.

The script processes the input video frame by frame, identifying green pixels using a specified color range.
It then overlays those areas with the corresponding pixels from the background video or image. The result is a new
real-time video stream where the original green background is continuously replaced.

Press 'q' while the output window is in focus to exit the program.

Example:
    python 01_01_01_Virtual_Scenarios.py -i "data/webcam.mp4" -b "data/praia.mp4"
"""

import argparse
import cv2
import numpy as np

# Set up argparse
parser = argparse.ArgumentParser(
    description='Script to replace a green background with a chosen image or video.'
)
parser.add_argument(
    '-i',
    '--input',
    help='Path to the video with green background.',
    required=True,
)
parser.add_argument(
    '-b', '--background', help='Path to the background video or image.', required=True
)
args = parser.parse_args()

# Load both videos
cap_webcam = cv2.VideoCapture(args.input)
cap_praia = cv2.VideoCapture(args.background)

# Main loop
while True:
    # Read one frame from each video
    ret_webcam, frame_webcam = cap_webcam.read()
    ret_praia, frame_praia = cap_praia.read()

    # Check if either video has ended
    if not ret_webcam or not ret_praia:
        break

    # Define green color range in RGB
    lower_green = np.array([0, 100, 0], dtype=np.uint8)
    upper_green = np.array([100, 255, 100], dtype=np.uint8)

    # Create a mask with pixels inside the green color range
    mask = cv2.inRange(frame_webcam, lower_green, upper_green)

    # Use the mask to extract the corresponding background pixels from the beach video
    praia_background = cv2.bitwise_and(frame_praia, frame_praia, mask=mask)

    # Invert the mask to get pixels outside the green color range
    mask_inv = np.invert(mask)

    # Use the inverted mask to extract non-green pixels from the webcam video
    webcam_foreground = cv2.bitwise_and(
        frame_webcam, frame_webcam, mask=mask_inv
    )

    # Combine the webcam foreground with the beach background
    result = cv2.addWeighted(praia_background, 1, webcam_foreground, 1, 0)

    # Display the result
    cv2.imshow('Result', result)

    # Check if the 'q' key was pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the captures and close all windows
cap_webcam.release()
cap_praia.release()
cv2.destroyAllWindows()


