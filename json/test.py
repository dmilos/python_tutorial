import json 
print '***************'
print json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}], indent=4)
print '***************'
print json.dumps({"c": 0, "b": 0, "a": 0}, sort_keys = True, indent=4 )
print '***************'
print json.dumps( {'4': 5, '6': 7}, indent=4)
print '***************'