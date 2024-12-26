"""
Customer Management System using Object-Oriented Programing (CMS using OOPS)
Perform CRUD Operation (Create, Read, Update, Delete)
    1. Add Customer
    2. Search Customer
    3. Delete Customer
    4. Edit Customer
    5. Display list of Customer
    6. Exit
"""
"Customer Management System using OOPS and Data stored in DataBase"
#Business Logic Layer:
import pymysql
import tkinter as tk
from tkinter import mainloop
class CustomerManagement:
    connection_=pymysql.connect(host="localhost",user="root",password="root2002",database="cms")
    cursor_=connection_.cursor()
    def __init__(self):
        "This is a constructor it calls automatically and make 4 variables in one location"
        self.id=0
        self.name=0
        self.age=0
        self.contact=0
    def addCustomer(self):
        "This method help to add new customers in DataBase"
        query_=f"insert into cmstb values('{self.id}','{self.name}','{self.age}','{self.contact}')"
        CustomerManagement.cursor_.execute(query_)
        CustomerManagement.connection_.commit()
    def searchCustomer(self):
        "This method help to find the index of input id"
        query_=f"select * from cmstb where id={self.id}"
        CustomerManagement.cursor_.execute(query_)
        data=CustomerManagement.cursor_.fetchone()
        self.name=data[1]
        self.age=data[2]
        self.contact=data[3]
    def deleteCustomer(self):
        "This method help to remove customer from DataBase"
        query_=f"delete from cmstb where id={self.id}"
        CustomerManagement.cursor_.execute(query_)
        CustomerManagement.connection_.commit()
    def editCustomer(self):
        "This method help to edit existed customer details"
        query_=f"update cmstb set name='{self.name}',age='{self.age}',mob='{self.contact}' where id={self.id}"
        CustomerManagement.cursor_.execute(query_)
        CustomerManagement.connection_.commit()
        return
# Presentation Layer:
def showCustomer(cms):
    "This method help to show data of one customer"
    print("Customer Id:", cms.id)
    print("Customer Name:", cms.name)
    print("Customer Age:", cms.age)
    print("Customer Contact No.:", cms.contact)

def displayCustomer():
    "This method directly display the data of all customer in GUI Window"
    query_=f"select * from cmstb"
    CustomerManagement.cursor_.execute(query_)
    customer_data=CustomerManagement.cursor_.fetchall()
    root=tk.Tk()
    root.title("Data of Customers")
    label_widget_1=tk.Label(root,text="Customer Id",font=1,bg="Light Blue",width="15")
    label_widget_1.grid(row=0,column=0)
    label_widget_2=tk.Label(root,text="Customer Name",font=1,bg="Light Blue",width="15")
    label_widget_2.grid(row=0, column=1)
    label_widget_3=tk.Label(root,text="Customer Age",font=1,bg="Light Blue",width="15")
    label_widget_3.grid(row=0, column=2)
    label_widget_4=tk.Label(root,text="Customer Contact No.",font=1,bg="Light Blue",width="20")
    label_widget_4.grid(row=0, column=3)
    r=1
    for tk_display in customer_data:
        label_widget_5=tk.Label(root,text=tk_display[0],font=1,bg="yellow",width="15")
        label_widget_5.grid(row=r,column=0)
        label_widget_6=tk.Label(root,text=tk_display[1],font=1,bg="yellow",width="15")
        label_widget_6.grid(row=r,column=1)
        label_widget_7=tk.Label(root,text=tk_display[2],font=1,bg="yellow",width="15")
        label_widget_7.grid(row=r,column=2)
        label_widget_8=tk.Label(root,text=tk_display[3],font=1,bg="yellow",width="20")
        label_widget_8.grid(row=r,column=3)
        r+=1

    for e in customer_data:
        print(f"Customer id:{e[0]} Customer Name:{e[1]} Customer Age:{e[2]} Customer Contact No.:{e[3]}")
    root.mainloop()

print("*** Welcome to using Chauhan Brothers Management System ***")
while(1):
    try:
        choice=input("""
        1. Add Customer
        2. Search Customer
        3. Delete Customer
        4. Edit Customer
        5. Display Data of Customer
        6. Exit
        =>Select any from above:""")
        if choice == "1":                                   # Add Customer
            try:
                cms=CustomerManagement()
                cms.id=input("Enter Customer Id:")
                cms.name=input("Enter Customer Name:")
                cms.age=input("Enter Customer Age:")
                cms.contact=input("Enter Customer Contact No.:")
                cms.addCustomer()
                print("Customer Added Successfully")
            except Exception as error:
                print("Error!",error)
        elif choice == "2":                                 # Search Customer
            try:
                cms=CustomerManagement()
                cms.id=input("Enter Customer Id:")
                cms.searchCustomer()
                showCustomer(cms)
            except Exception as error:
                print("Error!",error)
        elif choice == "3":                                 # Delete Customer
            try:
                cms=CustomerManagement()
                cms.id=input("Enter Customer Id:")
                cms.deleteCustomer()
                print("Customer Deleted Successfully")
            except Exception as error:
                print("Error!",error)
        elif choice == "4":                                 # Edit Customer
            cms=CustomerManagement()
            cms.id=input("Enter Customer Id:")
            cms.name=input("Enter Customer Name:")
            cms.age=input("Enter Customer Age:")
            cms.contact=input("Enter Customer Contact No.:")
            cms.editCustomer()
            print("Customer Edited Successfully")
        elif choice == "5":                                  # Display data of customer
            displayCustomer()
        elif choice == "6":                                  # Exit
            break
        else:
            print("Warning! Incorrect Choice")
    except Exception as error:
        print("Error!",error)
print("*** Thanks for using Chauhan Brothers Management System ***")