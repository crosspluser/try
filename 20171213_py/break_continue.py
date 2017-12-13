# -*- coding:utf-8 -*-

for i in range(5):
    if i ==3:
        break
    print i

for i in xrange(10):
    for j in xrange(10):
        break
    print i, j

for i in range(5):
    if i == 3:
        continue
    print i
