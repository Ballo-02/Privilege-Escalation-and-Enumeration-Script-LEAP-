"""Importing the necesssary files"""

import pytest, sys, os
sys.path.append("./src/") #so that the pytest knows when to find the tests
from leap import *
from ob_plugins import *
from plugins import *

test_file=open("testfile.txt","a")

"""testing each one of the enumerations privilage escalations as well as log files and peramters"""
def test_privesc_copy_passwd_linux():
    test_file.write(str(PrivEscA._test())) #writes the output to a file
    with open("testfile.txt") as f: #reads the first line of 'testfile.txt'
        first_line = f.readlines()
    assert first_line == ['None'] #checks if the commands has gone through

def test_enum_services_linux():
    test_file.write(str(EnumA._test("ps aux"))) #writes the output of the command to a file
    with open("testfile.txt") as f: #reads the first line of 'testfile.txt'
        first_line = f.readlines()
    assert first_line == ['None'] #checks if the commands has gone through


def test_enum_programs():
    test_file.write(str(EnumA._test("dpkg -l"))) #writes the output of the command to a file
    with open("testfile.txt") as f: #writes the output of the command to a file
        first_line = f.readlines()
    assert first_line == ['None'] #checks if the commands has gone through

#def test_enum_services_windows():
#    assert leap.dummyFunc(leap.unDummyFun
def test_log_file():
    try: #checks of the file exists by running an error as the script cant find it
        f = open("log")
        assert True==True
    except IOError:
        assert True==False

def test_parameter():
    carrot= (subprocess.run("python3 ./src/leap.py os", shell=True)) #runs a parameter command
    assert str(carrot) == "CompletedProcess(args='python3 ./src/leap.py os', returncode=1)" #checks if the right output is given


