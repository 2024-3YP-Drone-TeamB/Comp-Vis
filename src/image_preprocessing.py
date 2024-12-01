from PIL import Image
import numpy as np
import cv2

class PreProcessor:
    """Class for preprocessing images. Automatically removes EXIF data and loads images in BGR format as a numpy array."""
    def __init__(self, image_path, target_size=(640, 640)):
        """
        Initializes the PreProcessor Class.

        Args:
            image_path (str): Path to the image file. The image should be a .jpg file.
            target_size (tuple, optional): Desired size (width, height) to resize the image to. Defaults to (640, 640).
            Ensures that the exif data is removed from the image and loads the image in BGR, numpy array format.
        """
        self.image_path = image_path
        self.target_size = target_size
        self.image = self.load_image_without_exif()

    def load_image_without_exif(self):
        """Loads an image with EXIF data removed. Return the image in BGR format, as a numpy array."""
        img = Image.open(self.image_path).convert("RGB")  # Convert to RGB to remove EXIF
        return cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)  # Convert to BGR for OpenCV compatibility

    def resize_image(self):
        """Resize the image to the target size."""
        return cv2.resize(self.image, self.target_size)

    def convert_to_grayscale(self):
        """Convert the image to grayscale."""
        return cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)


class TestPreProcessor:
    def __init__(self, image_path, target_size=(640, 640)):
        """
        Initializes the TestPreProcessor Class.

        Args:
            image_path (str): Path to the image file.
            target_size (tuple, optional): Target size (width, height) for resizing. Defaults to (640, 640).
        """
        self.image_path = image_path
        self.target_size = target_size

    def test_resize_image(self):
        """Check that the resized image is the target size."""
        preprocessed_image = PreProcessor(self.image_path, self.target_size)
        resized_image = preprocessed_image.resize_image()
        assert resized_image.shape[:2] == self.target_size, "Resized image dimensions do not match target size."

    def show_processing(self):
        """Display the original and processed images side by side with padding if needed."""
        # Load the original image
        original_image = cv2.imread(self.image_path)

        # Preprocess the image
        preprocessed_image = PreProcessor(self.image_path, self.target_size)
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
        
class ThermalImagePreProcessor(PreProcessor):
    """Inherits from PreProcessor Class and adds thermal image specific preprocessing methods."""
    def __init__(self, image_path, target_size=(640,640), temperature_range=(0, 40)):
        super().__init__(image_path, target_size)
        self.temperature_range = temperature_range
        self.image = cv2.imread(self.image_path)

    def temperature_normalization(self, image):
        
        # TODO: Implement temperature normalisation
        
        pass

    def show_processing(self):
        """Display the original and processed images side by side with padding if needed."""
        # Load the original image
        original_image = cv2.imread(self.image_path)

        # Convert the preprocessed image to grayscale and resize it
        processed_image = self.convert_to_grayscale()
        processed_image = cv2.resize(processed_image, self.target_size)

        # Convert processed image to BGR for consistent display in color
        processed_image = cv2.cvtColor(processed_image, cv2.COLOR_GRAY2BGR)

        # Get heights and widths of both images
        original_height, original_width = original_image.shape[:2]
        processed_height, processed_width = processed_image.shape[:2]

        # Determine the maximum height and width for padding
        max_height = max(original_height, processed_height)
        max_width = max(original_width, processed_width)

        # Function to pad images to the same size
        def pad_image(img, target_height, target_width):
            top_pad = (target_height - img.shape[0]) // 2
            bottom_pad = target_height - img.shape[0] - top_pad
            left_pad = (target_width - img.shape[1]) // 2
            right_pad = target_width - img.shape[1] - left_pad
            return cv2.copyMakeBorder(img, top_pad, bottom_pad, left_pad, right_pad, cv2.BORDER_CONSTANT, value=(0, 0, 0))

        # Pad original and processed images to have the same dimensions
        padded_original = pad_image(original_image, max_height, max_width)
        padded_processed = pad_image(processed_image, max_height, max_width)

        # Stack the images side by side
        combined_image = np.hstack((padded_original, padded_processed))

        # Display the combined image
        cv2.imshow("Original and Processed Images with Padding", combined_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
