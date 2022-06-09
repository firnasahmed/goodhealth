import os
import sys

py = sys.executable

def pmc():
    os.system('%s %s' % (py, 'pharmacy.py'))

def m():
    os.system('%s %s' % (py, 'stock.py'))

def p():
    os.system('%s %s' % (py, 'invoice.py'))

def c():
    os.system('%s %s' % (py, 'customer.py'))

def s():
    os.system('%s %s' % (py, 'supplier.py'))

def ctr():
    os.system('%s %s' % (py, 'contracts.py'))

def h():
    os.system('%s %s' % (py, 'helpMenu.py'))


while True:
    print('----------------Welcome to the Good Health Company---------------')

    print('1.Pharmacy\n2.Drugs (Medicine)\n3.Purchase\n4.Customer \n5.Supplier\n6.Contracts\n7.Help\n8.Exit')
    print('------------------------------------------------------')
    choice = input('Enter the number of your choice : ')
    print('------------------------------------------------------')

    if choice == '1':
        pmc()
    elif choice == '2':
        m()
    elif choice == '3':
        p()
    elif choice == '4':
        c()
    elif choice == '5':
        s()
    elif choice == '6':
        ctr()
    elif choice == '7':
        h()
    elif choice == '8':
        print('----------------------exited--------------------------')
        break


    else:
        print('You entered an invalid option')


#   MN Firnas Ahamed
#   Reg 519217071
#   EEX4347 - Mini Project
#   Kandy Regional Centre