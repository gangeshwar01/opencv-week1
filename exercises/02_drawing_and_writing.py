# exercises/02_drawing_and_writing.py

import cv2
import numpy as np

def main():
    """
    Demonstrates how to draw shapes and write text on an image.
    """
    # Create a blank black image (500x500 pixels, 3 color channels)
    # The data type is uint8, which is standard for images.
    canvas = np.zeros((500, 500, 3), dtype="uint8")

    # Draw a green rectangle.
    # Arguments: image, top-left corner, bottom-right corner, color (BGR), thickness.
    cv2.rectangle(canvas, (50, 50), (200, 200), (0, 255, 0), 3)

    # Draw a red circle.
    # Arguments: image, center coordinates, radius, color (BGR), thickness.
    # A thickness of -1 fills the shape.
    cv2.circle(canvas, (350, 125), 75, (0, 0, 255), -1)

    # Draw a blue line.
    # Arguments: image, start point, end point, color (BGR), thickness.
    cv2.line(canvas, (50, 300), (450, 450), (255, 0, 0), 5)

    # Write text on the canvas.
    # Arguments: image, text, bottom-left corner of text, font, font scale,
    # color (BGR), thickness, line type.
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(canvas, 'OpenCV Drawing', (50, 400), font, 1, (255, 255, 255), 2, cv2.LINE_AA)

    # Display the result.
    cv2.imshow('My Canvas', canvas)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
