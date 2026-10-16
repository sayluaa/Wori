from ultralytics import solutions
import cv2

# 1. 비디오 경로 설정
cap = cv2.VideoCapture("http://210.99.70.120:1935/live/cctv009.stream/playlist.m3u8")

# 2. 모델 로드
blurrer = solutions.ObjectBlurrer(
    model="261016_4_yolo_advan.py/model.pt", #yolo8n-face.pt => 얼굴만 탐지
    show=False,
    conf=0.6,
    bulr_ratio=0.3
)
# 3. 비디오 프레임 처리
while cap.isOpened():
    success, frame = cap.read()
    if not success:
        print("프레임 확인해주세요")
        break
    
    # 3.1 모델 추론
    results = blurrer(frame)
    
    # 3-2. 처리된 프레임 표시 및 윈도우 창
    cv2.namedWindow("BLUR_YOLO", cv2.WINDOW_NORMAL) # 창 크기 조절
    cv2.imshow("BLUR_YOLO", results.plot_im)
    
    # 3-3. q키 눌러서 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("q키를 눌러서 종료")
        break
    
# 4. 자원 해제
cap.release()
cv2.destroyAllWindows()