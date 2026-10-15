import pyfiglet

from termcolor import colored

#구현 : pyfiglet + colored를 적용한 sentence 출력

# 내가 한거
# sentence = "Hello World"
# py_sentence = pyfiglet.figlet_format(sentence)
# result = colored((py_sentence), "yellow", ["bold"])
# print(result)

# 같이한거
sentence = "Wanna Go Home"
py_sentence = pyfiglet.figlet_format(sentence)
color_py_sentence = colored(py_sentence, "green")
print(color_py_sentence)