#!/usr/bin/python3

#Author: Nicholas Graca
#A script for managing virtualbox VMs
#Actions you can do:
#   Start, Stop, Create, Delete, list settings, list available VMs

import os


def create():
    name = input("What would you like to name your new VM? ")
    OpSys = input("What OS is " + name + " going to be? ")
    path = input("What is the path to " + OpSys + "?")
    ram = input("How much RAM would you like " + name + " to have?")
    os.system('vboxmanage createvm --name ' + name + ' --ostype ' + OpSys + ' --register')
    os.system('vboxmanage storagectl ' + name + ' --name IDE --add ide')
    os.system('vboxmanage modifyvm ' + name + ' --memory ' + ram)
    os.system('vboxmanage storageattach ' + name + ' --storagectl IDE --port 0 --device 0 --type dvddrive --medium ' + path)

def showOptions():
    detail = ''
    while detail not in 'YN':
        detail = input("Would you like a more detailed list? [y/n]: ").upper()
        if var == 'Y':
            os.system('vboxmanage list vms --long')
        if var == 'N':
            os.system('vboxmanage list vms')

def start(vm):
    os.system('vboxmanage startvm ' + vm)

def stop(vm):
    os.system('vboxmanage controlvm ' + vm + ' poweroff soft')

def showSettings(vm):
    os.system('vboxmanage showvminfo ' + vm)

def delete(vm):
    os.system('vboxmanage unregistervm ' + vm + ' --delete')




def main():
    opt = ''
    while(opt != 'Q'):
        print('\n#########################')
        print('|(A) : Create VM        |')
        print('|(B) : List all VMs     |')
        print('|(C) : Start VM         |')
        print('|(D) : Stop VM          |')
        print('|(E) : Show VM Settings |')
        print('|(F) : Delete VM        |')
        print('|(Q) : Quit             |')
        print('#########################\n')
        
        opt = input("What would you like to do?")
        opt = opt.upper()

        if opt not in 'ABCDEFQ':
            print("\nOption entered is INVALID, please try again.")
        
        elif opt == 'A':
            create()

        elif opt == 'B':
            showOptions()

        elif opt == 'C':
            vm = input('What VM are you talking about? ')
            start(vm)

        elif opt == 'D':
            vm = input('What VM are you talking about? ')
            stop(vm)

        elif opt == 'E':
            vm = input('What VM are you talking about? ')
            showSettings(vm)

        elif opt == 'F':
            vm = input('What VM are you talking about? ')
            delete(vm)

if __name__ == "__main__":
    main()

# SOURCE:
# https://www.virtualbox.org/manual/ch08.html