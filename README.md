# Computer Vision Preprocessing Module for Drone-based Landmine Detection

### Project Overview
# =================
 This project is part of a broader system designed for landmine detection using a drone. This code base is concerned with the computer vision required for detecting landmines. The aim of this work is to be able to fuse a range of different sensor data, and give robust and reliable predictions for the location of landmines.

### Version 1.03 
#### Author - Rory Millard UNIV 1/12/24

    This version includes a newer trained model, and the image processing pipeline
         - Predicted images in predicted_images folder
         - Images are resized to 640x640
         - Images are grayscale
         - Images dont contain EXIF data
         - Thermal image CV models are in src/models/

#### Whats new?

 - Trained a YOLOv11 large model on a 100% of the data, in google coalb with an Nvidia T4 GPU
 - the trained model is in src\models\yolov11_large_custom_ver02.pt
 - Added the training files of the two models - 'Model 1 Training' and 'Model 2 Training'.
   The files contain all the relevant training graphs, files and stats
 - Also added the google colab notebooks used for training in notebooks/

