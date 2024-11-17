from ultralytics import YOLO
import os
import random

#This script is used to evaluate the model on a set of 15 randomly chosen images from the test set, and save the results in the 'predicted_images' folder.
model = YOLO(r'C:\Users\RMill\OneDrive - Nexus365\Documents\Oxford\Engineering Work\Year 3\B3 - 3YP\Comp Vis\src\models\yolov11_custom_ver01.pt')  # Load model

# Get list of all image files in the directory
image_dir = r'C:\Users\RMill\OneDrive - Nexus365\Documents\Oxford\Engineering Work\Year 3\B3 - 3YP\Comp Vis\data\landmines_detection.v1i.yolov11\test\images'
image_files = [os.path.join(image_dir, f) for f in os.listdir(image_dir) if f.endswith('.jpg')]

# Select 15 random images
random_images = random.sample(image_files, 15)

# Predict and save results for each image
for i, image_path in enumerate(random_images, start=2):
    model.predict(source=image_path,
                    save=True,
                    show=True,
                    project="prediced_images", 
                    name=f"image{i}") 