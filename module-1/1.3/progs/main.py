import os
import sys

sys.path.append(sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

sys.path.append('..\\modules')

import module

zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(module.suml(zeroes))
print(module.prodl(ones))

