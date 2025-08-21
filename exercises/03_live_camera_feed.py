# exercises/03_live_camera_feed.py

import cv2

def main():
    """
    Captures video from the default webcam, converts it to grayscale,
    and displays it in real-time.
    """
    # Initialize video capture from the default camera (usually index 0).
    cap = cv2.VideoCapture(0)

    # Check if the webcam is opened correctly.
    if not cap.isOpened():
        print("Error: Cannot open camera.")
        return

    print("Camera feed is active. Press 'q' to quit.")

    # Loop to continuously get frames from the camera.
    while True:
        # Read a frame from the camera.
        # 'ret' is a boolean that is True if the frame was read successfully.
        # 'frame' is the captured image frame.
        ret, frame = cap.read()

        # If 'ret' is False, it means there was a problem (e.g., camera disconnected).
        if not ret:
            print("Error: Can't receive frame. Exiting...")
            break

        # Convert the captured frame to grayscale.
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Display the original color frame.
        cv2.imshow('Live Camera Feed (Color)', frame)

        # Display the grayscale frame.
        cv2.imshow('Live Camera Feed (Grayscale)', gray_frame)

        # Wait for 1 millisecond and check if the 'q' key was pressed.
        # cv2.waitKey(1) is crucial for rendering the video frames.
        # 0xFF == ord('q') is a platform-independent way to check for the key press.
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything is done, release the capture object and destroy windows.
    cap.release()
    cv2.destroyAllWindows()
    print("Camera feed stopped.")

if __name__ == '__main__':
    main()
