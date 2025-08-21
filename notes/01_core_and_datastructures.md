Topic: Core Functionality & Basic Data Structures
The Golden Rule: The single most important concept is that an OpenCV image in Python is a NumPy array. This means you can use all of NumPy's powerful slicing, indexing, and math operations on images directly.

Image as an Array:

Grayscale Image: A 2D array of shape (height, width). Each element represents pixel intensity from 0 (black) to 255 (white).

Color Image: A 3D array of shape (height, width, channels). The channels dimension usually has a size of 3.

BGR Color Order 🎨:

By default, OpenCV reads color images in BGR (Blue, Green, Red) order.

This is a common "gotcha" because most other libraries (like Matplotlib) use RGB (Red, Green, Blue).

To convert, use: rgb_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2RGB).

Data Types:

The most common data type for images is uint8 (unsigned 8-bit integer), which holds values from 0 to 255.

For some calculations, you might need to convert to a floating-point type like float32 to avoid data overflow, and then convert back.

Basic Operations:

Accessing a Pixel: pixel = image[y, x]

Cropping (ROI - Region of Interest): This is just NumPy array slicing! roi = image[startY:endY, startX:endX]
