# exercises/01_image_basics.py

import cv2
import numpy as np

def main():
    """
    Demonstrates basic OpenCV operations: loading, color conversion,
    blurring, and displaying an image.
    """
    # Define the path to your image.
    # Make sure you have an image file at this location.
    image_path = 'test_image.jpg'

    # 1. Read an image from disk.
    # The image is loaded as a NumPy array with BGR channel order.
    bgr_image = cv2.imread(image_path)

    # Always check if the image was loaded correctly.
    if bgr_image is None:
        print(f"Error: Could not read image from {image_path}")
        return

    # 2. Convert the image to grayscale.
    # This is a common preprocessing step for many computer vision tasks.
    gray_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2GRAY)

    # 3. Apply a Gaussian blur to the grayscale image.
    # This helps in reducing high-frequency noise. The kernel size (5, 5)
    # determines the amount of blur.
    blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

    # 4. Display the results in separate windows.
    cv2.imshow('Original BGR Image', bgr_image)
    cv2.imshow('Grayscale Image', gray_image)
    cv2.imshow('Blurred Image', blurred_image)

    # 5. Wait for a key press to close the windows.
    # waitKey(0) waits indefinitely. This is essential for the windows
    # to be displayed and responsive.
    print("Press any key to close all windows...")
    cv2.waitKey(0)

    # 6. Clean up and destroy all windows.
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
