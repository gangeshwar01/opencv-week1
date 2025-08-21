Topic: Application Utils (highgui, imgcodecs, videoio)
These modules handle getting data in and out of your program.

Reading and Writing Images (imgcodecs):

image = cv2.imread('path/to/image.jpg')

cv2.imwrite('path/to/save.png', image)

If imread fails (e.g., bad path), it returns None. Always check for this!

Displaying Images (highgui):

cv2.imshow('Window Name', image): Displays the image in a window. The window is identified by its name.

cv2.waitKey(delay): This is essential! It's not just a pause. It processes GUI events.

cv2.waitKey(0): Waits indefinitely until a key is pressed.

cv2.waitKey(1) (or any positive number): Waits for 1 millisecond. This is used inside loops to render frames of a video and check for user input. Without it, the imshow window will not update and may appear frozen.

cv2.destroyAllWindows(): Closes all windows created by OpenCV. Good practice to call this at the end of a script.

Working with Video (videoio):

To capture from a camera: cap = cv2.VideoCapture(0) (0 is usually the default webcam).

To read from a file: cap = cv2.VideoCapture('video.mp4').

The process is a loop:

Check if the capture is open: cap.isOpened().

Read a frame: ret, frame = cap.read(). ret is a boolean (True if a frame was read successfully).

Process the frame.

Display the frame.

Release the capture when done: cap.release()
