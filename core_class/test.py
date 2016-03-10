#!/usr/bin/env python

class FooType(object):
    def __init__(self, id):
        self.id = id
        print self.id, 'born'

    def __del__(self):
        print self.id, 'died'

print 'Make instance...'

ft = FooType(1)

print 'End...'