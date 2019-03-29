# Steel Detection  

## Table of Contents  

<!-- TOC -->

- [Steel Detection](#steel-detection)
    - [Table of Contents](#table-of-contents)
        - [Written in front](#written-in-front)
        - [References](#references)
        - [Main Dependencies](#main-dependencies)
        - [Usage](#usage)
            - [Installation](#installation)
            - [Datasets](#datasets)

<!-- /TOC -->

### Written in front  

As my Graduation Design, the project cost me almost 5 months to complete.5 months ago, i was new to deep learning and knew nothing about how to use TensorFlow to solve a computer vision problem. So at least, I'm quiet happy to conque the chanllage though the code of the project is mostly from the APIs supplied from TensoFlow Object Detection. Really appreciate the help of my friends and myriad articles on the Internet.  

### References  

[TensorFlow Object Detection API](https://github.com/tensorflow/models/tree/master/research/object_detection)  

### Main Dependencies  

The environment and dependencies of the project mainly includes:  

* **Python3.6.7**  
* **TensorFlow(>=1.12.0)**  
* **opencv**  
* **TensorFlow Object Detection API(0.1.0)**  

### Usage  

#### Installation  

For TensorFlow, run :  

    #For GPU (recommended)  
    pip3 install tensorflow-gpu  
    #For CPU  
    pip3 install tensorflow  

For more details of installation of TenosrFlow, you can visit [Tensorflow installation instructions](https://www.tensorflow.org/install/).  

For OpenCV, run :  

    pip3 install opencv-python  

For TensorFlow Object Detection :  

visit [TensorFlow Object Detection API Installation instructions](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/installation.md) for complete steps.  

#### Datasets  

The row datasets locate in [origin_img](https://github.com/JinshuChen/SteelDetection/tree/master/origin_img). There are nearly 200 pics in the folder and each picture has 100~300 steel of diffrent shapes. All the pictures came from different construction sites in Shanghai, which are all shot at **`random illumination environment`**. In fact, not all pics are proper for training. After selected, there remains about 80 pics with high-quality objections, which make up [the training datasets](https://github.com/JinshuChen/SteelDetection/tree/master/train_data), [the evaluation datasets](https://github.com/JinshuChen/SteelDetection/tree/master/eval_data) and [the test datasets](https://github.com/JinshuChen/SteelDetection/tree/master/test_data).  

The datasets contain 4 different shapes of steel, which are circle steel (circle_steel), triangle steel (sigma_steel), rectangle steel with two holes (THsquare_steel) and rectangle steel without holes (NHsquare_steel).  

<div align=center><img width="150" height="150" src="https://github.com/JinshuChen/SteelDetection/blob/master/presentation_img/D566A39B-594E-4ED0-BB01-1742F139C62A.png"/></div>
