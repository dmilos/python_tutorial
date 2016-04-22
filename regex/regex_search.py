#!/usr/bin/env python

import re
p = re.compile('[a-z]+')

print( p.search('123123ababababab123123' ).span())


m = p.search( "!@#!@#444)()(*)" )

if m:
    print('search found: ', m.group())
else:
    print('No search')

m= p.search( "QWEQWEaaaQWEQWE" )

if m:
    print('search found: ', m.group())
else:
    print('No search')

m= p.search("!@#aa11!@#!1a!@#")

if m:
    print('search found: ', m.group())
else:
    print('No search')



