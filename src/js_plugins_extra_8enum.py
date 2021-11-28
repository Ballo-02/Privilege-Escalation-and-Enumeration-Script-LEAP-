""" Plugins for LEAP designed by James Shuttleworth """

from plugins import PrivEsc, Enumeration

import os, tempfile

from subprocess import Popen, PIPE

import pty

from consolemenu import Screen

# A very basic method, but useful
def shellRun(command):
    """ Put given commands into a temporary file, spawn a shell and explain how to use the command """
    f = tempfile.NamedTemporaryFile(delete=False)
    fname=f.name
    f.write(command.encode())
    f.close()
    os.system(f"chmod u+x {fname}")
    print(f"Execute command with '{fname}'...\nCtrl-D to leave shell")
    
    pty.spawn("/bin/bash")
    #os.system(fname)
    os.unlink(fname)


class DumbSudoEscalation(PrivEsc):
    """An example plugin that tries to use `sudo su` to get root. 

    Requires being given the password for the current user and relies
    on the current user having sudo privs, so while technically it
    escalates proveleges, it does so only if you already have the
    right credentials

    """
    def __init__(self, pw):
        PrivEsc.__init__(self)
        self.pw=pw
        self.name="DumbSudoEscalation - not that useful"
        self.author="James Shuttleworth"
        self.description="Use sudo to 'hack' into the root account"
    def execute(self):
        print("Executing")
        shellRun("sudo xterm")
        print("Done")
def group_A():
    Screen().input("press any key")
    enumcommand=Enumeration("Group Enumeration", "Owen Ball", "lists group", "cat /etc/group")
    print(enumcommand.info())
    Screen().input("press any key ")
    enumcommand.execute()
    Screen().input("press any key")
def OS_A():
    Screen().input("press any key")
    enumcommand=Enumeration("Operating System", "Owen Ball", "Tells the user the operating system", "uname -a")
    print(enumcommand.info())
    Screen().input("press any key ")
    enumcommand.execute()
    Screen().input("press any key")
def SUID_SGID_A():
    Screen().input("press any key")
    enumcommand=Enumeration("SUID and SGID", "Owen Ball", "Lists out all the SUID and SGID files", "find / -perm /6000 2>/dev/null;")
    print(enumcommand.info())
    Screen().input("press any key ")
    enumcommand.execute()
    Screen().input("press any key")
def users_A():
    Screen().input("press any key")
    enumcommand=Enumeration("Users Enumeration", "Owen Ball", "Lists the Users", "ls -al")
    print(enumcommand.info())
    Screen().input("press any key ")
    enumcommand.execute()
    Screen().input("press any key")
def login_user_A():
    Screen().input("press any key")
    enumcommand=Enumeration("Logged in user", "Owen Ball", "Displays the current user and group", "id")
    print(enumcommand.info())
    Screen().input("press any key ")
    enumcommand.execute()
    Screen().input("press any key")
def services_A():
    Screen().input("press any key")
    enumcommand=Enumeration("Services", "Owen Ball", "Which services are running", "ps aux")
    print(enumcommand.info())
    Screen().input("press any key ")
    enumcommand.execute()
    Screen().input("press any key")
def programs_A():
    Screen().input("press any key")
    enumcommand=Enumeration("Programs installed", "Owen Ball", "What programs are installed", "dpkg -l")
    print(enumcommand.info())
    Screen().input("press any key ")
    enumcommand.execute()
    Screen().input("press any key")
def networks_A():
    Screen().input("press any key")
    enumcommand=Enumeration("Network", "Owen Ball", "What network interface controller are being used", "ifconfig -a")
    print(enumcommand.info())
    Screen().input("press any key ")
    enumcommand.execute()
    Screen().input("press any key")
#class PrivSec1(PrivEsc)
#    def __init__(self):
#        self.name=name
#        self.author=author
#        self.description=description
#    def execute(self):
        
