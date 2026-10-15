# 클래스 : 설계도 class Dog
# 객체 : 틀로 찍어낸 진짜 붕어빵 (실제로 만들어진 것)	dog1, dog2
# 속성 : 붕어빵의 맛·크기 (정보를 담는 변수)	self.name, self.age
# 메서드 : 붕어빵이 할 수 있는 일 (먹기·데우기 — 클래스 안의 함수)	bark()
# 생성자 : 붕어빵을 처음 만들 때 자동 실행되는 준비 단계 (재료 넣기)	__init__

#클래스 정의
class Bungeobbang:                          # 클래스 정의
    def __init__(self, name, color):  # 생성자 — 객체 생성 시 자동 실행
        self.name = name            # 속성 name 저장
        self.color = color             # 속성 color 저장

    def info(self):                 # 메서드 정의
        print(f"안녕, 나는 {self.name} 붕어빵이고 {self.color}색이야.")

# 객체 생성
first_bbang = Bungeobbang("슈크림", "연노란")

# 메서드 호출
first_bbang.info()