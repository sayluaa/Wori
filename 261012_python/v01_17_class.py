#클래스 정의
class Rice_cake:                          # 클래스 정의
    def __init__(self, name, color, shape):  # 생성자 — 객체 생성 시 자동 실행
        self.name = name            # 속성 name 저장
        self.color = color             # 속성 color 저장
        self.shape = shape             # 속성 shape 저장

    def info(self):                 # 메서드 정의
        print(f"저건 {self.name}이고 {self.color}색을 띄며 {self.shape} 모양이야.")
    
    def eat(self):                 # 메서드 정의
            print(f"나는 {self.name}(이)가 더 좋아.")
        

# 객체 생성
first_cake = Rice_cake("백설기", "하얀", "네모난")
second_cake = Rice_cake("쑥떡", "녹", "동그란")



# 메서드 호출
first_cake.info()
first_cake.eat()
second_cake.info()
second_cake.eat()
