import array
import os
import sys

code_path = "./out.tbc"

code = array.array('B')

codesize = os.stat(code_path).st_size
code.fromfile(open(code_path, 'rb'), codesize)

if sys.byteorder == 'big':
	code.byteswap()

print(code)
