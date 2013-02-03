#! /usr/bin/python

import sys

words = ('toys', 'fun', 'syot', 'nuf',)

cqs = raw_input("Enter a command, question, or statement: ")

if(cqs in words):
    print str.strip(cqs)

else:
    print "cqs was not found try again!"
    



