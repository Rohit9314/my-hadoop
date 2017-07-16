# My-Hadoop
High Performance Distributed Computing for Big Data Using Hadoop Framework and running applications on large clusters, Containerized Docker Engine using Python , ansible, YAML, JSON, HTML, CSS
## Getting Started
In order to run hadoop setup first write your ip address in browser followed by '/login.html' and type username and password which can be set according to your choice in 'login.py' file manually.

Now choose the type of hadoop cluster you want to setup i.e., manual setup in which every thing will be entered according to user's wish or on-demand setup where user has to just fill the  input boxes according to his requirements and everything will be setup automatically inside *dockers*.

### *Prerequisites*
    1. Redhat Linux with Jq(for json), ansible, Hadoop and JDk installed .
    2. A VG with name 'myvg' of atleast 2Gb in size.
    3. Docker setup and  loaded image of  os 'centos'.  
    4. Install ssh service , Hadoop version 1 and JDk installed inside centos and  commit a new image of this centos with name 'os:v5'.
    5. Add a hostname and ip in '[web]' in '/etc/ansible/hosts' file
#### Note:
**In on-demand setup a LV  will be created from 'myvg' VG on the system (let's say main system) whose hostname and ip is set in '/etc/ansible/hosts' file and will be shared to the system where you are setting Docker setup  through NFS server. This will create entry in 'fstab' file of  main system. **
**So if you remove th LV, you need to  remove entry from fstab file otherwise your system will be corrupted (but can be repair ).**
