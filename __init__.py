import os
import sys

dir_common = os.path.split(os.path.realpath(__file__))[0]
sys.path.append(dir_common)  # 将根目录添加到系统目录,才能正常引用其他文件的内容
print('系统根目录', dir_common)
