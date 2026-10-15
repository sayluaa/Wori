# 파일 쓰기 : 새롭게 생성, 기존 내용이 있다면 덮어씀
# with open("memo.txt", "w", encoding="utf-8")as f:
#     f.write("새로운 한줄 추가")

# 파일 읽기
# with open("memo.txt", "r", encoding="utf-8")as f:
#     text = f.read()
    
# # print(text) # 새로운 한줄 추가

# # 파일 이어쓰기
# with open("memo.txt", "a", encoding="utf-8")as f:
#     f.write("\n 지금 내가 쓴 내용도 작성 완료")
    
# print("완료")

# 1. x 모드
# with open("memo2.txt", "x", encoding="utf-8")as f:
#     f.write("새로 추가를 하나요? 막나요?")
    
   
# 2. rb 모드
# with open("img.jpg", "rb")as img:
#     img_data = img.read()
   
# print(img_data) 

# 3. wb 모드(이미지 쓰기)
# with open("wb_img.jpg", "wb")as b_img:
#     b_img.write(img_data)
    
# 4. r+ 모드(읽기 쓰기 둘다)
# with open("memo2.txt", "r+", encoding="utf-8")as f:
#     text = f.read()# 먼저 읽기
#     f.seek(0) # 맨 앞부터 수정
#     f.write("새롭게 시작할게")  # 새로 쓰기
#     # f.write(text.replace("새로운", "낡은")) # 문자 변경
#     f.truncate() # 나머지 내용 제거
    
# print("DONE")
