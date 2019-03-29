import cv2
import numpy as np
import tensorflow as tf
from object_detection.utils import label_map_util
from object_detection.utils import visualization_utils as vis_util
import csv
import os


class TOD(object):
    def __init__(self):
        self.PATH_TO_CKPT = r'/home/c/workspace/tf_models/research/SteelDetection/results_android20190205/frozen/frozen_inference_graph.pb'
        self.PATH_TO_LABELS = r'/home/c/workspace/tf_models/research/SteelDetection/steel_label_for_fasterrcnn.pbtxt'
        self.NUM_CLASSES = 4
        # self.PATH_TO_CKPT = r'/home/c/workspace/tf_models/research/object_detection/faster_rcnn_inception_resnet_v2_atrous_oid_2018_01_28/frozen_inference_graph.pb'
        # self.PATH_TO_LABELS = r'/home/c/workspace/tf_models/research/object_detection/data/oid_bbox_trainable_label_map.pbtxt'
        # self.NUM_CLASSES = 546
        self.detection_graph = self._load_model()
        self.category_index = self._load_label_map()

    def _load_model(self):
        detection_graph = tf.Graph()
        with detection_graph.as_default():
            od_graph_def = tf.GraphDef()
            with tf.gfile.GFile(self.PATH_TO_CKPT, 'rb') as fid:
                serialized_graph = fid.read()
                od_graph_def.ParseFromString(serialized_graph)
                tf.import_graph_def(od_graph_def, name='')
        return detection_graph

    def _load_label_map(self):
        label_map = label_map_util.load_labelmap(self.PATH_TO_LABELS)
        categories = label_map_util.convert_label_map_to_categories(label_map,
                                                                    max_num_classes=self.NUM_CLASSES,
                                                                    use_display_name=True)
        category_index = label_map_util.create_category_index(categories)
        return category_index
    def detect(self, image):
        with self.detection_graph.as_default():
            with tf.Session(graph=self.detection_graph) as sess:
                # Expand dimensions since the model expects images to have shape: [1, None, None, 3]
                image_np_expanded = np.expand_dims(image, axis=0)
                image_tensor = self.detection_graph.get_tensor_by_name('image_tensor:0')
                boxes = self.detection_graph.get_tensor_by_name('detection_boxes:0')
                scores = self.detection_graph.get_tensor_by_name('detection_scores:0')
                classes = self.detection_graph.get_tensor_by_name('detection_classes:0')
                num_detections = self.detection_graph.get_tensor_by_name('num_detections:0')
                # Actual detection.
                (boxes, scores, classes, num_detections) = sess.run(
                    [boxes, scores, classes, num_detections],
                    feed_dict={image_tensor: image_np_expanded})
                # Visualization of the results of a detection.
                Image = vis_util.visualize_boxes_and_labels_on_image_array(
                    image,
                    np.squeeze(boxes),
                    np.squeeze(classes).astype(np.int32),
                    np.squeeze(scores),
                    self.category_index,
                    use_normalized_coordinates=True,
                    min_score_thresh=.4)
                count = 0
                for index, value in enumerate(scores):
                    for index, values in enumerate(value):
                        if values >= 0.4:
                            count = count + 1
                print('the count of objects is: ', count) 
        # cv2.namedWindow("detection", cv2.WINDOW_NORMAL)
        # cv2.imshow("detection", Image)
        # cv2.waitKey(0)

if __name__ == '__main__':
    img_path = '/home/c/workspace/tf_models/research/SteelDetection/train_data/img'
    csv_path = '/home/c/workspace/tf_models/research/SteelDetection/train_data/nas_train_data_4.csv'
    f = os.listdir(img_path)
    for files in f:
        print(files)
        tmp_path = os.path.join(img_path, files)
        image = cv2.imread(tmp_path)
        detecotr = TOD()
        detecotr.detect(image)
        csv_reader = csv.reader(open(csv_path,'r')) 
        true_num = 0
        for lines in csv_reader:
            if lines[0] == files:
               true_num = true_num + 1
        print('the real count of object is: ', true_num)

