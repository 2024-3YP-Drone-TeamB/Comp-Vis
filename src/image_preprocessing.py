
from PIL import Image
import numpy as np
import cv2
import os
import glob



class ImagePreprocessing:
    
    def __init__(self, image_path, target_size = (640, 640)):
        """
        Initializes the ImagePreprocessing class.

        Args:
            image_path (str): Path to the image file.
            target_size (tuple, optional): Desired size (width, height) to resize the image to. Defaults to (640, 640).
            mode (str, optional): Preprocessing mode. Can be "grayscale", "rgb", or a custom function. Defaults to "grayscale".
        """ 
        self.image_path = image_path
        self.image = cv2.imread(image_path)
        self.target_size = target_size
    
    def resize_image(self):
        """Resize an image to the target size while preserving aspect ratio."""
        self.image = cv2.resize(self.image, self.target_size)
        return self.image
    
    def remove_exif_data(self):
        """Remove EXIF data from an image."""
        with Image.open(self.image_path) as img:
            img = img.convert("RGB")
            return cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
        
    def convert_to_grayscale(self):
        """Convert an image to grayscale."""
        return cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
    
    def preprocess_image(self):
        """Preprocess an image by resizing it, removing EXIF data, and converting it to grayscale.
        Args:   
            image_path (str): Path to the image file.
            target_size (tuple, optional): Desired size (width, height) to resize the image to. Defaults to (640, 640).
        Output:
            np.array: Preprocessed image.   
        
        """
        self.resize_image()
        self.remove_exif_data()
        return self.convert_to_grayscale()

    


