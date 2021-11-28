"""Importing the necesssary libaries"""

#import pty
import subprocess #allows commands to be run in python



class GeneralPrivEsc(): #A class that contians general Privilage Escalation info without executing a command
    """Execute the privelege escalation/enumeration, dropping the user
        into a shell or displaying collected info."""
    def __init__(self, name, author, description): #function that takes in the name of privalage escalation method authior of who created it and
# a descripton of what the privilage escalation does
        self.name=name
        self.author=author
        self.description=description
    def info(self): #gives out the relevant information about the privilage escalation currenlty being run
        """Return useful information on the plugin, suitable for the user to
        read"""
        return f"{self.name}, by {self.author},  {self.description}"
class PrivEsc(): #A class that contians general Privilage Escalation info inlcuding executing a command
    """Execute the privelege escalation/enumeration, dropping the user
        into a shell or displaying collected info."""
    def __init__(self, command):
        self.command=command
    def execute(self): #function that takes in the command used for the privilage escalation
        file_log=open("log","a") #opens/creates a log file to append assigned to a variable
        information=subprocess.run(self.command, shell=True) #runs the command given ina shell assighning it to a variable
        file_log.write(str(information)+"\n") #writes the command to a the log file
        file_log.close() #cloes the file
        """Execute the privelege escalation/enumeration, dropping the user
        into a shell or displaying collected info."""

class Enumeration(): #A class that contians general Enumeration info including executing a command
    """A generic privelege enumeration class. Include common
    functionality here"""
    def __init__(self, name, author, description, command): #function that takes in the name of the enumeration method author of who created it and
# a descripton of what enumeratiob does with the command executed
        self.name=name
        self.author=author
        self.description=description
        self.command=command
    def execute(self): #function that takes in the command used for the enumeration
        file_log=open("log","a") #opens/creates a log file to append assigned to a variable 
        information=subprocess.run(self.command, shell=True) #runs the command given ina shell assighning it to a variable
        file_log.write(str(information)+"\n")  #writes the command to a the log file
        file_log.close() #closes the file
    def info(self): #gives out the relevant information about the privilage escalation currenlty being run
        """Return useful information on the plugin, suitable for the user to
        read"""
        return f"{self.name}, by {self.author},  {self.description}"

