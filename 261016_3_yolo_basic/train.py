from ultralytics import YOLO

# 1. 모델 로드
model = YOLO("yolo11n-cls.pt")

# 2. 모델 학습
model.train(data="C:/Users/Woori/Downloads/make_cls_yolo_model/dataset", epochs=2, batch=1, imgsz=256)