import image_preprocessing

not_landmine_image_path = r"C:\Users\RMill\OneDrive - Nexus365\Documents\Oxford\Engineering Work\Year 3\B3 - 3YP\Comp Vis\data\not_landmine_images\800600.jpg"
ThermalImage = image_preprocessing.ThermalImagePreProcessor(not_landmine_image_path)

ThermalImage.show_processing()




