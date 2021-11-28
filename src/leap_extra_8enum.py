##!/usr/bin/env python3

from js_plugins import *
from consolemenu import *
from consolemenu.items import *
from plugins import *

if __name__=="__main__":
    print("")
# Import the necessary packages
def privilage_escalation(choose_privilage):
    if (choose_privilage == 1):
        cheese()
def enumeration(choose_enumeration):
    if (choose_enumeration == 1):
        group_A()
    elif (choose_enumeration == 2):
        OS_A()
    elif (choose_enumeration == 3):
        SUID_SGID_A()
    elif (choose_enumeration == 4):
        users_A()
    elif (choose_enumeration == 5):
        networks_A()
    elif (choose_enumeration == 6):
        login_user_A()
    elif (choose_enumeration == 7):
        services_A()
    elif (choose_enumeration == 8):
        programs_A()


def menu():
# Create the menu
    menu = ConsoleMenu("LEAP Project", "")

    enumA= FunctionItem("Group Enumeration    - Person A", enumeration, [1])
    enumB= FunctionItem("Operating System     - Person A", enumeration, [2])
    enumC= FunctionItem("SUID and SGID        - Person A", enumeration, [3])
    enumD= FunctionItem("Users                - Person A", enumeration, [4])
    enumE= FunctionItem("Networks             - Person A", enumeration, [5])
    enumF= FunctionItem("Logged in User/Group - Person A", enumeration, [6])
    enumG= FunctionItem("Services    -        - Person A", enumeration, [7])
    enumH= FunctionItem("Programs    -        - Person A", enumeration, [8])


    privescA= FunctionItem("Privilage Escalation -Person A", privilage_escalation, [1])
    privescB= FunctionItem("Privilage Escalation -Person B", privilage_escalation, [2])
    privescC= FunctionItem("Privilage Escalation -Person C", privilage_escalation, [3])

    privesc_menu = ConsoleMenu("Privilage Escalation","Choice")
    privesc_menu.append_item(privescA)
    privesc_menu.append_item(privescB)
    privesc_menu.append_item(privescC)



    enum_menu = ConsoleMenu("Enumerations", "Choice")
    enum_menu.append_item(enumA)
    enum_menu.append_item(enumB)
    enum_menu.append_item(enumC)
    enum_menu.append_item(enumD)
    enum_menu.append_item(enumE)
    enum_menu.append_item(enumF)
    enum_menu.append_item(enumG)
    enum_menu.append_item(enumH)


# MenuItem is the base class for all items, it doesn't do anything when selected

    enum_menu= SubmenuItem("Enumeration", enum_menu, menu)
    privesc_menu=SubmenuItem("Privilage Escalation", privesc_menu, menu)

# Once we're done creating them, we just add the items to the menu
    menu.append_item(enum_menu)
    menu.append_item(privesc_menu)
#    menu.append_item(git_users)

# Finally, we call show to show the menu and allow the user to interact
    menu.show()
menu()
