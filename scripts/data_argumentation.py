import os
from impy.ObjectDetectionDataset import *

# def main():
#  # Define the path to images and annotations
#  images_path = "/home/c/workspace/tf_models/research/SteelDetection/impy_train_data/circle_steel/img"
#  annotations_path = "/home/c/workspace/tf_models/research/SteelDetection/impy_train_data/circle_steel/annotations"
#  # Define the name of the dataset
#  dbName = "circle_steel"
#  # Create an object of ImageLocalizationDataset
#  imda = ObjectDetectionDataset(imagesDirectory = images_path, annotationsDirectory = annotations_path, databaseName = dbName)
#  # Reduce the dataset to smaller Rois of smaller ROIs of shape 1032x1032.
#  images_output_path = "/home/c/workspace/tf_models/research/SteelDetection/impy_train_data/circle_steel/img_adapted"
#  annotations_output_path = "/home/c/workspace/tf_models/research/SteelDetection/impy_train_data/circle_steel/annotations_adapted"
#  imda.reduceDatasetByRois(offset = [640, 640], outputImageDirectory = images_output_path, outputAnnotationDirectory = annotations_output_path)

# if __name__ == "__main__":
#  main()

def main():
 # Define the path to images and annotations
 images_path = "/home/c/workspace/tf_models/research/SteelDetection/impy_train_data/NHsquare_steel/img_adapted"
 annotations_path = "/home/c/workspace/tf_models/research/SteelDetection/impy_train_data/NHsquare_steel/annotations_adapted"
 # Define the name of the dataset
 dbName = "NHsquare_steel"
 # Create an object of ImageLocalizationDataset
 imda = ObjectDetectionDataset(imagesDirectory = images_path, annotationsDirectory = annotations_path, databaseName = dbName)
 # Apply data augmentation by using the following method of the ImageLocalizationDataset class.
 configuration_file = "/home/c/workspace/tf_models/research/SteelDetection/impy_train_data/config2.json"
 images_output_path = "/home/c/workspace/tf_models/research/SteelDetection/impy_train_data/NHsquare_steel/img_adapted"
 annotations_output_path = "/home/c/workspace/tf_models/research/SteelDetection/impy_train_data/NHsquare_steel/annotations_adapted"
 imda.applyDataAugmentation(configurationFile = configuration_file, outputImageDirectory = images_output_path, outputAnnotationDirectory = annotations_output_path)

if __name__ == "__main__":
 main()