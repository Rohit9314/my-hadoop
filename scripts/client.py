#!/usr/bin/python2

import commands, cgi

print "content-type: text/html"
print

Cip=cgi.FormContent()['ipC'][0]


Cpass=cgi.FormContent()['passC'][0]
 
mip=cgi.FormContent()['MIP'][0]

print "<h2 align='center'>*******************************************Welcome to my Hadoop setup*******************************************</h2>"

#remove previous core-file entry....................
RmvcoreEntry=commands.getstatusoutput("sudo sshpass -p {} ssh {} \"sed -i '/<configuration>/Q' /etc/hadoop/core-site.xml\"".format(Cpass, Cip))
if RmvcoreEntry[0]==0:
	print "<br/><i>"
	print "<h2><font color='red'> !!  previous coreEntry is remove...</font></h2>"
	print "</i>"
else:
	print "<br/><i>->"
	print "No coreEntry done..."
	print "</i>"

#remove previous mapred-file entry....................
map_redEntry=commands.getstatusoutput("sudo sshpass -p {} ssh {} \"sed -i '/<configuration>/Q' /etc/hadoop/mapred-site.xml\"".format(Cpass, Cip))
if map_redEntry[0]==0:
	print "<br/><i>->"
	print "Previous map-red Entry is removed..."
	print "</i>"
else:
	print "<br/><i>->"
	print "No previous map-red entry remove..."
	print "</i>"
#core-file entry
coreFile=commands.getstatusoutput("sudo sshpass -p {0} ssh {1} \"echo -e '<configuration>\n<property>\n<name>fs.default.name</name>\n<value>hdfs://{2}:10001</value>\n</property>\n</configuration>'| cat >>/etc/hadoop/core-site.xml\"".format(Cpass, Cip,mip))
if coreFile[0]==0:
	print "<br/><i>->"
	print "CoreFile's entry done  successfully..."
	print "</i>"
else:
	print "<br/><i>->"
	print "No coreFile entry done..."
	print "</i>"
# MAP-red.xml file entry..........................................................................
mapredFile=commands.getstatusoutput("sudo sshpass -p {0} ssh {1} \"echo -e '<configuration>\n<property>\n<name>mapred.job.tracker</name>\n<value>{2}:9001</value>\n</property>\n</configuration>'| cat >>/etc/hadoop/mapred-site.xml\"".format(Cpass, Cip,mip))
if mapredFile[0]==0:
	print "<br/><i>->"
	print "Map-red's entry done  successfully..."
	print "</i>"
else:
	print "<br/><i>->"
	print "No mapredFile entry done..."
	print "</i>"

# mapper-reducer program.........................................
print "<br/><br/>"
print """<form enctype='multipart/form-data' action='file.py' method='POST'>
Browse your file <input type='file' name='f' />
<input type='submit' />
</form>"""

