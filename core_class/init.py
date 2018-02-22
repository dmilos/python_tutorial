#!/usr/bin/env python

class FooType(object):
    def __init__(self, id):
        self.id = id
        print self.id, 'born'

print 'Make instance...'

ft = FooType(1)

print 'End...'