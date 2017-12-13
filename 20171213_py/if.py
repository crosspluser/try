# -*- coding:utf-8 -*-

true_num = 88

guess_num = int(raw_input("\nInput the number:"))

if guess_num > true_num:
    print "It's lower\n"
elif guess_num < true_num:
    print "It's higher\n"
else:
    print "Got it\n"

print "Game exit :)"
