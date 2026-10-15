import cv2
import matplotlib.pyplot as plt

# 1. 이미지 로드
img = cv2.imread("img.jpg")

# 2. 이미지 증강
# 밝기
img_bright = cv2.convertScaleAbs(img, alpha=1, beta=50)
# alpha : 픽셀에 곱하는 값
# beta : 더할 밝기 (+50 = qkfrrp, -50 = 어둡게)

#채도
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
h, s, v =cv2.split(img_hsv)
h = (h + 30) % 180
# 채도 범위 변경
img_hue = cv2.cvtColor(cv2.merge([h, s, v]), cv2.COLOR_HLS2BGR)

# 수평 반전
img_flipped = cv2.flip(img, 1) 

# 3. 이미지 시각화
fig, ax = plt.subplots(2, 2, figsize=(10,5))

# 3-1. 원본 이미지
ax[0,0].imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
ax[0,0].axis('off')
ax[0,0].set_title("Original")

# 3-2. 밝기 이미지
ax[0,1].imshow(cv2.cvtColor(img_bright, cv2.COLOR_BGR2RGB))
ax[0,1].axis('off')
ax[0,1].set_title("Bright")

# 채도 이미지
ax[1,0].imshow(cv2.cvtColor(img_hue, cv2.COLOR_BGR2RGB))
ax[1,0].axis('off')
ax[1,0].set_title("HSV")


ax[1,1].imshow(cv2.cvtColor(img_flipped, cv2.COLOR_BGR2RGB))
ax[1,1].axis('off')
ax[1,1].set_title("FLIPPED")

plt.show()

# 5. 이미지 저장
cv2.imwrite("./bright_img.jpg", img_bright)
cv2.imwrite("./hsv_img.jpg", img_hsv)
cv2.imwrite("./flip_img.jpg", img_flipped)

print("이미지 저장 완료")