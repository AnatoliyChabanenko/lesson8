from lesson18.lesson18_2 import say_hello

from pprint import pprint
import sys

#
# pprint(sys.path)
sys.path.insert(0 ,'/Users/chabanenko.anatoliygmail.com/Downloads/пайтон/pythonProject/lesson16')
sys.path.append('/Users/chabanenko.anatoliygmail.com/Downloads/пайтон/pythonProject/lesson17')
pprint(sys.path)
print(sys.argv)
print(sys.byteorder)
print(sys.builtin_module_names )
print(sys.executable)
print(sys.maxsize)
pprint(sys.platform)