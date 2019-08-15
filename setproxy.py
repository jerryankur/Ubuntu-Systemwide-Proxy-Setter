#This code is written by Priyanshu Dwivedi, Indian Institute of Information Technology, Design and Manufacturing, Jabalpur
#Source: https://github.com/coderpd/Ubuntu-Systemwide-Proxy-Setter
print("=======================================================================================")
print("WARNING: This script will touch system variables proceed with your own risk!")
print("Note: Leave the username and password empty if your proxy doesn't need credentials")
print("Note: This script will change the system variables to use proxy, browsers uses gsetting")
print("proxy. To use the proxy in browser, put the same proxy also in Settings by yourself")
print("=======================================================================================")
print("\n\t\t\tPROXY SETTER")
print("\n1) Press 1 to set proxy to system variables")
print("2) Press 2 to remove proxy from system variables")
print("0) Press 0 to exit")
inp=input("\tInput: ")
if inp==1:
    print("importing system")
    import sys
    import re
    import fileinput
    print("importing os")
    import os

    proxy=raw_input("\n\tHost: ")
    port=raw_input("\tPort: ")
    user=raw_input("\tUsername: ")
    password=raw_input("\tPassword: ")
    print("\ntouching apt configurations")
    os.system('sudo touch /etc/apt/apt.conf')
    if len(user)>0:
        flag = 0
        print("modifying environment variables")
        for line in fileinput.input("/etc/environment", inplace=1):
            if "proxy" in line:
                flag = 1
                line = re.sub(r'(.*)_proxy=(.*)', r'\1_proxy="\1://'+user+':'+password+'@'+proxy+':'+port+"/\"\n", line.rstrip())
            sys.stdout.write(line)

        if flag == 0:
            file1 = open("/etc/environment", "w")
            file1.write("PATH=\"/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games\"\n")
            file1.write("http_proxy=\"http://"+user+":"+password+"@"+proxy+":"+port+"/\"\n")
            file1.write("https_proxy=\"https://"+user+":"+password+"@"+proxy+":"+port+"/\"\n")
            file1.write("ftp_proxy=\"ftp://"+user+":"+password+"@"+proxy+":"+port+"/\"\n")
            file1.write("socks_proxy=\"socks://"+user+":"+password+"@"+proxy+":"+port+"/\"\n")
            file1.close()

        flag = 0
        print("modifying apt configurations")
        for line in fileinput.input("/etc/apt/apt.conf", inplace=1):
            if "Acquire::" in line and "Cache" not in line:
                flag = 1
                line = re.sub(r'Acquire::(.*)::proxy (.*)', r'Acquire::\1::proxy "\1://'+user+":"+password+"@"+proxy+":"+port+"/\";\n", line.rstrip())
            sys.stdout.write(line)

        if flag == 0:
            file1 = open("/etc/apt/apt.conf", "w")
            file1.write("Acquire::http::proxy \"http://"+user+":"+password+"@"+proxy+":"+port+"/\";\n")
            file1.write("Acquire::https::proxy \"https://"+user+":"+password+"@"+proxy+":"+port+"/\";\n")
            file1.write("Acquire::ftp::proxy \"ftp://"+user+":"+password+"@"+proxy+":"+port+"/\";\n")
            file1.write("Acquire::http::No-Cache \"True\";\n")
            file1.write("Acquire::socks::proxy \"socks://"+user+":"+password+"@"+proxy+":"+port+"/\";\n")
            file1.close()

        flag = 0
        print("modifying bash variables")
        for line in fileinput.input("/etc/bash.bashrc", inplace=1):
            if "export" in line:
                flag = 1
                line = re.sub(r'export (.*)_proxy=(.*)', r'export \1_proxy=\1://'+user+':'+password+'@'+proxy+':'+port+'\n', line.rstrip())
            sys.stdout.write(line)

        if flag == 0:
            file1 = open("/etc/bash.bashrc", "r+")
            l=file1.readlines()
            file1.close()
            file1 = open("/etc/bash.bashrc", "a")
            if not l[-1][-1]=='\n':
                file1.write("\n")
            file1.write("export http_proxy=http://"+user+":"+password+"@"+proxy+":"+port+"\n")
            file1.write("export https_proxy=https://"+user+":"+password+"@"+proxy+":"+port+"\n")
            file1.write("export ftp_proxy=ftp://"+user+":"+password+"@"+proxy+":"+port+"\n")
            file1.close()


        flag = 0
        print("modifying wgetrc variables")
        for line in fileinput.input("/etc/wgetrc", inplace=1):
            if not line.startswith("#") and "proxy" in line:
                flag = 1
                line = re.sub(r'(.*)_proxy=(.*)//(.*)', r'\1_proxy=\1://'+user+':'+password+'@'+proxy+':'+port+'\n', line.rstrip())
            sys.stdout.write(line)

        if flag == 0:
            file1 = open("/etc/wgetrc", "r+")
            l=file1.readlines()
            file1.close()
            file1 = open("/etc/wgetrc", "a")
            if not l[-1][-1]=='\n':
                file1.write("\n")
            file1.write("http_proxy=http://"+user+":"+password+"@"+proxy+":"+port+"\n")
            file1.write("https_proxy=https://"+user+":"+password+"@"+proxy+":"+port+"\n")
            file1.write("ftp_proxy=ftp://"+user+":"+password+"@"+proxy+":"+port+"\n")
            file1.close()

    else:
        flag = 0
        print("modifying environment variables")
        for line in fileinput.input("/etc/environment", inplace=1):
            if "proxy" in line:
                flag = 1
                line = re.sub(r'(.*)_proxy=(.*)', r'\1_proxy="\1://'+proxy+':'+port+"/\"\n", line.rstrip())
            sys.stdout.write(line)

        if flag == 0:
            file1 = open("/etc/environment", "w")
            file1.write("PATH=\"/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games\"\n")
            file1.write("http_proxy=\"http://"+proxy+":"+port+"/\"\n")
            file1.write("https_proxy=\"https://"+proxy+":"+port+"/\"\n")
            file1.write("ftp_proxy=\"ftp://"+proxy+":"+port+"/\"\n")
            file1.write("socks_proxy=\"socks://"+proxy+":"+port+"/\"\n")
            file1.close()

        flag = 0
        print("modifying apt configurations")
        for line in fileinput.input("/etc/apt/apt.conf", inplace=1):
            if "Acquire::" in line and "Cache" not in line:
                flag = 1
                line = re.sub(r'Acquire::(.*)::proxy (.*)', r'Acquire::\1::proxy "\1://'+proxy+":"+port+"/\";\n", line.rstrip())
            sys.stdout.write(line)

        if flag == 0:
            file1 = open("/etc/apt/apt.conf", "w")
            file1.write("Acquire::http::proxy \"http://"+proxy+":"+port+"/\";\n")
            file1.write("Acquire::https::proxy \"https://"+proxy+":"+port+"/\";\n")
            file1.write("Acquire::ftp::proxy \"ftp://"+proxy+":"+port+"/\";\n")
            file1.write("Acquire::http::No-Cache \"True\";\n")
            file1.write("Acquire::socks::proxy \"socks://"+proxy+":"+port+"/\";\n")
            file1.close()

        flag = 0
        print("modifying bash variables")
        for line in fileinput.input("/etc/bash.bashrc", inplace=1):
            if "export" in line:
                flag = 1
                line = re.sub(r'export (.*)_proxy=(.*)', r'export \1_proxy=\1://'+proxy+':'+port+'\n', line.rstrip())
            sys.stdout.write(line)

        if flag == 0:
            file1 = open("/etc/bash.bashrc", "r+")
            l=file1.readlines()
            file1.close()
            file1 = open("/etc/bash.bashrc", "a")
            if not l[-1][-1]=='\n':
                file1.write("\n")
            file1.write("export http_proxy=http://"+proxy+":"+port+"\n")
            file1.write("export https_proxy=https://"+proxy+":"+port+"\n")
            file1.write("export ftp_proxy=ftp://"+proxy+":"+port+"\n")
            file1.close()


        flag = 0
        print("modifying wgetrc variables")
        for line in fileinput.input("/etc/wgetrc", inplace=1):
            if not line.startswith("#") and "proxy" in line:
                flag = 1
                line = re.sub(r'(.*)_proxy=(.*)//(.*)', r'\1_proxy=\1://'+proxy+':'+port+'\n', line.rstrip())
            sys.stdout.write(line)

        if flag == 0:
            file1 = open("/etc/wgetrc", "r+")
            l=file1.readlines()
            file1.close()
            file1 = open("/etc/wgetrc", "a")
            if not l[-1][-1]=='\n':
                file1.write("\n")
            file1.write("http_proxy=http://"+proxy+":"+port+"\n")
            file1.write("https_proxy=https://"+proxy+":"+port+"\n")
            file1.write("ftp_proxy=ftp://"+proxy+":"+port+"\n")

    print("\t\t---Systemwide Proxy set---")
    print("Please reboot your system now")
elif inp==2:
    print("modifying bash variables")
    with open("/etc/bash.bashrc","r+") as f:
        new_f = f.readlines()
        f.seek(0)
        for line in new_f:
            if "export http_proxy" not in line and "export https_proxy" not in line and "export ftp_proxy" not in line and "export socks_proxy" not in line:
                f.write(line)
        f.truncate()
        f.close()

    print("modifying wgetrc variables")
    with open("/etc/wgetrc","r+") as f:
        new_f = f.readlines()
        f.seek(0)
        for line in new_f:
            if "http_proxy" not in line and "https_proxy" not in line and "ftp_proxy" not in line and "socks_proxy" not in line:
                f.write(line)
        f.truncate()
        f.close()

    print("modifying environment variables")
    with open("/etc/environment","r+") as f:
        new_f = f.readlines()
        f.seek(0)
        for line in new_f:
            if "http_proxy" not in line and "https_proxy" not in line and "ftp_proxy" not in line and "socks_proxy" not in line:
                f.write(line)
        f.truncate()
        f.close()

    print("modifying apt variables")
    with open("/etc/apt/apt.conf","r+") as f:
        new_f = f.readlines()
        f.seek(0)
        for line in new_f:
            if "Acquire::http" not in line and "Acquire::https" not in line and "Acquire::ftp" not in line and "Acquire::socks" not in line:
                f.write(line)
        f.truncate()
        f.close()

    print("modification completed...Proxy unset completed\nPlease reboot your system now")
elif inp==0:
    print("exiting script")
else:
    print("Wrong Input\nexiting script")
print("\n\n\t---programmed by PD")