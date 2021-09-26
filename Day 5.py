#LOOP HACKATHON
#
# import math
# import os
# import random
# import re
import sys

#
#
# if __name__ == '__main__':
#     n = int(input())
#
# for i in range(1,10 + 1):
#     print("{} x {} = {}".format(n,i,n * 1))
n = int(input().strip())
for i in range(1, 11):
    product = n * i
    print('{} x {} = {}'.format(n, i, product))
