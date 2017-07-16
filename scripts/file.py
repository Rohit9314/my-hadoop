#!/usr/bin/python2

import cgi,commands

print "content-type: text/html"
print

fileData=cgi.FormContent()['f'][0]
fh=open('../uploads/dataSet.txt', 'w')
fh.write(fileData)
fh.close()

#Master and Job tracker ip..........
copy=commands.getstatusoutput("sudo sshpass -p 'redhat' scp ../uploads/dataSet.txt  192.168.43.67:/root/Desktop/")
if copy[0]==0:
	print "Copy done.."
else:
	print "No copy.."


upload=commands.getstatusoutput("sudo sshpass -p 'redhat' ssh 192.168.43.67  hadoop fs -put /root/Desktop/dataSet.txt /")
if upload[0]==0:
	print "Data Set uploaded..."
else:
	print "No data set uploaded..."
