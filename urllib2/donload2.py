import urllib2
import sys

username = 'vxme-am-jenkins'
password = 'PsoGlav123'
url = 'http://10.53.59.190:8080/job/Trunk_Autologin/config.xml'

import urllib2, base64

request = urllib2.Request(url)
base64string = base64.encodestring('%s:%s' % (username, password)).replace('\n', '')
request.add_header("Authorization", "Basic %s" % base64string)   
result = urllib2.urlopen(request).read()

print result
