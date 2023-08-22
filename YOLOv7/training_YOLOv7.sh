#!/bin/bash
# tiny model
python train.py --workers 8 --device 0 --epochs 100 --save_period 10 --batch-size 16 --data data/config_sheep.yaml --img 640 640 --cfg cfg/training/yolov7-tiny_custom.yaml --weights 'yolov7-tiny.pt' --name tiny --hyp data/hyp.scratch.custom.yaml
# normal model
python train.py --workers 8 --device 0 --epochs 100 --save_period 10 --batch-size 12 --data data/config_sheep.yaml --img 640 640 --cfg cfg/training/yolov7_custom.yaml --weights 'yolov7_training.pt' --name medium --hyp data/hyp.scratch.custom.yaml
# large model
python train.py --workers 8 --device 0 --epochs 100 --save_period 10 --batch-size 8 --data data/config_sheep.yaml --img 640 640 --cfg cfg/training/yolov7x_custom.yaml --weights 'yolov7x_training.pt' --name large --hyp data/hyp.scratch.custom.yaml
