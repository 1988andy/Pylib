import sys
sys.path.append("..")

import os
import fs

fpath = os.getcwd() + ("\\temp.txt")
print('fs.write_file(fpath, "China 中国好 \r\n", True)')
fs.write_file(fpath, "China 中国好 \r\n", True)
print("============================")
print("fs.read_file(fpath)")
print(fs.read_file(fpath))

