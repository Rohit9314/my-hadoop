#!/usr/bin/python2

import cgi,LV,commands,masterFun

print "Content-Type: text/html"
print

num= cgi.FormContent()['nslave'][0]
Size= cgi.FormContent()['size'][0]
ip=cgi.FormContent()['IP'][0]
p=cgi.FormContent()['P'][0]

total=int(num)

print "<h1 align='center'><strong><i>**********************Welcome to Docker setup**********************</strong></i></h1><br />"

#***********Creation of master and job tracker*******************

masterFun.Master(p, ip)

#***********Don't change anything in lvc*******************

tlv=0
while tlv<total:
	LV.lvc(tlv,Size)
print "<h2 align='center'><strong><i>*********************You are inside Docker**********************</strong></i></h2><br />"
	nfsStatus=commands.getstatusoutput("sudo  systemctl restart nfs")
	if nfsStatus[0]==0:
		print "<br/><i>->"
		print "NFS server is setup successfully.."
		print "</i>"
	else:
		print "<br/><i>->"
		print "<h2><font color='red'>!!Not able to create NFS server ...</font></h2>"
		print "</i>"
	# 	Mount-Point creation........................................
	dirC= commands.getstatusoutput("sudo sshpass -p {0} ssh -o strictHostKeyChecking=no {1} mkdir -p /media/Docker{2} ".format(p,ip,tlv))
	if dirC[0]==0:
		mount=commands.getstatusoutput("sudo sshpass -p {0} ssh -o strictHostKeyChecking=no {1} mount 192.168.43.234:/media/Myansible/ansil{2} /media/Docker{3}".format(p,ip,tlv,tlv))
		if mount[0]==0:
			print "<br/><i>->"
			print "LV is mounted successfully .."
			print "</i>"

			dockerStatus=commands.getstatusoutput("sudo sshpass -p {0} ssh -o strictHostKeyChecking=no {1} docker run -dit -v /media/Docker{2}:/dockStore{3} --privileged=true --name=Dock{4} os:v5".format(p,ip,tlv,tlv,tlv))
			if dockerStatus[0]==0:
				print "<br/><i>->"
				print "Docker  started successfully .."
				print "</i>"
			else:
				print "<br/><i>->"
				print "<h2><font color='red'>!!No  docker started ...</font></h2>"
				print "</i>"

			#Previous hdfs file entries remove..............
			hdfsEntry=commands.getstatusoutput("sudo sshpass -p {} ssh {} \"sed -i '/<configuration>/Q' /ManualHadoop/hdfs-site.xml\"".format(p, ip))
			if hdfsEntry[0]==0:
				print "<br/><i>->"
				print "Previous hdfs file entry is removed..."
				print "</i>"
			else:
				print "<br/><i>->"
				print "<h2><font color='red'>!!No previous hdfs file entry removed...</font></h2>"
				print "</i>"
			#Previous core file entries remove..............
			coreEntry=commands.getstatusoutput("sudo sshpass -p {} ssh {} \"sed -i '/<configuration>/Q' /ManualHadoop/core-site.xml\"".format(p, ip))
			if coreEntry[0]==0:
				print "<br/><i>->"
				print "Previous coreEntry is removed..."
				print "</i>"
			else:
				print "<br/><i>->"
				print "<h2><font color='red'>!!No previous coreEntry remove...</font></h2>"
				print "</i>"
			#Previous map-red file entries remove..............
			map_redEntry=commands.getstatusoutput("sudo sshpass -p {} ssh {} \"sed -i '/<configuration>/Q' /ManualHadoop/mapred-site.xml\"".format(p, ip))
			if map_redEntry[0]==0:
				print "<br/><i>->"
				print "Previous map-red Entry is removed..."
				print "</i>"
			else:
				print "<br/><i>->"
				print "<h2><font color='red'>!!No previous map-red entry remove...</font></h2>"
				print "</i>"
			#Hdfs-site.xml file entry.................................................................................................
			hdfsFile=commands.getstatusoutput("sudo sshpass -p {0} ssh {1} \"echo -e '<configuration>\n<property>\n<name>dfs.data.dir</name>\n<value>/dockStore{2}</value>\n</property>\n</configuration>'| cat >>/ManualHadoop/hdfs-site.xml\"".format(p, ip,tlv))
			if hdfsFile[0]==0:
				print "<br/><i>->"
				print "hdfsFile's entry done successfully..."
				print "</i>"
			else:
				print "<br/><i>->"
				print "<h2><font color='red'>!!No hdfsFile entry done...</font></h2>"
				print "</i>"
			#Core-site.xml file entry...........................................................................
			coreFile=commands.getstatusoutput("sudo sshpass -p {0} ssh {1} \"echo -e '<configuration>\n<property>\n<name>fs.default.name</name>\n<value>hdfs://{2}:10001</value>\n</property>\n</configuration>'| cat >>/ManualHadoop/core-site.xml\"".format(p, ip,ip))
			if coreFile[0]==0:
				print "<br/><i>->"
				print "CoreFile's entry done  successfully..."
				print "</i>"
			else:
				print "<br/><i>->"
				print "<h2><font color='red'>!!No coreFile entry done...</font></h2>"
				print "</i>"
			# MAP-red.xml file entry	(TskTracker)................................................................
			mapredFile=commands.getstatusoutput("sudo sshpass -p {0} ssh {1} \"echo -e '<configuration>\n<property>\n<name>mapred.job.tracker</name>\n<value>{2}:9001</value>\n</property>\n</configuration>'| cat >>/ManualHadoop/mapred-site.xml\"".format(p, ip,ip))
			if mapredFile[0]==0:
				print "<br/><i>->"
				print "Map-red's entry done  successfully..."
				print "</i>"
			else:
				print "<br/><i>->"
				print "<h2><font color='red'>!!No mapredFile entry done...</font></h2>"
				print "</i>"
			# hosts file entry...........................................
			GetHostDock=commands.getoutput("sudo sshpass -p {0} ssh -o strictHostKeyChecking=no {1} docker inspect Dock{2} | jq '.[].Config.Hostname'".format(p,ip,tlv))
			GetIpDock=commands.getoutput("sudo sshpass -p {0} ssh -o strictHostKeyChecking=no {1} docker inspect Dock{2} | jq '.[].NetworkSettings.Networks.bridge.IPAddress'".format(p,ip,tlv))
			hostFile=commands.getstatusoutput("sudo sshpass -p {0} ssh {1} \"echo -e '{2}  {3} ' | cat >>/etc/hosts\"".format(p, ip,GetIpDock.strip('"'),GetHostDock.strip('"')))
			if hostFile[0]==0:
				print "<br/><i>->"
				print "hostFile's entry done  successfully..."
				print "</i>"
			else:
				print "<br/><i>->"
				print "<h2><font color='red'>!!No hostFile entry done...</font></h2>"
				print "</i>"			

		#******************************Docker Part*******************************************
			copy=commands.getstatusoutput("sudo sshpass -p {0} ssh  -o strictHostKeyChecking=no {1} 'sshpass -p rj scp -o strictHostKeyChecking=no    /ManualHadoop/hdfs-site.xml /ManualHadoop/core-site.xml /ManualHadoop/mapred-site.xml {2}:/etc/hadoop/'".format(p,ip, GetIpDock.strip('"')))
			if copy[0]==0:
				print "<br/><i>->"
				print "hdfs , core and map-red file  is created in docker..."
				print "</i>"
			else:
				print "<br/><i>->"
				print "<h2><font color='red'>!!No hdfs , core and map-red file is created in docker...</font></h2>"
				print "</i>"

			DNserviceStart=commands.getstatusoutput("sudo sshpass -p {0} ssh -o strictHostKeyChecking=no {1} docker exec Dock{2} hadoop-daemon.sh start datanode".format(p,ip,tlv))
			TTserviceStart=commands.getstatusoutput("sudo sshpass -p {0} ssh -o strictHostKeyChecking=no {1} docker exec Dock{2} hadoop-daemon.sh start tasktracker".format(p,ip,tlv))	
			if DNserviceStart[0]==0 and TTserviceStart[0]==0 :
				print "<br/><i>->"
				print "Datanode and Task tracker started successfully ."
				print "</i>"
			else:
				print "<br/><i>->"
				print "<h2><font color='red'>!!No  datanode and tasktracker started successfully ..</font></h2>"
				print "</i>"
		else:
			print "<br/><i>->"
			print "<h2><font color='red'>!!LV is not mounted successfully...So no further processing!!!</font></h2>"
			print "</i>"
	else:
		print "<h2><font color='red'>!!No directory is created inside media folder ...Nothing to do!!</font></h2>"

	tlv=tlv+1

