import tensorflow as tf
import os
import scipy

pic_path = "/home/c/workspace/tf_models/research/SteelDetection/test_img"
dirs = os.listdir(pic_path)
count = 0
for filename in dirs:
        count = count + 1
        im = tf.gfile.FastGFile(os.path.join(pic_path, filename), 'rb').read()
        print("processing %d pic"%count)
        with tf.Session() as sess:
            img_data = tf.image.decode_jpeg(im)
            image_float = tf.image.convert_image_dtype(img_data, tf.float32)
            resized = tf.image.resize_images(image_float, [640, 640], method=3)
            resized_im = resized.eval()
            # new_mat = np.asarray(resized_im).reshape(1, 64, 64, 3)
            scipy.misc.imsave(os.path.join(pic_path, filename),resized_im)

