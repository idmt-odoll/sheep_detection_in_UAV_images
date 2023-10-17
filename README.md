# Sheep Detection in UAV images
This is the official repo for the paper [**Comparison of Object Detection Algorithms for Livestock Monitoring of Sheep in UAV images**](https://github.com/idmt-odoll/sheep_detection_in_UAV_images/Comparison_of_Object_Detection_Algorithms_for_Livestock_Monitoring_of_Sheep_in_UAV_images.pdf) which will be presented on the 3rd Internation Workshop [Camera traps, AI, and Ecology](https://inf-cv.uni-jena.de/camtrap-ws/), 7th - 8th September 2023 in Jena, Germany. 

<font color="red">Currently only the YOLO detectors are included. The remaining detectors from the TensorFlow detection API will be added soon.</font>

In this work, various publicly available general object detectors were tested for the task of detecting sheep in UAV images. 
Therefore, these detectors were transfer-learned on the same dataset of sheep using their respective standard configuration
provided in the associated official repo. The following are instructions to transfer-learn the object detectors to reproduce 
the results of this paper. 

NOTES: 
- In the paper the YOLOv5n and YOLOv5s are stated wrongly with 7.7 and 24.0 billion FLOPS, instead it should be 4.5 and 16.5 billion FLOPS.
- For training we used a NVIDIA GeForce GTX 1080 Ti with 11 GB memory, batch sizes were set accordingly and can differ on other systems.
  
#### <font color="red">It is possible that the standard configurations or object detector architectures at the time of reading are different from those used for this work.</font>

## Table of Contents

- [Dataset](#dataset-and-evaluation)
- [YOLOv5](#yolov5)
- [YOLOv6](#yolov6)
- [YOLOv7](#yolov7)
- [YOLOv8](#yolov8)
- [YOLOv5u](#yolov5u)
- [Citation](#citation)
- [License](#license)


## Dataset and Evaluation

We used the raw images of the [SheepCounter](https://universe.roboflow.com/riisprivate/sheepcounter/dataset/11) dataset for our experiments. For 
the YOLO models you need the groundtruth in YOLO format and for the other detectors you will need the COCO format. The training set was used for transfer learning, the validation set for monitoring the loss during training, and the 
test set to evaluate the trained models on the COCO metrics. <br> 

For evaluation, we used [pycocotools](https://pypi.org/project/pycocotools/#description). For converting the YOLO format to
COCO format we used [globox](https://github.com/laclouis5/globox).

The script for estimating the model complexity of the tensorflow models is **model_complexity.py**. The complexity of the
YOLO models were taken from those sources: [YOLOv5](https://github.com/ultralytics/yolov5), [YOLOv6](https://github.com/meituan/YOLOv6), 
[YOLOv7](https://arxiv.org/abs/2207.02696), [YOLOv8](https://github.com/ultralytics/ultralytics), [YOLOv5u](https://github.com/ultralytics/ultralytics/pull/771)



## YOLOv5

1. copy the [official repo](https://github.com/ultralytics/yolov5) and install the required packages following the instruction from the repo
2. download models **yolov5n.pt**, **yolov5s.pt**, **yolov5m.pt**, **yolov5l.pt**, **yolov5x.pt** from [here](https://github.com/ultralytics/yolov5/releases/tag/v7.0) and move them to the root of the downloaded repo
3. move **config_v5.yaml** and **train_YOLOv5.py** from subdirectory [YOLOv5](https://github.com/idmt-odoll/sheep_detection_in_UAV_images/tree/main/YOLOv5) into the downloaded repo
4. change the variable **path** in **config_v5.yaml** to the downloaded dataset
5. use script **train_YOLOv5.py**
   - adjust the batch size to match your system

NOTE: The default configuration is in [hyp.scratch-low.yaml](https://github.com/idmt-odoll/sheep_detection_in_UAV_images/tree/main/YOLOv5/hyp.scratch-low.yaml), can be found in the official repo in <code>data/hyps/</code>


## YOLOv6

1. copy the [official repo](https://github.com/meituan/YOLOv6) and install the required packages following the instruction from the repo
2. move the scripts from subdirectory [YOLOv6](https://github.com/idmt-odoll/sheep_detection_in_UAV_images/tree/main/YOLOv8) to following directories of the downloaded repo:
   - **engine.py** to <code>yolov6/core/</code> and replace file (for saving weights every 10 epochs)
   - **config_v6.yaml** to <code>data/</code>
   - **train_YOLOv6.sh** to the root
3. copy the SheepCounter dataset into the repo to its own subdirectory and name it **SheepCounter**
4. refactor the dataset, so it's structured like this:
   ```shell
   SheepCounter
   ├── images
   │   ├── train
   │   │   ├── train0.jpg
   │   │   └── train1.jpg
   │   ├── val
   │   │   ├── val0.jpg
   │   │   └── val1.jpg
   │   └── test
   │       ├── test0.jpg
   │       └── test1.jpg
   └── labels
       ├── train
       │   ├── train0.txt
       │   └── train1.txt
       ├── val
       │   ├── val0.txt
       │   └── val1.txt
       └── test
           ├── test0.txt
           └── test1.txt
   ```
5. download pretrained models **yolov6n.pt**, **yolov6s.pt**, **yolov6m.pt** and **yolov6l.pt** from [here](https://github.com/meituan/YOLOv6/releases/tag/0.3.0) and move them to <code>weights/</code>
6. use bash script **train_YOLOv6.sh** to start training, alternatively start the training of each detector separately by using a CLI
   - adjust the batch size to match your system 

NOTE: the default configs are [yolov6n_finetune.py](https://github.com/idmt-odoll/sheep_detection_in_UAV_images/tree/main/YOLOv6/yolov6n_finetune.py),
[yolov6s_finetune.py](https://github.com/idmt-odoll/sheep_detection_in_UAV_images/tree/main/YOLOv6/yolov6s_finetune.py), 
[yolov6m_finetune.py](https://github.com/idmt-odoll/sheep_detection_in_UAV_images/tree/main/YOLOv6/yolov6m_finetune.py), 
[yolov6l_finetune.py](https://github.com/idmt-odoll/sheep_detection_in_UAV_images/tree/main/YOLOv6/yolov6l_finetune.py),
can be found in the official repo in <code>configs/</code>


## YOLOv7

1. copy the [official repo](https://github.com/WongKinYiu/yolov7)
2. create a virtual environment
   - Option 1) use the instruction in the repo to create a docker environment
   - Option 2) create a python environment, change to the repo directory and use pip: <code>pip install -r requirements.txt</code>
3. move the scripts from subdirectory [YOLOv7](https://github.com/idmt-odoll/sheep_detection_in_UAV_images/tree/main/YOLOv8) to following directories of the downloaded repo:
   - **yolov7-tiny_custom.yaml**, **yolov7_custom.yaml**, **yolov7x_custom.yaml** to <code>cfg/training/</code>
   - **config_v7** to <code>data/</code>
   - **train_YOLOv7.sh** to the root
   - **train.py** to the root and replace (for saving weights every 10 epochs)
4. download the pretrained models **yolov7-tiny.pt**, **yolov7_training.pt** and **yolov7x_training.pt** from [here](https://github.com/WongKinYiu/yolov7/releases/tag/v0.1) and move to root
5. copy the SheepCounter dataset into the repo to its own subdirectory and name it **SheepCounter**
6. use bash script **train_YOLOv7.sh** to start training, alternatively start the training of each detector separately by using a CLI
   - adjust the batch size to match your system

NOTE: the default config is [hyp.scratch.custom.yaml](https://github.com/idmt-odoll/sheep_detection_in_UAV_images/tree/main/YOLOv7/hyp.scratch.custom.yaml), can be found in the official repo in <code>data/</code>


## YOLOv8
We utilised the [ultralytics](https://github.com/ultralytics/ultralytics) package (version 8.0.53) for training and testing.
The used YOLO class we will be deprecated in version 8.1.x and training instruction should be found on their website.

1. create a python environment and install ultralytics using pip which should install all necessary packages
   - <code>pip install ultralytics==8.0.53</code>
2. (optional) Download pretrained models **yolov8n.pt**, **yolov8s.pt**, **yolov8m.pt**, **yolov8l.pt** and **yolov8x.pt** from [here](https://github.com/ultralytics/assets/releases/)
3. (optional) create a project and copy **config_v8.yaml** and **train_YOLOv8.py** to it
4. change the variable **path** in **config_v8.yaml** to the downloaded dataset
5. use script **train_YOLOv8.py** in subdirectory [YOLOv8](https://github.com/idmt-odoll/sheep_detection_in_UAV_images/tree/main/YOLOv8) and adjust the path to the model
   - instead of downloading the model in step 1, just give the models name without **.pt** suffix
   - adjust the batch size to match your machine (-1 for auto-batch size)

NOTE: The default config is [default.yaml](https://github.com/idmt-odoll/sheep_detection_in_UAV_images/tree/main/YOLOv8/default.yaml), can be found in the official repo in <code>ultralytics/cfg/</code>


## YOLOv5u
We utilised the [ultralytics](https://github.com/ultralytics/ultralytics) package (version 8.0.53) for training and testing. 
The used YOLO class we will be deprecated in version 8.1.x and training instruction should be found on their website.

1. create a python environment and install ultralytics using pip which should install all necessary packages
   - <code>pip install ultralytics==8.0.53</code>
2. (optional) Download pretrained models **yolov5nu.pt**, **yolov5su.pt**, **yolov5mu.pt**, **yolov5lu.pt** and **yolov5xu.pt** from [here](https://github.com/ultralytics/assets/releases/)
3. (optional) create a project and copy **config_v5u.yaml** and **train_YOLOv5u.py** to it
4. change the variable **path** in **config_v5u.yaml** to the downloaded dataset
5. use script **train_YOLOv5u.py** in subdirectory [YOLOv5u](https://github.com/idmt-odoll/sheep_detection_in_UAV_images/tree/main/YOLOv5u) and adjust the path to the model
   - instead of downloading the model in step 1, just give the models name without **.pt** suffix
   - adjust the batch size to match your machine (-1 for auto-batch size)

NOTE: The default config is [default.yaml](https://github.com/idmt-odoll/sheep_detection_in_UAV_images/tree/main/YOLOv5u/default.yaml), can be found in the official repo in <code>ultralytics/cfg/</code>



## Citation

If you found this work useful, consider citing us

```
@inproceedings{Doll_2023_UAVSheepDetection_CamTrapWS,
author = {Doll, Oliver and Loos, Alexander},
title = {{Comparison of Object Detection Algorithms for Livestock Monitoring of Sheep in UAV images}},
booktitle = {Camera traps, AI, and Ecology - 3rd International Workshop},
address = {Jena, Germany},
year = {2023},
pages = {},
}
```

## License

This work is licensed as [Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0) license](https://creativecommons.org/licenses/by-nc/4.0/).
