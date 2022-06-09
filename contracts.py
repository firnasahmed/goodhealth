import sys
import os
import pymysql

py = sys.executable


def back():
    os.system('%s %s' % (py, 'main.py'))


def addContract():
    try:
        conn = pymysql.connect(host="localhost", user="root", password="", database="stock")

        myCursor = conn.cursor()
        pmcid = input("Contract Details - Enter the Pharmacy ID for this Agreement: ")
        supid = input("Contract Details - Enter the Supplier ID for this Agreement: ")
        sdate = input("Start Date of the Contract (YYYY-MM-DD): ")
        edate = input("End Date of the Contract (YYYY-MM-DD): ")
        details = input("Details: ")

        myCursor.execute("Insert into  contracts(pmc_code,s_id,start_date,end_date,details) values (%s,%s,%s,%s,%s)",
                         [pmcid, supid, sdate, edate, details])

        conn.commit()
        print("Contract added Successfully")

    except:
        print("Something goes wrong")


def removeContract():
    a = input("Enter Contract ID to remove:")
    try:
        conn = pymysql.connect(host="localhost", user="root", password="", database="stock")
        myCursor = conn.cursor()
        myCursor.execute("Delete from  contracts where 	cont_id = %s", [a])
        conn.commit()
        myCursor.close()
        conn.close()
        print("\t\tContract Removed Successfully")
        a.set("")
    except:
        print("")



def viewContract():
    try:
        conn = pymysql.connect(host="localhost", user="root", password="", database="stock")
        myCursor = conn.cursor()
        myCursor.execute("Select * from contracts")

        conn.commit()
        myresult = myCursor.fetchall()

        for x in myresult:
            print("Contract ID: ",x[0])
            print("Pharmacy ID of this Contract: ", x[1])
            print("Supplier ID of this Contract: ", x[2])
            print("Start Date of this Contract: ", x[3])
            print("End Date of this Contract: ", x[4])
            print("Details: ", x[5])
            print('========================================\n')
        myCursor.close()
        conn.close()

    except:
        print("")


while True:
    print('------------------------------------------------------')
    print('1.Add Contract \n2.View Contract\n3.Remove Contract\n4.Back To Menu')
    print('------------------------------------------------------')
    choice = input('Enter the number of your choice : ')
    print('------------------------------------------------------')

    if choice == '1':
        print('---------------------Add Contract---------------------')
        addContract()
        print('------------------------------------------------------')


    elif choice == '2':
        print('---------------------View Contract------------------')
        viewContract()
        print('------------------------------------------------------')

    elif choice == '3':
        print('------------------------Remove Contract----------------------')
        removeContract()
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