# -*- coding: utf-8 -*-

# Нужно собратть информацию об операционной системе и ыерсии пайтона

# TODO запустить этот скрипт и закомитить результат его рработы (файл os_info.txt)

import platform
import sys

info = 'OS info is \n {} \n\nPython version is {} {}'.format(platform.uname(), sys.version, platform.architecture())
print(info)

with open('os_info.txt', 'w') as ff:
    ff.write(info)