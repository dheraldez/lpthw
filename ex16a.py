#! /usr/bin/python

from sys import argv

script, filename = argv

print "We're going to read %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'r')

print "Reading the file.   Goodbye!"
print "\n"
print target.read()

print "And finally we close it!"
target.close()