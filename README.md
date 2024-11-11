# Computer Vision Preprocessing Module for Drone-based Landmine Detection

### Project Overview
# =================
 This project is part of a broader system designed for landmine detection using a drone. 
 The drone autonomously captures images at specified GPS coordinates, and this module 
 preprocesses those images for further analysis using computer vision techniques. 
 This preprocessing pipeline is designed to be modular, enabling future development 
 of more sophisticated computer vision capabilities.

### Features
 ========
 The initial Minimum Viable Product (MVP) for this system includes the following:
 - Image Preprocessing: Resizes images to a standard 640x640 resolution, removes EXIF data 
   that may cause incorrect orientation, and converts images to grayscale for consistent processing.
 - Modular Design: Built with future extensions in mind, allowing easy integration of more 
   complex preprocessing steps and models.
 - Testing: Includes tests to validate image resizing and preprocessing steps.

### Installation
 ============
#### Prerequisites
 -------------
 Ensure you have Python 3.7+ installed along with the required libraries.

 1. Clone the Repository:
    ```
    git clone https://github.com/your-username/your-repo-name.git
    cd your-repo-name
    ```

 2. Set Up a Virtual Environment:
    ```
    python -m venv 3yp-venv
    source 3yp-venv/bin/activate  # On Windows use: .\3yp-venv\Scripts\activate
    ```

 3. Install Dependencies:
    ```
    pip install -r requirements.txt
    ```

#### Dependencies
 ------------
 - OpenCV: For image loading, resizing, and display.
 - Pillow (PIL): For removing EXIF data from images.
 - NumPy: For image manipulation and handling.

### Usage
 =====

#### Example
 -------
 Here’s a quick example of how to use the `PreProcessedImage` class to preprocess an image:

```python
from image_preprocessing import PreProcessedImage

# Load and preprocess the image
 image_path = "path/to/your/image.jpg"
 preprocessed_image = PreProcessedImage(image_path)
 processed_img = preprocessed_image.preprocess_image()

 # Display the processed image
 preprocessed_image.show_processed_image()
 ```

### Classes and Methods
 ===================

#### `PreProcessedImage`
 -------------------
 A class that handles image preprocessing, including resizing, EXIF data removal, and grayscale conversion.

 - `__init__(image_path, target_size=(640, 640))`: Initializes the class with the image path and target size for resizing.
 - `resize_image()`: Resizes the image to the target size.
 - `remove_exif_data()`: Removes orientation data from the image.
 - `convert_to_grayscale()`: Converts the image to grayscale.
 - `preprocess_image()`: Runs all preprocessing steps.