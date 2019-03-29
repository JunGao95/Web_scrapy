import os
import base64
import sys

f = open('base64-test.txt', 'r', encoding='utf-8')
text = f.read()
f.close()

font = base64.b64decode(text)

f = open('font.woff', 'wb')
f.write(font)
f.close()