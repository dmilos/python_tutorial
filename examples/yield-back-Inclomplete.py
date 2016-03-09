#!/usr/bin/python

def counter(maximum):
    i = 0
    while i < maximum:
        val = (yield i)
        # If value provided, change counter
        if val is not None:
            i = val
        else:
            i += 1


it = counter(10)
next(it)
next(it)
it.send(8)
next(it)
