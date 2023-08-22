#!/bin/bash
python tools/train.py --batch 16 --conf configs/yolov6n_finetune.py --data data/config_v6.yaml --fuse_ab --device 0 --epochs 100 --img-size 640 --name nano --eval-interval 1

python tools/train.py --batch 14 --conf configs/yolov6s_finetune.py --data data/config_v6.yaml --fuse_ab --device 0 --epochs 100 --img-size 640 --name small --eval-interval 1

python tools/train.py --batch 12 --conf configs/yolov6m_finetune.py --data data/config_v6.yaml --fuse_ab --device 0 --epochs 100 --img-size 640 --name medium --eval-interval 1

python tools/train.py --batch 8 --conf configs/yolov6l_finetune.py --data data/config_v6.yaml --fuse_ab --device 0 --epochs 100 --img-size 640 --name large --eval-interval 1