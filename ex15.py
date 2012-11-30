#! /usr/bin/python

from sys import argv

#First argument form the command line is script, second is a filename


filename = raw_input("Please input a filename > ")

#creates file object named txt
txt = open(filename)

print "Here's your file %r:" % filename

# reads the file object
print txt.read()

txt.close()
