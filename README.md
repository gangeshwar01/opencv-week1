# opencv-week1
# OpenCV Week 1 🚀

This repository contains all the notes, code exercises, and research from a one-week intensive self-study program focused on the fundamentals of OpenCV and computer vision. The objective was to gain a foundational understanding of the library's core modules, key concepts, and practical applications.

---

## 📚 Topics Covered

-   **Introduction to OpenCV:** History, installation, and basic setup.
-   **Core Functionality (`core`):** Understanding that OpenCV images are NumPy arrays, basic array operations (slicing, channels), and the BGR color format.
-   **Image Processing (`imgproc`):** Color space conversions (Grayscale, HSV), geometric transformations, filtering (blurring, sharpening), thresholding, and edge detection (Canny).
-   **I/O & GUI (`imgcodecs`, `videoio`, `highgui`):** Reading/writing images, capturing video from a camera, and displaying images and video streams.
-   **Object Detection (`objdetect`):** Introduction to Haar Cascades for face detection.
-   **Image Processing Theory:** Fundamentals of pixels, color spaces, convolution, and filtering.

---

## 📂 Repository Structure

The repository is organized to separate notes, code, and research for clarity.

.
├── README.md           # This overview file
├── requirements.txt    # Python dependencies for the project
├── exercises/          # Directory for all practical Python scripts
│   ├── 01_image_basics.py
│   ├── 02_drawing_and_writing.py
│   └── 03_live_camera_feed.py
├── notes/              # Markdown notes summarizing key concepts
│   ├── 01_core_and_datastructures.md
│   ├── 02_imgproc_basics.md
│   └── 03_io_and_gui.md
├── research/           # Summaries of investigated topics
│   └── research_summary.md
└── report/             # The final comprehensive report in PDF format
└── opencv_week1_report.pdf


---

## 🛠️ Setup and Usage

To run the exercises in this repository, follow these steps.

### Prerequisites

-   Python 3.8+
-   A webcam (for the live camera feed exercise)

### Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/](https://github.com/)<your-username>/opencv-week1.git
    cd opencv-week1
    ```

2.  **Create and activate a virtual environment (recommended):**
    ```bash
    python -m venv venv
    # On Windows
    venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```

3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

### Running the Exercises

Navigate to the `exercises` directory and run any of the Python scripts. Make sure you have an image named `test_image.jpg` in the root directory or update the image path in the scripts.

```bash
python exercises/01_image_basics.py
