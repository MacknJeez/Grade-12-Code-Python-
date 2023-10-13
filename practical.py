import mysql.connector
no=0
mydb = mysql.connector.connect(host='localhost', user='root', password='tiger', database='practical', autocommit=True)
mycursor=mydb.cursor()

def insert():
    x=int(input("\nEnter number of entries:"))
    global no
    for i in range(x):
        no=no+1
        name=input("\nEnter name:")
        stip=input("Enter stipend:")
        prof=input("Enter profession:")
        grade=input("Enter grade:")
        mycursor.execute(f"INSERT INTO parttime values({no},'{name}',{stip},'{prof}','{grade}')")
    
def view():
    mycursor.execute('SELECT * FROM parttime')
    x = mycursor.fetchall()
    print(x)

def update(old,new):
    mycursor.execute(f"UPDATE parttime set name='{new}' where name='{old}'")
    
def updateint(old,new):
    mycursor.execute(f"UPDATE parttime set name={new} where name={old}")

def delete():
    name=input("Enter name to delete")
    mycursor.execute(f"delete from parttime where name='{name}'")
    
def updatemenu():

    view()
    print("\nWhat do you want to update? ")
    print("1. Name")
    print("2. stipend")
    print("3. profession")
    print("4. grade")
    c=input()
    if c=='1':
        old=input("\nEnter name to update:")
        new=input("Enter new name:")
        update(old,new)
    if c=='2':
        old=int(input("\nEnter stipend to update:"))
        new=int(input("Enter new stipend:"))
        updateint(old,new)
    if c=='3':
        old=input("\nEnter profession to update:")
        new=input("Enter profession stipend:")
        update(old,new)
    if c=='4':
        old=input("\nEnter grade to update:")
        new=input("Enter new grade:")
        update(old,new)
    
choice=0
while choice!=5:

    print("\n1. Insert")
    print("2. View")
    print("3. Update")
    print("4. Delete")
    print("5. Quit")
    choice=input()
    
    if choice=='1':
        insert()

    elif choice=='2':
        view()

    elif choice=='3':
        updatemenu()

    elif choice=='4':
        delete()

    elif choice=='5':
        break
    else:
        print("Invalid Input")
        
        
