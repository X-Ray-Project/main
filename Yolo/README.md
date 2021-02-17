### Yolov5
+ Yolo.ipynb
    + Yolov5s

+ Yolo2.ipynb
    + Yolov5l

+ Yolo3.ipynb
    + Yolov5s
    + 5-Fold 방식



+ 진행한 Yolo parameter
    + 전처리 / train / detect / result
    + train 80% val 20% / --img 832 --batch 16 --epochs 30 / --img 640 --conf 0.15 --iou 0.5 / 0.024
    + train 80% val 20% / --img 640 --batch 16 --epochs 200 / --img 640 --conf 0.15 --iou 0.4 / 0.048
    + 5-Fold train 80% val 20% / --img 640 --batch 16 --epochs 40 X5 / --img 640 --conf 0.15 --iou 0.4 / 0.098 
    