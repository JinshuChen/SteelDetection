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
            - [Training and evaluation](#training-and-evaluation)
            - [Test](#test)

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

The row datasets locate in [origin_img](https://github.com/JinshuChen/SteelDetection/tree/master/origin_img). There are nearly 200 pics in the folder and each picture has 100~300 steel of diffrent shapes. All the pictures came from different construction sites in Shanghai, which are all shot at **`random illumination environment`**. 

<div align=center><img width="600" height="350" src="https://github.com/JinshuChen/SteelDetection/blob/master/presentation_img/img2.png"/></div>

In fact, not all pics are proper for training. After selected, there remains about 80 pics with high-quality objections, which make up [the training datasets](https://github.com/JinshuChen/SteelDetection/tree/master/train_data), [the evaluation datasets](https://github.com/JinshuChen/SteelDetection/tree/master/eval_data) and [the test datasets](https://github.com/JinshuChen/SteelDetection/tree/master/test_data).  

The datasets contain 4 different shapes of steel, which are circle steel (circle_steel), triangle steel (sigma_steel), rectangle steel with two holes (THsquare_steel) and rectangle steel without holes (NHsquare_steel).  

<div align=center><img width="600" height="350" src="https://github.com/JinshuChen/SteelDetection/blob/master/presentation_img/img1.png"/></div>

**Note that** steel in `image e` and `image f` has pins inside, which means the interference to the detection model.

The classes of steel in training datasets dietributed as the following picture, which shows that the number of 4 classes and the defficulty of detection are positive correlated.

<div align=center><img width="600" height="350" src="https://github.com/JinshuChen/SteelDetection/blob/master/presentation_img/img3.png"/></div>

The annotations of the pics are done with the help of LabelImg, which are of PASCAL_VOC format. For the need of training, the annotations are converted into `.csv` and finally `.record`.

#### Training and evaluation

For training and evaluation, just run :  

    # From the SteelDetection/ directory
    python3 model_main.py
        --pipeline_config_path='YOUR_PIPELINE_CONFIG_PATH' \
        --model_dir='YOUR_MODEL_DIR' \
        --num_train_steps=YOUR_NUM_TRAIN_STEPS \
        --alsologtostderr

**Note that** the pipeline.config is very important because it assigns almost all the hyper-parameters and configs your training needs. Refers to [the API's proto settings](https://github.com/tensorflow/models/tree/master/research/object_detection/protos) to know what can you do to make your training more efficient.

To check the results at any time during the training, run :  

    tensorboard --logdir='YOUR_MODEL_DIR'

With tensorboard you can monitor all the metrics of the model and see the results of the model running on the eval datasets. Also you can monitor the metrics in your shell of course :sun_with_face:.

To make sure the GPU's occupation, run :  

    nvidia-smi -l

#### Test

For test, you may need [the frozen graph](https://github.com/JinshuChen/SteelDetection/blob/master/frozen_graph/frozen_inference_graph.pb) first. run :  

    # From the SteelDetection/scripts directory
    python3 export_inference_graph.py \
    --input_type=image_tensor \
    --pipeline_config_path='YOUR_PIPELINE_CONFIG_PATH' \
    --trained_checkpoint_prefix='YOUR_TRAINED_CKPT_PREFIX' \
    --output_directory='YOUR_EXPORT_DIR'

For test, run : 

    # From the SteelDetection/scripts directory
    python3 detection.py

Remeber to change the path and classes in the script.

Finally, if you are so lucky that you've trained such a pretty model as what I've got :laughing:, you'll get the results after you run the `detection.py` : 

<div align=center><img width="1000" height="350" src="https://github.com/JinshuChen/SteelDetection/blob/master/presentation_img/img4.png"/></div>

