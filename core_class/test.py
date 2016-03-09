class FooType(object):
    def __init__(self, id):
        self.id = id
        print self.id, 'born'

    def __del__(self):
        print self.id, 'died'

def make_foo():
    print 'Making...'
    ft = FooType(1)
    print 'Returning...'
    return ft

print 'Calling...'
ft = make_foo()
print 'End...'