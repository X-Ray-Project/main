### Yolov5
+ Yolo.ipynb
    + Yolov5s
    + 1024x1024 / train 80% val 20% / --img 832 --batch 16 --epochs 30 / --img 640 --conf 0.15 --iou 0.5 / 0.024
+ Yolo2.ipynb
    + Yolov5l
    + 1024x1024 / train 80% val 20% / --img 640 --batch 16 --epochs 200 / --img 640 --conf 0.15 --iou 0.4 / 0.048

+ Yolo3.ipynb
    + Yolov5s
    + 5-Fold 방식
    + 1024x1024 / 5-Fold train 80% val 20% / --img 640 --batch 16 --epochs 40 X5 / --img 640 --conf 0.15 --iou 0.4 / 0.098 

+ Yolov4.ipynb
    + Yolov5s
    + 5-Fold 방식
    + 1024x1024 / 5-Fold train 66% val 33% / --img 832 --batch 16 --epochs 40 X5 / --img 832 --conf 0.2 --iou 0.4 / 0.126
    + 1024x1024 / 5-Fold train 66% val 33% / --img 832 --batch 16 --epochs 40 X5 / --img 832 --conf 0.4 --iou 0.4 / 0.113
    + 1024x1024 / 5-Fold train 66% val 33% / --img 832 --batch 16 --epochs 40 X5 / --img 832 --conf 0.15 --iou 0.4 / 0.13


+ 진행한 Yolo parameter
    + 이미지 / 전처리 / train / detect / result
    + 1024x1024 / train 80% val 20% / --img 832 --batch 16 --epochs 30 / --img 640 --conf 0.15 --iou 0.5 / 0.024
    + 1024x1024 / train 80% val 20% / --img 640 --batch 16 --epochs 200 / --img 640 --conf 0.15 --iou 0.4 / 0.048
    + 1024x1024 / 5-Fold train 80% val 20% / --img 640 --batch 16 --epochs 40 X5 / --img 640 --conf 0.15 --iou 0.4 / 0.098 
    + 1024x1024 / 5-Fold train 66% val 33% / --img 832 --batch 16 --epochs 40 X5 / --img 832 --conf 0.2 --iou 0.4 / 0.126
    + 1024x1024 / 5-Fold train 66% val 33% / --img 832 --batch 16 --epochs 40 X5 / --img 832 --conf 0.4 --iou 0.4 / 0.113
    + 1024x1024 / 5-Fold train 66% val 33% / --img 832 --batch 16 --epochs 40 X5 / --img 832 --conf 0.15 --iou 0.4 / 0.13
