#!/usr/bin/python2

import commands


def Master(Mpass, Mip):
	#creation of master folder..........................................................................................
	master=commands.getstatusoutput("sudo sshpass -p {0} ssh -o strictHostKeyChecking=no {1} mkdir -p /master".format(Mpass,Mip))
	if master[0]==0:
		print "<br/>"
		print ">>Master folder is created in '/' folder..."
		print "<br/>"
	else:
		print "<br/>"
		print ">>No Master is created...."	
		print "<br/>"
	#Previous core file and hdfs file entry remove.....................................................................................
	M_hdfsEntry=commands.getstatusoutput("sudo sshpass -p {} ssh {} \"sed -i '/<configuration>/Q' /etc/hadoop/hdfs-site.xml\"".format(Mpass,Mip))
	if M_hdfsEntry[0]==0:
		print "<br/>"
		print ">>previous hdfsEntry is remove..."
		print "<br/>"
	else:
		print "<br/>"
		print ">>No hdfsEntry done..."
		print "<br/>"
	M_coreEntry=commands.getstatusoutput("sudo sshpass -p {} ssh {} \"sed -i '/<configuration>/Q' /etc/hadoop/core-site.xml\"".format(Mpass,Mip))
	if M_coreEntry[0]==0:
		print "<br/>"
		print ">>previous coreEntry is remove..."
		print "<br/>"
	else:
		print "<br/>"
		print ">>No coreEntry done..."
		print "<br/>"

	#Hdfs-site.xml file entry.................................................................................................
	M_hdfsFile=commands.getstatusoutput("sudo sshpass -p {0} ssh {1} \"echo -e '<configuration>\n<property>\n<name>dfs.name.dir</name>\n<value>/master</value>\n</property>\n</configuration>'| cat >>/etc/hadoop/hdfs-site.xml\"".format(Mpass,Mip))
	if M_hdfsFile[0]==0:
		print "<br/>"
		print ">>hdfsFile is done..."
		print "<br/>"
	else:
		print "<br/>"
		print ">>No hdfsFile done..."
		print "<br/>"
	#Core-site.xml file entry......................................................................................................
	M_coreFile=commands.getstatusoutput("sudo sshpass -p {0} ssh {1} \"echo -e '<configuration>\n<property>\n<name>fs.default.name</name>\n<value>hdfs://{2}:10001</value>\n</property>\n</configuration>'| cat >>/etc/hadoop/core-site.xml\"".format(Mpass,Mip,Mip))
	if M_coreFile[0]==0:
		print "<br/>"
		print ">>coreFile is done..."
		print "<br/>"
	else:
		print "<br/>"
		print ">>No coreFile done..."
		print "<br/>"
	#Format namenode
	formatNamenode=commands.getstatusoutput("sudo sshpass -p {0} ssh -l root {1} \"echo 'Y' | hadoop namenode -format\" ".format(Mpass,Mip))
	if formatNamenode[0]==0:
		print "<br/>"
		print ">>Namenode formatted successfully...."
		print "<br/>"
	else:
		print "<br/>"
		print ">>namenode not formatted..."
		print "<br/>"
	#remove previous mapred-file entry....................
	map_redEntry=commands.getstatusoutput("sudo sshpass -p {} ssh {} \"sed -i '/<configuration>/Q' /etc/hadoop/mapred-site.xml\"".format(Mpass,Mip))
	if map_redEntry[0]==0:
		print "<br/><i>->"
		print "Previous map-red Entry is removed..."
		print "</i>"
	else:
		print "<br/><i>->"
		print "No previous map-red entry remove..."
		print "</i>"
	# MAP-red.xml file entry..........................................................................
	mapredFile=commands.getstatusoutput("sudo sshpass -p {0} ssh {1} \"echo -e '<configuration>\n<property>\n<name>mapred.job.tracker</name>\n<value>{2}:9001</value>\n</property>\n</configuration>'| cat >>/etc/hadoop/mapred-site.xml\"".format(Mpass,Mip,Mip))
	if mapredFile[0]==0:
		print "<br/><i>->"
		print "Map-red's entry done  successfully..."
		print "</i>"
	else:
		print "<br/><i>->"
		print "No mapredFile entry done..."
		print "</i>"
	#JOB-tracker service start....................................................................................................
	jobtracker=commands.getstatusoutput("sudo sshpass -p {0} ssh {1} hadoop-daemon.sh start jobtracker".format(Mpass,Mip))
	if jobtracker[0]==0:
		print "<br/><i>->"
		print "JOB tracker started successfully...."
		print "</i>"
	else:
		print "<br/><i>->"
		print "JOB-tracker not started..."
		print "</i>"
	#Namenode Start Service..............................................................................................................
	namenode=commands.getstatusoutput("sudo sshpass -p {0} ssh {1} hadoop-daemon.sh start namenode".format(Mpass,Mip))
	if namenode[0]==0:
		print "<br/>"
		print ">>namenode started successfully...."
		print "<br/>"
	else:
		print "<br/>"
		print ">>namenode not started..."
		print "<br/>"

