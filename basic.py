#!/usr/bin/env python

import httplib
c = httplib.HTTPSConnection("ccc.de")
c.request("GET", "/")
response = c.getresponse()
print response.status, response.reason
data = response.read()
print data
