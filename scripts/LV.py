#!/usr/bin/python2

import commands

def lvc(LvNum,lvsize):
	LV_CREATE= """---
- hosts: web
  tasks:
   - name: Creating Lv
     lvol:
      vg: myvg
      lv: ansil{0}
      size: {1}g

   - name: Formatting LV
     filesystem: 
      fstype: ext4
      dev: /dev/myvg/ansil{2}

   - name: Mounting created lv
     mount:
      path: /media/Myansible/ansil{3}
      src: /dev/myvg/ansil{4}
      fstype: ext4
      state: mounted """.format(LvNum,lvsize,LvNum,LvNum,LvNum)
	chown=commands.getstatusoutput("sudo chown apache /webcontent/scripts/f.yml")
	if chown[0]==0:
		fh=open("/webcontent/scripts/f.yml", "w")
		fh.write(LV_CREATE)
		fh.close()
		lvstatus=commands.getstatusoutput("sudo ansible-playbook /webcontent/scripts/f.yml")
		if lvstatus[0]==0:
			print "<br/><br/><i>->" 
			print "lv created... "
			print "<br/></i>"
			chown2=commands.getstatusoutput("sudo chown apache /etc/exports")
			if chown2[0]==0:
				entry=commands.getstatusoutput("sudo  echo '/media/Myansible/ansil{0} *(rw,no_root_squash)'>> /etc/exports".format(LvNum))
				if entry[0]==0:
					print "<br/><i>->"
					print "entry done successfully..."
					print "<br/></i>"
				else:
					print "<h2><font color='red'>!!no entry done...</font></h2>"
			else:
				print "<h2><font color='red'>!!chown2 not done</font></h2>"
				
		else:
			print "<br/><i>->"
			print "First Create myvg--VG manually"
			print "<br/></i>"
	else:
		print "<br/><i>->"
		print "<h2><font color='red'>!!no fh...</font></h2>"
		print "</i>"


