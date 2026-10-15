# is_raining = True

# if is_raining:
#     print("우산을 챙겨요!") #True일때 이 줄 실행
# else:
#     print("우산 없어도 돼요") #False일때 이 줄 실행

temperature = 9 #오늘 기온 (°C)

if temperature >= 30:
    print("덥다! 반팔 입기") # 30이상 일때 이 줄 출력
elif temperature >= 20:
    print("딱 좋아! 가볍게 입기") #(29 >= 20) 일때 이 줄 출력
elif temperature >= 10:
    print("쌀쌀해, 겉옷 챙기기") #(19 >= 10) 일때 이 줄 출력
else:
    print("추워! 두꺼운 코트 입기") # 9이하 일때 이 줄 출력