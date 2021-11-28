##!/usr/bin/env python3

"""Importing the necesssary files"""

from ob_plugins import * #importing everything from the 'ob_plugins.py' so my plugin functions can be called
import sys #importing the 'sys' module to allow paramters to be passed
from consolemenu import * #importing all the console menu functions to make a more user friendly menu
from consolemenu.items import *
from person_B.plugins2 import *
from person_B.plugins_B import *
from person_C.plugins_mg import *
from person_D.plugins3 import *
from person_D.ms_plugins import *




def privilage_escalation(choose_privilage): #function that takes in the input from the privilage escalation menu
    if (choose_privilage == 1):
        PrivEscA.copy_passwd_A_linux()
    elif (choose_privilage  == 2):
        PrivEsc_B1().execute()
    elif (choose_privilage  == 3):
        Privesc_C1.create_vuln()
        Privesc_C1.execute()
    elif (choose_privilage  == 4):
        EmacsPrivEsc().run()
    elif (choose_privilage  == 5):
        emacsPrivEsc.run()


def enumeration(choose_enumeration): #function that takes in the input from the privilage escalation menu
    if (choose_enumeration == 1):
        EnumA.services_A_linux()
    elif (choose_enumeration == 2):
        EnumA.services_A_windows()
    elif (choose_enumeration == 3):
        EnumA.programs_A_linux()
    elif (choose_enumeration == 4):
        Enumeration_B1().execute()
    elif (choose_enumeration == 5):
        Enumeration_B2().execute()
    elif (choose_enumeration == 6):
        Enumeration_C2.env_info()
    elif (choose_enumeration == 7):
        Enumeration_C3.interesting_files()
    elif (choose_enumeration == 8):
        ListUsers().run()
    elif (choose_enumeration == 9):
        EtcEnum().run()
    elif (choose_enumeration == 10):
        EnumA.os()



def menu(): #function that is called to activate the menu
# Create the menu
    menu = ConsoleMenu("LEAP Project", "") #Creates a menu with a title 'LEAP Project' with an empty subtitle

    """Displays what function will be executed 'Services' with what operating system it works on
    'L' for Linux and 'W' for Windows which user created it 'Person A' (what are assigned in the 'README' file)
    the functions name to be called with the suitbale paramter to be passed to it"""


    enumA= FunctionItem("Services        L      - Person A", enumeration, [1]) #used in the example^
    enumB= FunctionItem("Services        W      - Person A", enumeration, [2])
    enumC= FunctionItem("Programs        L      - Person A", enumeration, [3])
    enumD= FunctionItem("SUID & SGID     L      - Person B", enumeration, [4])
    enumE= FunctionItem("Networks        L      - Person B", enumeration, [5])
    enumF= FunctionItem("Enviroment Info L      - Person C", enumeration, [6])
    enumG= FunctionItem("Senstive Files  L      - Person C", enumeration, [7])
    enumH= FunctionItem("List Users      L      - Person D", enumeration, [8])
    enumI= FunctionItem("Bin files       L      - Person D", enumeration, [9])
    enumJ= FunctionItem("OS             W/L     - Person D", enumeration, [10])



    """Displays what function will be executed 'Create Malicous passwd file' with what operating system
    it works on  'L' for Linux and 'W' for Windows which user created it "Person A" (what are assigned
    in the 'README' file) the functions name to be called with the suitbale paramter to be passed to it"""

    privescA= FunctionItem("Create Malicous passwd file L -Person A", privilage_escalation, [1]) #used in the example^
    privescB= FunctionItem("dd in binary to read shadow l -Person B", privilage_escalation, [2])
    privescC= FunctionItem("Python Vulnerability        l -Person C", privilage_escalation, [3])
    privescD= FunctionItem("Emacs Vulnerabilty          l -Person D", privilage_escalation, [4])



    privesc_menu = ConsoleMenu("Privilage Escalation","Choice") #Creates a menu with a title 'Privilage Escalation' with 'Choice' as a subtitle

    """Adds the variables such as 'privescA' to the privilage escalation menu named 'privesc_menu'"""

    privesc_menu.append_item(privescA) #used in the example^
    privesc_menu.append_item(privescB)
    privesc_menu.append_item(privescC)
    privesc_menu.append_item(privescD)



    enum_menu = ConsoleMenu("Enumerations", "Choice")  #Creates a menu with a title 'Enumeration' with 'Choice'  as a subtitle


    """Adds the variables such as 'enumA' to the enumeration menu named 'enum_menu'"""


    enum_menu.append_item(enumA) #used in the example^
    enum_menu.append_item(enumB)
    enum_menu.append_item(enumC)
    enum_menu.append_item(enumD)
    enum_menu.append_item(enumE)
    enum_menu.append_item(enumF)
    enum_menu.append_item(enumG)
    enum_menu.append_item(enumH)
    enum_menu.append_item(enumI)
    enum_menu.append_item(enumJ)


    """Creates the submenu's"""

    enum_menu= SubmenuItem("Enumeration", enum_menu, menu) #creates the submenu 'enum_menu' with the title 'Enumeration' that is linked to the main
# 'menu' therefore is displayed there
    privesc_menu=SubmenuItem("Privilage Escalation", privesc_menu, menu) #creates the submenu 'privesc_menu' with the title 'Privilage Escalation'
# that is link'menu' therefore is displayed therefore displayed to the main

    """Adds the variables such as 'enum_menu' to the main menu named 'menu'"""
    menu.append_item(enum_menu) #used in the example
    menu.append_item(privesc_menu)


    menu.show() #displays the final menu

if __name__=="__main__": #runs everytime 
    parameters=(sys.argv) #creates a variable that is equal to what the parameters given
    system=platform.system() #cretaes a variable that is the system type
    if (len(parameters) == 2): #checks if a parameter is given or blank
        del parameters[0] #deletes the default o position of argv
    else:
        menu() #starts the menu
    if (system == "Linux"): #checks of the current operating system is linux to only use linux commands
        if (parameters[0] == "enumerate"): #executes all the enumarations if the parameter is 'enumerate'
            EnumA.services_A_linux()
            EnumA.programs_A_linux()
            EnumA.os_A()
        elif (parameters[0] == "privesc"):
            PrivEscA.copy_passwd_A_linux() #runs copy_shadow function that uses a privilage escalation emthod to get into the shell
        elif (parameters[0] == "services"):
            EnumA.services_A_linux() #runs services function telling us what servcies are currenlty running
        elif (parameters[0] == "programs"):
            EnumA.programs_A_linux() #runs program function showing what programs are installed
        elif (parameters[0] == "os"):
            EnumA.os_A() #runs the os function telling us the current operating system
        elif (parameters[0] == "copy_passwd"):
            PrivEscA.copy_passwd_A_linux()
        else:
            menu() #starts the menu
    elif (system == "Windows"): #checks of the current operating system is windows to only use linux commands
        if (parameters[0] == "enumerate"): #executes all the enumarations if the parameter is 'enumerate'
            EnumA.services_A_windows()
        elif (parameters[0] == "privesc"):
            print("")
        elif (parameters[0] == "services"):
            EnumA.services_A_windows() #runs services function telling us what servcies are currenlty running
        else:
            menu() #starts the menu
