from chatbot.utils.abc import hello as a1
from chatbot.projects.proj1.components.class1 import super_hello
from chatbot.projects.proj1.utils.data_process import hello as b1

print(a1(), b1())
print(super_hello())