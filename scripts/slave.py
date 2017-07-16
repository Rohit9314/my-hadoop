#!/usr/bin/python2

import cgi, commands, LV

print "content-type: text/html"
print 

#ipClient=raw_input("Enter the ip of client server: ")
#password= raw_input("Enter the password of the client: ")
#lv= raw_input("Enter the harddisk name: ")
#mip=raw_input("Enter master ip: ")



ipClient=cgi.FormContent()['Clientip'][0]
password=cgi.FormContent()['PASSWORD'][0]
mip=cgi.FormContent()['MIP'][0]
lvSize=cgi.FormContent()['size'][0]

LV.lvc(ipClient,password,lvsize)
"""
#creation of slave folder, unmounting it if previously mounted, formatting it, finally mounting on /slave folder....................
slave=commands.getstatusoutput("sudo sshpass -p {0} ssh -o strictHostKeyChecking=no {1} mkdir -p /slave".format(password,ipClient))
if slave[0]==0:
	print "Slave folder is created in '/' folder..."
else:
	print "No slave is created...."	
unmount=commands.getstatusoutput("sudo sshpass -p {0} ssh {1} umount {2}".format(password,ipClient,sd))
if unmount[0]==0:
	print "unmount  is done if alreaady monted..."
else:
	print "No unmount is done..."
Format=commands.getstatusoutput("sudo sshpass -p {0} ssh {1} mkfs.ext4 {2}".format(password,ipClient,sd))
if Format[0]==0:
	print "Format is done..."
else:
	print "No Format done..."
mount=commands.getstatusoutput("sudo sshpass -p {0} ssh {1} mount {2} /slave".format(password,ipClient,sd))
if mount[0]==0:
	print "mount is done in '/slave' folder..."
else:
	print "No mount is done..."
#Previous core file and hdfs file entry remove.....................................................................................
hdfsEntry=commands.getstatusoutput("sudo sshpass -p {} ssh {} \"sed -i '/<configuration>/Q' /etc/hadoop/hdfs-site.xml\"".format(password, ipClient))
if hdfsEntry[0]==0:
	print "previous hdfsEntry is remove..."
else:
	print "No hdfsEntry done..."
coreEntry=commands.getstatusoutput("sudo sshpass -p {} ssh {} \"sed -i '/<configuration>/Q' /etc/hadoop/core-site.xml\"".format(password, ipClient))
if coreEntry[0]==0:
	print "previous coreEntry is remove..."
else:
	print "No coreEntry done..."



#Hdfs-site.xml file entry.................................................................................................
hdfsFile=commands.getstatusoutput("sudo sshpass -p {0} ssh {1} \"echo -e '<configuration>\n<property>\n<name>dfs.data.dir</name>\n<value>/slave</value>\n</property>\n</configuration>'| cat >>/etc/hadoop/hdfs-site.xml\"".format(password, ipClient))
if hdfsFile[0]==0:
	print "hdfsFile is done..."
else:
	print "No hdfsFile done..."
#Core-site.xml file entry......................................................................................................
coreFile=commands.getstatusoutput("sudo sshpass -p {0} ssh {1} \"echo -e '<configuration>\n<property>\n<name>fs.default.name</name>\n<value>hdfs://{2}:10001</value>\n</property>\n</configuration>'| cat >>/etc/hadoop/core-site.xml\"".format(password, ipClient,mip))
if coreFile[0]==0:
	print "coreFile is done..."
else:
	print "No coreFile done..."

#Datanode Start Service..............................................................................................................
datanode=commands.getstatusoutput("sudo sshpass -p {0} ssh {1} hadoop-daemon.sh start datanode".format(password, ipClient))
if datanode[0]==0:
	print "datanode started successfully...."
else:
	print "datanode not started..."


"""
