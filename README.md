# Sheep Detection in UAV images
This is the official repo for the paper "**Comparison of Object Detection Algorithms for Livestock Monitoring of Sheep in UAV images**" which will be presented on the 3rd Internation Workshop Camera traps, AI, and Ecology, 7th - 8th September 2023 in Jena, Germany. 

Content will be added until/after the presentation at the workshop.

In this work, various publicly available general object detectors were tested for the task of detecting sheep in UAV images. 
Therefore, these detectors were transfer-learned on the same dataset of sheep using their respective standard configuration
provided in the associated official repo. The following is a guide to transfer-learn the object detectors to reproduce 
the results of this paper. 

NOTES: 
- In the paper the YOLOv5n and YOLOv5s are stated wrongly with 7.7 and 24.0 billion FLOPS, instead it should be 4.5 and 16.5 billion FLOPS.
- For training we used a NVIDIA GeForce GTX 1080 Ti with 11 GB memory, batch sizes were set accordingly and can differ on other systems.
- Paths to the dataset provided in the config files must be adjusted before training.
  
#### <font color="red">It is possible that the standard configurations or object detector architectures at the time of reading are different from those used for this work.</font>

## Table of Contents

- [Dataset](##datasetandevaluation)
- [YOLOv5](##yolov5)
- [YOLOv6](##yolov6)
- [YOLOv7](##yolov7)
- [YOLOv8](##yolov8)
- [YOLOv5u](##yolov5u)
- [Citation](##citation)
- [License](##license)


## Dataset and Evaluation

We used the raw images of the [SheepCounter](https://universe.roboflow.com/riisprivate/sheepcounter/dataset/11) dataset for our experiments. <br>
The training set was used for transfer learning, the validation set for monitoring the loss during training, and the 
test set to evaluate the trained models on the COCO metrics. <br> 

For evaluation, we used [pycocotools](https://pypi.org/project/pycocotools/#description). For converting the yolo-format to
coco-format we used [globox](https://github.com/laclouis5/globox).

The script for estimating the model complexity of the tensorflow models is **model_complexity.py**. The complexity of the
YOLO models were taken from those sources: [YOLOv5](https://github.com/ultralytics/yolov5), [YOLOv6](https://github.com/meituan/YOLOv6), 
[YOLOv7](https://arxiv.org/abs/2207.02696), [YOLOv8](https://github.com/ultralytics/ultralytics), [YOLOv5u](https://github.com/ultralytics/ultralytics/pull/771)



## YOLOv5


## YOLOv6


## YOLOv7


## YOLOv8


## YOLOv5u
We utilised the [ultralytics](https://github.com/ultralytics/ultralytics) package (8.0.53 ) for training and testing. 
The used YOLO class we will be deprecated in version 8.1.x and training instruction should be found on their website.

Models pretrained on COCO can be found [here](https://github.com/ultralytics/assets/releases/)


## Citation

If you found this work useful, consider citing us

```
@inproceedings{Doll:2023:ctws,
  title = {Comparison of Object Detection Algorithms for Livestock Monitoring of Sheep in UAV images},
  author = {Doll, Oliver and Loos, Alexander},
  maintitle = {Camera traps, AI, and Ecology},
  booktitle = {3rd International Workshop},
  year = {2023},
  month_numeric = {09}
}
```

## License