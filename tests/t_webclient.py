import sys
sys.path.append("..")

from webclient import *

wc = WebClient("http://www.cnblogs.com/feeland/p/4415645.html")
print(wc.getstring())
