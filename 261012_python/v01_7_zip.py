names = ["뽀삐", "초코", "쿠키"]
scores = [95, 88, 72]

# for name, score in zip(names, scores): # for문이 한 번 돌 때마다 같은 자리끼리 (name, score) 한 쌍을 받음
#     print(f"{name}: {score}점")
# 뽀삐: 95점
# 초코: 88점
# 쿠키: 72점

# pairs = list(zip(names, scores)) # 짝지은 결과가 한꺼번에 (이름, 점수) 튜플 리스트로 출력
# print(pairs) # [('뽀삐', 95), ('초코', 88), ('쿠키', 72)]

keys = ["이름", "나이", "직업"]
values = ["홍길동", 30, "개발자"]

person = dict(zip(keys, values)) # zip()이 이름표(키)·내용(값)을 짝짓고, dict()가 사물함으로 묶음
print(person) # {'이름': '홍길동', '나이': 30, '직업': '개발자'}