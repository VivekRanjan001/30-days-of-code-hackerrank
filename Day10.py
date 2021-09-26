#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
listofbinaryno = []
while True:
    quest = n//2
    reminder = n%2
    if reminder == 0:
        listofbinaryno.append(reminder)
    else:
            listofbinaryno.append(reminder)
    n = quest
    if n == 0:
        break
listofbinaryno.reverse()
counter = 0
libc = []
for i in range(len(listofbinaryno)-1):
    if listofbinaryno[i] == 1:
        counter += 1

        if i == len(listofbinaryno)-2:
            if listofbinaryno[i+1] == 1:
                counter += 1
                libc.append(counter)

        if listofbinaryno[i + 1] == 0:
            libc.append(counter)
            counter = 0

libc.sort()
print(libc[-1])

