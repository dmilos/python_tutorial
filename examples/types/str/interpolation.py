print 'Signed integer decimal %i' % 10
print 'Signed integer decimal %d' % 10

print 'Signed octal value  %o' % 10
print '      'u'	Obsolete type – it is identical to 'd'.	(7)
# print '      'x'	Signed hexadecimal (lowercase).	(2)
# print '      'X'	Signed hexadecimal (uppercase).	(2)
# print '      'e'	Floating point exponential format (lowercase).	(3)
# print '      'E'	Floating point exponential format (uppercase).	(3)
# print '      'f'	Floating point decimal format.	(3)
# print '      'F'	Floating point decimal format.	(3)
# print '      'g'	Floating point format. Uses lowercase exponential format if exponent is less than -4 or not less than precision, decimal format otherwise.	(4)
# print '      'G'	Floating point format. Uses uppercase exponential format if exponent is less than -4 or not less than precision, decimal format otherwise.	(4)
# print '      'c'	Single character (accepts integer or single character string).	 
# print '      'r'	String (converts any Python object using repr()).	(5)
# print '      's'	String (converts any Python object using str()).	(6)
# print '      '%'	No argument is converted, results in a '%' character in the result.	 


print '%(language)s has %(number)03d quote types.' %  {"language": "Python", "number": 2}
