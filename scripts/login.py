#!/usr/bin/python2


import cgi

print "content-type: text/html"


userName=cgi.FormContent()['username'][0]
passWord=cgi.FormContent()['password'][0]

auser="sp"
apass="redhat"

if userName == auser and  passWord == apass:
	print "location: ../demand.html"
	print

else:
	
	print "location: ../login.html"
	print
