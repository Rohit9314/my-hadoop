#!/usr/bin/python2

import commands, cgi

print "content-type: text/html"
print

TIP=cgi.FormContent()['tip'][0]
JIP=cgi.FormContent()['jip'][0]
TP=cgi.FormContent()['tp'][0]
#remove previous mapred-file entry....................
map_redEntry=commands.getstatusoutput("sudo sshpass -p {} ssh {} \"sed -i '/<configuration>/Q' /etc/hadoop/mapred-site.xml\"".format(TP,TIP))
if map_redEntry[0]==0:
	print "<br/><i>->"
	print "Previous map-red Entry is removed..."
	print "</i>"
else:
	print "<br/><i>->"
	print "No previous map-red entry remove..."
	print "</i>"
# MAP-red.xml file entry..........................................................................
mapredFile=commands.getstatusoutput("sudo sshpass -p {0} ssh {1} \"echo -e '<configuration>\n<property>\n<name>mapred.job.tracker</name>\n<value>{2}:9001</value>\n</property>\n</configuration>'| cat >>/etc/hadoop/mapred-site.xml\"".format(TP,TIP,JIP))
if mapredFile[0]==0:
	print "<br/><i>->"
	print "Map-red's entry done  successfully..."
	print "</i>"
else:
	print "<br/><i>->"
	print "No mapredFile entry done..."
	print "</i>"
#TASK-tracker service start....................................................................................................
tasktracker=commands.getstatusoutput("sudo sshpass -p {0} ssh {1} hadoop-daemon.sh start tasktracker".format(TP,TIP))
if tasktracker[0]==0:
	print "<br/><i>->"
	print "TASK-tracker started successfully...."
	print "</i>"
else:
	print "<br/><i>->"
	print "TASK-tracker not started..."
	print "</i>"

