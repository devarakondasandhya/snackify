import mysql.connector
con=mysql.connector.connect(host='localhost',user='root',passwd='your_mysql_password', database = 'snackify')

cur=con.cursor()
q="select * from menu "
cur.execute(q)
data=cur.fetchall()
if data==[]:
    cur.execute("insert into menu values(1,'Ice cream',50)")
    cur.execute("insert into menu values(2,'Gulab jamun',12)")
    cur.execute("insert into menu values(3,'Ras malai',44)")
    cur.execute("insert into menu values(4,'Halwa',50)")
    cur.execute("insert into menu values(5,'Rasgulla',15)")
    cur.execute("insert into menu values(6,'Pani puri',30)")
    cur.execute("insert into menu values(7,'Pan Pizza',120)")
    cur.execute("insert into menu values(8,'Samosa',27)")
    cur.execute("insert into menu values(9,'Bhel puri',50)")
    cur.execute("insert into menu values(10,'Vada Pav',30)")
    cur.execute("insert into menu values(11,'Pakora Bhaji',50)")
    cur.execute("insert into menu values(12,'Chai',10)")
    con.commit()
    
    
q="select * from staff"
cur.execute(q)
data=cur.fetchall()
if data==[]:
    cur.execute("insert into staff values(1,'Sandhya',6000)")
    con.commit()

from datetime import datetime
print("------------------------------------WELCOME-------------------------------------------")
print("--------------------------------------TO----------------------------------------------")
print("-------------------------SNACKIFY SNACKS & SWEETS CORNER--------------------------------")
print("______________________________________________________________________________________")
print("..........................Made By : Sandhya Devarakonda................................")
print("______________________________________________________________________________________")


while True:
    print("\n\nPlease Choose\n1. For OWNER \n2. For CUSTOMER\n3. For EXIT\n")
    choice=int(input("Enter your choice: "))
    if choice==3:
        break
    if choice==1:
        owner=input("ENTER USERNAME: ")
        password=input("ENTER PASSWORD: ")
        if password=='root':
            print("------------------------------You have logged in as admin successfully!!!-----------------------")
            print("Press 1 to add items in the shop")
            print("Press 2 to see items in the shop")
            print("Press 3 to update cost of any item")
            print("Press 4 to add a new staff into the shop")
            print("Press 5 to see the details of the staff")
            print("Press 6 to update the salary of the staff")
            print("Press 7 to exit to logout as admin")
            c=0
            while(c!=7):
                c=int(input("\nEnter your choice: "))
                if c==1:
                    def add():
                        sno=int(input("Enter Serial_no: "))
                        item=input("Enter item name: ")
                        cost=int(input("Enter cost: "))
                        p=(sno,item,cost)
                        i='insert into menu values(%s,%s,%s)'
                        cur.execute(i,p)
                        con.commit()
                        print("Item added successfully!")
                    add()


                elif c==2:
                    def items():
                        print("Items in the shop are as follows : ")
                        q='select*from menu'
                        cur.execute(q)
                        data=cur.fetchall()
                        t=(['Serial_no','Items ','Cost'])
                        for serial_no,items,cost in data:
                            print(serial_no,":",items ,":",cost)
                    items()

                
                elif c==3:
                    def modify():
                        sno=input("Enter the sno of the item you want to update: ")
                        cost=input("Enter the new amount: ")
                        cur.execute("update menu set cost="+cost+" where sno = "+sno+';')
                        con.commit()
                        print("TABLE AFTER UPDATING")
                        q="select*from menu"
                        cur.execute(q)
                        data=cur.fetchall()
                        t=(['sno','items','cost'])
                        for sno,items,cost in data :
                            print(sno,":",items,":",cost)

                    def items():
                        print("Items in the shop are as follows : ")
                        q='select*from menu'
                        cur.execute(q)
                        data=cur.fetchall()
                        t=(['Serial_no','Items ','Cost'])
                        for serial_no,items,cost in data:
                            print(serial_no,":",items ,":",cost)
                        
                    items()
                    modify()

                
 
                
                elif c==4:
                    def alter():
                        sno=int(input("Enter sno: "))
                        n=input("Enter name:")
                        salary=int(input("Enter the salary: "))
                        d=(sno,n,salary)
                        s='insert into staff values(%s,%s,%s)'
                        cur.execute(s,d)
                        con.commit()
                        print("NEW STAFF ADDED !!")
                
                    
                    alter()
                
                elif c==5:
                    def staff():
                        print("Staff present in the shop are as follows: ")
                        q="select*from staff"
                        cur.execute(q)
                        data=cur.fetchall()
                        t=(['Serial_no','Name','Salary'])
                        print(t)
                        for serial_no,name,salary in data:
                            print(serial_no,":",name,":",salary)
                    staff()
                
                elif c==6:
                    def sal():
                        print("Choose 1 to increment the salary")
                        print("Choose 2 to reduce the salary")
                        g=int(input("Enter choice (1/2): "))
                        name=input("Enter the name of EMPLOYEE: ")
                        salary=input("Enter the salary to be added/deducted: ")
                        if g==1:
                            cur.execute("update staff set salary=salary+"+salary+" "+"where name="+"'"+name+"'"+';')
                            con.commit()
                            print("TABLE AFTER UPDATION")
                            q="select*from staff"
                            cur.execute(q)
                            data=cur.fetchall()
                            t=(['Serial_no','Name','Salary'])
                            for sno,name,salary in data:
                                print(sno,":",name,":",salary)
                        if g==2:
                            cur.execute("update staff set salary=salary-"+salary+" "+"where name="+"'"+name+"'"+';' )
                            con.commit()
                            print("TABLE AFTER UPDATION")
                            sq="select*from staff"
                            cur.execute(sq)
                            data=cur.fetchall()
                            t=(['Serial_no','Name','Salary'])
                            for sno,name,salary in data:
                                print(sno,":",name,":",salary)
                    sal()
                elif c==7:
                    continue
                else:
                    print("SORRY..You have entered the wrong number, input from 1 to 7")
        else:
            print("****************************** WRONG PASSWORD! *****************************************************")


            
      
            
    elif choice==2:
        name=input("Enter your name: ")
        phone=int(input("Enter your phone number: "))
        c=0
        while(c!=3):
            print('\nPress 1 to see the MENU')
            print('Press 2 to order an item')
            print('Press 3 to exit')
            print()
            c=int(input("Enter your choice: "))
            if c==1:
                def items():
                    print("Items in the shop are as follows: ")
                    q='select*from menu'
                    cur.execute(q)
                    data=cur.fetchall()
                    t=(['Serial_No','Items','Cost'])
                    print(t)
                    for serial_no,items,cost in data:
                        print(serial_no,":",items,":",cost)
                items()
            elif c==2:
                print("Hello!! What would you like to order?")
                q="select*from menu"
                cur.execute(q)
                data=cur.fetchall()
                t=(['Serial_No','Items','Cost'])
                print(t)
                for serial_no,items,cost in data:
                    print(serial_no,":",items,":",cost)
                sql="select sno from menu "
                cur.execute(sql)
                data=cur.fetchall()
                l=[]
                for i in range(len(data)):
                    l.append(data[i][0])
                '''print(l)'''
            
                a=''
                order=''
                amt=0
                b=0
                while a!='n':
                    d=int(input("\nEnter your Serial No of the Item to Buy: "))
                    if d in l :
                        qty=int(input("Enter Qty: "))
                        print("You have successfully ordered your selected item!!!\t")
                    
                        cur.execute("select*from menu where sno="+str(d))
                    
                        for i in cur:
                            L=i[2]
                            p=i[1]
                            con.commit()
                            if order=='':
                                order=order+p
                            else:
                                order = order +','+ p 
                            amt=amt+qty*L
                            b=b+1
                            a=input('Do you want to order more? (y/n): ')
                    else:
                        print("Wrong Input")
                if a=='n':
                    print("\n")
                    print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                    print("                                  YOUR BILL")
                    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                    print(" Customer's name: ",name)
                    print(" Contact no.: ",phone)
                    print(" Total items: ",b)
                    print(" Items ordered are: ",order)
                    print(" Total amount: ",amt)
                    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@ THANK_YOU FOR ORDERING @@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
                    print("\t\t\t\t\t\tDate:",datetime.now())
                
    else:
        print("\t\t\t\t\t\t\t***************************WRONG_PASSWORD***********************************\t\t\t\t\t\t\t\t")













