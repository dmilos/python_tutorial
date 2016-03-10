#!/usr/bin/env python

myfile = open( "./test.txt", "r" )

# Line include new line at the end
for line in  myfile :
    print( "linija %s", line )