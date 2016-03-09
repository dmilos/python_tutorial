import re
p = re.compile('[a-z]+')



print(p.match('ababababab').span())


m= p.match("444")

if m:
    print('Match found: ', m.group())
else:
    print('No match')

m= p.match("aaa")

if m:
    print('Match found: ', m.group())
else:
    print('No match')

m= p.match("aa111a")

if m:
    print('Match found: ', m.group())
else:
    print('No match')



