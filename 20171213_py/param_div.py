# -*- coding:utf-8 -*-
def parrot(a,b='b_param', c='c_param'):

    print "\nc:", c,

    print "\na:", a,

    print "\nb", b

d = {"a": "value1", "b": "value2", "c": "value3"}
parrot(**d)
