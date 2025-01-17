import os
os.chdir("/data/embryo/tfrecords/yolov3-tf2")

os.system("python detect_SK.py \
--classes /data/embryo/random/classes.txt \
--weights /data/embryo/tfrecords/nick_model/yolov3-tf2/checkpoints/yolov3_best_model.tf \
--size 416 \
--output /data/embryo/tfrecords/nick_model/1241/detections_416/ \
--num_classes 2 \
--img_dir /data/embryo/tfrecords/test/")
