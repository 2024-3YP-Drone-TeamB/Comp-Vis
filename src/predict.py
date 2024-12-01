"""
Landmine Detection Drone System - Main Application

This file serves as the central orchestration point for the drone-based 
landmine detection system, integrating computer vision, geospatial analysis, 
and risk mapping technologies.

This version is designed to be used for a single drone, with a thermal camera.
It is assumed that there is some level of preprocessing of the raw sensor data (sufficient contrast enhancement etc.)
However no accurate thermographic calibration is assumed

Author: [Rory Millard - University College, Oxford]
Created: [1/12/2024]
Version: 0.1.0
"""



#Import relevant modules
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
import cv2
from ultralytics import YOLO
import json


from image_preprocessing import ThermalImagePreProcessor

#Define file paths
drone_data_path = r"data\mission_XXX\run_001" #Data from the drone. see README for details
results_data_path = r"results\mission_XXX" #

#Load the PRETRAINED YOLO model 
model = YOLO(r'C:\Users\RMill\OneDrive - Nexus365\Documents\Oxford\Engineering Work\Year 3\B3 - 3YP\Comp Vis\src\models\yolov11_large_custom_ver02.pt')

#If it is not already there, create a folder to store the results
if not os.path.exists(results_data_path):
    os.makedirs(results_data_path)
    
#Find how many images we have
number_of_images = int(len(os.listdir(drone_data_path)) / 2 )#Divide by 2 as we have a a .jpg and .json for each image. Integer vaiue

#Create folders for the processed images, and the updated JSON files with predictions
#If it is not already there, create a folder to store the results

prediction_json_path = os.path.join(results_data_path, 'json')  
processed_image_path = os.path.join(results_data_path, 'processed_images')  

#DO NOT CONFUSE "processed_image_path" with "processed_image_paths" - the former is the path to the folder, the latter is a list of paths to the images

processed_image_paths = [os.path.join(processed_image_path, 'IMG' + f'_{i}.jpg') for i in range(1, number_of_images + 1)]  
old_json_paths = [os.path.join(drone_data_path, 'IMG_' + f'{i}.json') for i in range(1, number_of_images + 1)] 
prediction_json_paths = [os.path.join(prediction_json_path, 'IMG' + f'_{i}.json') for i in range(1, number_of_images + 1)]

#If it is not already there, create a folder to store the jsons that are updated with predictions
if not os.path.exists(prediction_json_path):
    os.makedirs(prediction_json_path)
    
#If it is not already there, create a folder to store the processed images
if not os.path.exists(processed_image_path):
    os.makedirs(processed_image_path)
    
    
#For each image, pass it through the preprocessing code
for image_index in range(number_of_images):
    
    #Load the image. We have to do this in a slightly convoluted way as the images are not numbered sequentially
    
    image_index += 1 #We start at 1, not 0

    temp_image_path = drone_data_path + rf"\IMG_{image_index}.jpg"

    
    #Run the preprocessing code
    temp_processed_image = ThermalImagePreProcessor(temp_image_path, target_size = (640,640))
    temp_processed_image.image = temp_processed_image.resize_image()
    temp_processed_image.image = temp_processed_image.convert_to_grayscale()
    
    #Save the processed image

    cv2.imwrite(processed_image_paths[image_index-1], temp_processed_image.image)

    
    # cv2.imshow("Visualisation" , temp_processed_image.image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

#soft Copy all of the json files from data to results to be updated

for image_index in range(number_of_images):
        
    #Copy the json file to the results folder
    os.system(f'copy {old_json_paths[image_index]} {prediction_json_path}')

inference_results = model(processed_image_paths, # A list of image paths
                          show=False,
                          verbose=False)




# Iterate over inference results and update JSON files
for result_index, result in enumerate(inference_results):
    # Extract bounding boxes (xyxyn) and probabilities
    boxes = result.boxes.xyxyn.cpu().numpy()  # Convert to numpy for easier manipulation
    probs = result.boxes.conf.cpu().numpy()  # Extract probabilities
    
    
    

    
    # Load the json file from drone_data_path. Every second file is a json file
    with open(prediction_json_paths[result_index], 'r') as f:
        json_data = json.load(f)
    

    # Update the JSON file with detection results
    json_data['bounding_boxes'] = boxes.tolist()  # Convert numpy array to list
    json_data['probabilities'] = probs.tolist()  # Convert numpy array to list

    # Save the updated JSON data
    with open(prediction_json_paths[result_index], 'w') as f:
        json.dump(json_data, f, indent=4)

print(f"Updated JSON files are saved in {prediction_json_path}")