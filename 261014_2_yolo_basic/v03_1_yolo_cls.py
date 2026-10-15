from ultralytics import YOLO
import cv2 # 이미지 넣을때 짝꿍인 컴퓨터 비전

# 1. 모델 로드
# YOLO("모델명")
model = YOLO("yolo11n-cls.pt")
# n -> s -> m -> l -> x

# 2. 모델 추론
results = model("261014_2_yolo_basic/input2.jpg")

# 3. 결과 시각화
result_image = results[0].plot()

# 4. 결과 이미지 저장
# output_result_image_path = "저장할 경로/저장할 이미지 파일 이름.jpg"
output_result_image_path = "./output2.jpg"
cv2.imwrite(output_result_image_path, result_image)

print(f"예측 결과 이미지가 잘 저장되었습니다. {output_result_image_path}")