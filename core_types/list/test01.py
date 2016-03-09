a = ['a', 'b', 'c']

print a
a +=   'd'
print a

b = [ a, ['a', 'b', 'c'], 'c']

print b

print a in b
print a not in b

print a + b

print 'a[1] = ' + a[1]
print 'a[-1] = ' + a[-1]

print a[1:2]

print 'len(b) = %i' % len(b)
print min(b)
print max(b)
