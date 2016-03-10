#!/usr/bin/env python

def generate_ints(N):
    for i in range(N):
        print ( 'tra la la' )
        yield i

for i in generate_ints(5):
    print ( i )

