import subprocess
process = subprocess.Popen( [ 'help', '/?' ], stdout=subprocess.PIPE )
print str.split(  process.communicate() [0], '\r\n' )
