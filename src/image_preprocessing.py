from PIL import Image
import numpy as np
import cv2

class PreProcessedImage:
    def __init__(self, image_path, target_size=(640, 640)):
        """
        Initializes the PreProcessedImage Class.

        Args:
            image_path (str): Path to the image file. The image should be a .jpg file.
            target_size (tuple, optional): Desired size (width, height) to resize the image to. Defaults to (640, 640).
        """
        self.image_path = image_path
        self.target_size = target_size
        self.image = self.remove_exif_data()  # Remove EXIF and load image directly

    def resize_image(self):
        """Resize an image to the target size."""
        self.image = cv2.resize(self.image, self.target_size)
        return self.image

    def remove_exif_data(self):
        """Load an image with EXIF data removed."""
        with Image.open(self.image_path) as img:
            img = img.convert("RGB")  # Removing EXIF by converting to RGB
        return cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

    def convert_to_grayscale(self):
        """Convert the image to grayscale."""
        self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        return self.image

    def preprocess_image(self):
        """Run all preprocessing steps and return the final processed image."""
        self.resize_image()
        self.convert_to_grayscale()
        return self.image


class TestPreProcessedImage:
    def __init__(self, image_path, target_size=(640, 640)):
        """
        Initializes the TestPreProcessedImage Class.

        Args:
            image_path (str): Path to the image file.
            target_size (tuple, optional): Target size (width, height) for resizing. Defaults to (640, 640).
        """
        self.image_path = image_path
        self.target_size = target_size

    def test_resize_image(self):
        """Check that the resized image is the target size."""
        preprocessed_image = PreProcessedImage(self.image_path, self.target_size)
        resized_image = preprocessed_image.resize_image()
        assert resized_image.shape[:2] == self.target_size, "Resized image dimensions do not match target size."

    def show_processing(self):
        """Display the original and processed images side by side with padding if needed."""
        # Load the original image
        original_image = cv2.imread(self.image_path)

        # Preprocess the image
        preprocessed_image = PreProcessedImage(self.image_path, self.target_size)
        processed_image = preprocessed_image.preprocess_image()

        # Convert processed image to BGR for consistency in display
        if len(processed_image.shape) == 2:  # Check if grayscale
            processed_image = cv2.cvtColor(processed_image, cv2.COLOR_GRAY2BGR)

        # Get heights and widths of both images
        original_height, original_width = original_image.shape[:2]
        processed_height, processed_width = processed_image.shape[:2]

        # Determine the maximum height and width for padding
        max_height = max(original_height, processed_height)
        max_width = max(original_width, processed_width)

        # Add padding to the original image
        top_pad = (max_height - original_height) // 2
        bottom_pad = max_height - original_height - top_pad
        left_pad = (max_width - original_width) // 2
        right_pad = max_width - original_width - left_pad
        padded_original = cv2.copyMakeBorder(
            original_image, top_pad, bottom_pad, left_pad, right_pad, cv2.BORDER_CONSTANT, value=(0, 0, 0)
        )

        # Add padding to the processed image
        top_pad = (max_height - processed_height) // 2
        bottom_pad = max_height - processed_height - top_pad
        left_pad = (max_width - processed_width) // 2
        right_pad = max_width - processed_width - left_pad
        padded_processed = cv2.copyMakeBorder(
            processed_image, top_pad, bottom_pad, left_pad, right_pad, cv2.BORDER_CONSTANT, value=(0, 0, 0)
        )

        # Stack the images side by side
        combined_image = np.hstack((padded_original, padded_processed))

        # Display the combined image
        cv2.imshow("Original and Processed Images with Padding", combined_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

