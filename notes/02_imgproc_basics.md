Topic: Image Processing (imgproc module)
This module contains the majority of image manipulation functions.

Color Space Conversion:

cv2.cvtColor(image, flag) is the key function.

Grayscale (cv2.COLOR_BGR2GRAY): Simplifies the image. Essential for many algorithms that don't need color information, like Canny edge detection.

HSV (cv2.COLOR_BGR2HSV): Hue, Saturation, Value. Very useful for object detection based on color, as Hue is more robust to lighting changes than BGR values.

Geometric Transformations:

Scaling: cv2.resize() to change an image's dimensions.

Translation: Shifting an image's location. Requires creating a transformation matrix M.

Rotation: Rotating an image. Use cv2.getRotationMatrix2D() to create the matrix, then apply it with cv2.warpAffine().

Image Filtering (Convolution):

Concept: A kernel (a small matrix) is slid across the image. The pixel values in the kernel's window are combined to produce a new value for the central pixel. This is called convolution.

Blurring / Smoothing: Used to reduce noise. cv2.GaussianBlur(image, (kernel_size), 0) is the most common method. The kernel size must be odd numbers, e.g., (5, 5).

Edge Detection: Aims to find boundaries in an image. The Canny edge detector (cv2.Canny()) is a popular multi-stage algorithm that produces clean, thin edges.
