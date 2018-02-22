#!/usr/bin/env python

class FooType(object):

    def __del__(self):
        print 'Good by'

print 'Make instance...'

ft = FooType();

print 'End...'