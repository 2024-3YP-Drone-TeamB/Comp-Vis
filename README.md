# Computer Vision Preprocessing Module for Drone-based Landmine Detection

### Project Overview
# =================
 This project is part of a broader system designed for landmine detection using a drone. This code base is concerned with the computer vision required for detecting landmines. The aim of this work is to be able to fuse a range of different sensor data, and give robust and reliable predictions for the location of landmines.

### Version 1.02 
#### Author - Rory Millard UNIV 17/11/24

    This version includes a trained model, and the image processing pipeline
         - Predicted images in predicted_images folder
         - Images are resized to 640x640
         - Images are grayscale
         - Images dont contain EXIF data

#### Whats new?

 - Trained a YOLOv11 nano model on a 20% subset of the data, in google colab with T4 GPU
 - Predicted images in predicted_images folder
 - Wrote an evaluation script
 - the trained model is in src\models\yolov11_custom_ver01.pt

