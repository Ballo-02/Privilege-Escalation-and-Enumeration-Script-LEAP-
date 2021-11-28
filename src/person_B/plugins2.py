""" Template classes for plugins and useful functions """

import pty
import subprocess
import os, tempfile
from consolemenu import Screen


## A couple of optional super classes and a general item class to represent them more abstractly
## Can be used to add common functionality to privesc/enumeration plugins

class Item:
    """A generic privelege escalation/enumeration class. Include common
    functionality here"""
    def __init__(self, name, author, description, command):
        self.name=name
        self.author=author
        self.description=description
        self.command=command
    def execute(self):
        information=subprocess.run(self.command, shell=True)
        """Execute the privelege escalation/enumeration, dropping the user
        into a shell or displaying collected info.
        """
        print("This should be overridden in your plugin")

    def info(self):
        """Return useful information on the plugin, suitable for the user to
        read"""
        return f"{self.name}, by {self.author}.  {self.description}"

class PrivEsc_B(Item):
    pass

class Enumeration_B(Item):
    pass
