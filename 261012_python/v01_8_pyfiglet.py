import pyfiglet
# 텍스트를 아스키 아트로 변환해주는 외부 라이브러리

# sentence = pyfiglet.figlet_format("Hello") # figlet_format 함수에 문자열을 넘기면 큼지막한 아스키 아트로 출력
# print(sentence)
#  _   _      _ _       
# | | | | ___| | | ___  
# | |_| |/ _ \ | |/ _ \ 
# |  _  |  __/ | | (_) |
# |_| |_|\___|_|_|\___/ 

sentence = "Hello"
py_sentence = pyfiglet.figlet_format(sentence)
print(sentence) # Hello
# print(py_sentence)
#  _   _      _ _       
# | | | | ___| | | ___  
# | |_| |/ _ \ | |/ _ \ 
# |  _  |  __/ | | (_) |
# |_| |_|\___|_|_|\___/ 