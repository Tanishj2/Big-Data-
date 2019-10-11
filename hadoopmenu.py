import os
import signal		#signal is module which is used here to terminate with message
import getpass	#getpass is used here my password is not show on screen , and basically it is a module in python
import subprocess

def lw(x,y):
	print("good bye, c u next time")
	exit()
signal.signal(2,lw)	

apassword = 'redhat'
#password = input()
password = getpass.getpass("Enter your password::")

os.system("tput setaf 1")
print("\t\tWelcome to Create Hadoop Cluster\t\t")
os.system("tput setaf 0")
print("\t\t\t***************")

print("Some basis prerequisite steps you should follow for making hadoop cluster")
subprocess.getstatusoutput("tput setaf 5")
print("""
Press 1:to install JAVA JDK VERSION 8 for hadoop
Press 2:to install HADOOP Software VERSION 1 
Press 3:to check java and hadoop version
Press 4:to set unique name for master,slave ip
Press 5:to set slave configuration-
Press 6:to set master configuration-
Press 7:to set client configuration-
Press 8:to start hadoop datanode in SLave System
Press 9:to start hadoop namenode in Master System
Press 10:to send data/file/folder from Client System
Press 11:to read data from file/folder""")
subprocess.getstatusoutput("tput setaf 0")

print("Enter your choice")
ch = input()

if ch == "1":
	#Install JAVA JDK......
	print("I assume, you install the below version of JAVA JDK file:")
	print("To run/install the JDK use below command:")
	os.system("rpm -ivh /root/Desktop/jdk-8u171-linux-x64.rpm")
	print("Enter ip for Set JAVA_HOME variable Path for permanent:")
	ip = input()
	subprocess.getstatusoutput("scp .bashrc {}:/root/.bashrc".format(ip))
	
elif ch == "2":
	#Install HAdoop Software .....
	print("I assume, you install the below version of JAVA JDK file:")
	print("To run/install the hadoop software use below command:")
	os.system("rpm -ivh /root/Desktop/hadoop-1.2.1-1.x86_64.rpm --force")
 	
elif ch == "3":
	#Check Install or not.....
	ver1 = subprocess.getstatusoutput("java -version")	
	ver2 = subprocess.getstatusoutput("hadoop version")
	if ver1[0] == 0:
		print("JAva version install successfull")
	else: 
		print("Java version not install")
elif ch == "4":
	#Set IP with Name
	os.system("tput setaf 2")
	print("""You have to set NAME for IP that will be easy for identify network
	Give name according to yours IP using [vim /etc/hosts]cmd""")
	os.system("tput setaf 0")
	os.system("vim /etc/hosts")
elif ch == "5":
	#Slave Configuration............
	print("I'll share my slave configuration file that will be helpful for you")
	print("**Please NOTe that Change your IP in [core-site.xml] file using (vim core-site.xml) cmd****")
	print("Enter IP for set SLAVE configuration")	
	ip = input()
	ip1=input()
	os.system("scp /root/Desktop/config-file/slave-config.txt {}:/etc/hadoop/hdfs-site.xml".format(ip))
	os.system("scp /root/Desktop/config-file/master.txt {}:/etc/hadoop/core-site.xml".format(ip))	
	#os.system("scp /root/Desktop/config-file/data {}:/".format(ip))	
elif ch == "6":
	#MAster configuration...........
	print("I'll share my master configuration file that will be helpful for you")
	os.system("tput setaf 2")
	print("**Please NOTe that Change your IP in [core-site.xml] file using (vim core-site.xml) cmd****")
	os.system("tput setaf 0")
	print("Enter IP for set Master configuration")
	ip = input()
	os.system("scp /root/Desktop/config-file/master-config.txt {}:/etc/hadoop/hdfs-site.xml".format(ip))
	os.system("scp /root/Desktop/config-file/master.txt {}:/etc/hadoop/core-site.xml".format(ip))	
	#os.system("scp /root/Desktop/config-file/master {}:/".format(ip))
elif ch == "7":
	#Client Configuration..........
	print("I'll share my client configuration file that will be helpful for you")
	os.system("tput setaf 2")
	print("**Please NOTe that Change your IP in [core-site.xml] file using (vim core-site.xml) cmd****")
	os.system("tput setaf 0")
	print("Enter your IP to set Client Configuration")
	ip = input()
	os.system("scp /root/Desktop/config-file/master.txt {}:/etc/hadoop/core-site.xml".format(ip))	
elif ch == "8":
	print("enter two  ip")
	ip = input()
	ip1 = input()
	#So,we are done with configuration then we start datanode in Slave System here:-
	print("Starting datanode here-------")
	os.system("ssh {} iptables -F".format(ip))	#first we disabled firewall temporary
	#os.system("ssh {} mkdir /data".format(ip))
	os.system("ssh {} hadoop-daemon.sh start datanode".format(ip))
	os.system("ssh {} jps".format(ip))		#We check datanode is start or not
	os.system("ssh {} iptables -F".format(ip1))	#first we disabled firewall temporary
	os.system("ssh {} hadoop-daemon.sh start datanode".format(ip1))
	#os.system("ssh {} mkdir /data".format(ip))
	os.system("ssh {} jps".format(ip1))		#We check datanode is start or not
elif ch == "9":
	print("enter ip for master")
	ip = input()
	#So,we are done with configuration then we start namenode in Master System here:-
	print("Starting namenode here--------")
	#os.system("ssh {} hadoop namenode -format".format(ip))	#use only once 	
	os.system("ssh {} hadoop-daemon.sh start namenode".format(ip))
	os.system("ssh {} jps".format(ip))
	os.system("ssh {} hadoop dfsadmin -report".format(ip))
elif ch == "10":
	print("enter ip for client")
	ip = input()
	#Here we are sending files/folder to MAster:--
	print("Sending files/folder/data from CLient to MAster:--")
	print("Enter your file name you created")
	why = input() 
	os.system("ssh {} ls -lh why.txt".format(ip))		#to know file size 
	os.system("ssh {} hadoop fs -put why.txt /".format(ip))	#upload file to master
elif ch == "11":
	#Client can read file 
	os.system("hadoop fs -cat /f.txt")
else:
	print("Enter correct options")	
