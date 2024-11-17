from ultralytics import YOLO

# Load a YOLOv5 model
model = YOLO(r'C:\Users\RMill\OneDrive - Nexus365\Documents\Oxford\Engineering Work\Year 3\B3 - 3YP\Comp Vis\src\models\yolo11n.pt')  

# Train the model
results_subset_20 = model.train(data=r'C:\Users\RMill\OneDrive - Nexus365\Documents\Oxford\Engineering Work\Year 3\B3 - 3YP\Comp Vis\data\landmines_detection.v1i.yolov11\date_subset_.2.yaml',
                                epochs=100,
                                imgsz=640,
                                device="cpu")
