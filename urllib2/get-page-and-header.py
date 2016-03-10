import urllib.request
local_filename = "./a.html"

local_filename, headers = urllib.request.urlretrieve('http://python.org/')
print( headers )
print( local_filename )