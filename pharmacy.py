import sys
import os
import pymysql

py = sys.executable


def back():
    os.system('%s %s' % (py, 'main.py'))


def addPharmacy():
    try:
        conn = pymysql.connect(host="localhost", user="root", password="", database="stock")

        myCursor = conn.cursor()
        pmc_name = input("Enter the Pharmacy Name: ")
        pmc_address = input("Enter the Pharmacy Address: ")
        pmc_phone = input("Enter the Pharmacy phone No: ")

        myCursor.execute("Insert into pharmacy(pmc_name,pmc_address,pmc_phone) values (%s,%s,%s)",
                         [pmc_name, pmc_address, pmc_phone])
        conn.commit()
        print("Pharmacy added Successfully")

    except:
        print("Something goes wrong")


def removePharmacy():
    a = input("Enter Pharmacy Name to remove: ")
    try:
        conn = pymysql.connect(host="localhost", user="root", password="", database="stock")
        myCursor = conn.cursor()
        myCursor.execute("Delete from Pharmacy where pmc_name = %s", [a])
        conn.commit()
        myCursor.close()
        conn.close()
        print("\t\Pharmacy Removed Successfully")
        a.set("")
    except:
        print("")


def viewPharmacy():
    try:
        conn = pymysql.connect(host="localhost", user="root", password="", database="stock")
        myCursor = conn.cursor()
        myCursor.execute("Select * from pharmacy")

        conn.commit()
        myresult = myCursor.fetchall()

        for x in myresult:
            print(x)
        myCursor.close()
        conn.close()

    except:
        print("")


while True:
    print('-----------------------------------------------------------')
    print('1.Add Pharmacy \n2.Remove Pharmacy\n3.View Pharmacy\n4.Back To Menu')
    print('-----------------------------------------------------------')
    choice = input('Enter the number of your choice : ')
    print('-----------------------------------------------------------')

    if choice == '1':
        print('----------------------Add Pharmacy--------------------')
        addPharmacy()
        print('------------------------------------------------------')


    elif choice == '2':
        print('--------------------Remove Pharmacy------------------')
        removePharmacy()
        print('------------------------------------------------------')


    elif choice == '3':
        print('------------------View Pharmacies----------------------')
        viewPharmacy()
        print('------------------------------------------------------')


    elif choice == '4':
        back()
        break

    else:
        print('You entered an invalid option')


#   MN Firnas Ahamed
#   Reg 519217071
#   EEX4347 - Mini Project
#   Kandy Regional Centre