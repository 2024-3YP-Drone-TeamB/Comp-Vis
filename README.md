# Computer Vision Preprocessing Module for Drone-based Landmine Detection

### Project Overview
# =================
 This project is part of a broader system designed for landmine detection using a drone. This code base is concerned with the computer vision required for detecting landmines. The aim of this work is to be able to fuse a range of different sensor data, and give robust and reliable predictions for the location of landmines.

### Version 1.01 
#### Author - Rory Millard UNIV 11/11/24

This version only includes the image preprocessing pipeline for thermographic images to ensure:
    - Images are resized to640x640
    - Images are grayscale
    - Images dont contain EXIF data

#### Whats new?

 - Included this readme.md file
 - Created the image_preprocessing module
     - This module includes the PreProcessedImage Class
     - This module includes the TestPreProcessedImage Class
 - Created the testing.py file to implement testing of aspects of the codebase
