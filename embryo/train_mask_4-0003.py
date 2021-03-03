#batch size 4
#lr 0.0003
import os
os.chdir("/data/embryo/models/research")

os.system("python object_detection/model_main_tf2.py \
--pipeline_config_path /data/embryo/models/research/model.config \
--model_dir /data/embryo/mask_rcnn/data/model-4-0003 \
--alsologtostderr")