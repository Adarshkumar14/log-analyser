import os
file1=open("/root/log_analysis/workspace/malicious_ip.txt","r")
y=file1.read().splitlines()
file1.close()
for x in y:
 os.system("sudo iptables -A  INPUT -s 'x'  -j DROP")

print('completed')
