'''Conole based CRUD Application developed by Mrinmoy Bhattacharjee
Front End: Python
Back End : MySQL
please provide the appropriate connection details of mysql in con.connect() function
it will automatically create the required database and table.
 !!!Happy Coding!!!

'''
from beautifultable import BeautifulTable
import mysql.connector as  conn
from mysql.connector import Error
from matplotlib import pyplot as plt
def database():
    global conn, cursor,mycon
    #mycon = conn.connect(host="ServerName", user="username", passwd="my_sqlpassword", database="database_name")
    mycon = conn.connect(host="localhost", user="root", passwd="root", database="mysql")
    # cursor_object=connection_name.cursor()
    cursor = mycon.cursor()
    cursor.execute("create database if not exists `libinfo`")
    cursor.execute("use libinfo")
    cursor.execute(
        "CREATE TABLE if not exists `book`(slno INTEGER PRIMARY KEY AUTO_INCREMENT ,bookid varchar(30),bname varchar(40),aname varchar(40),pub varchar(50),isbn varchar(60),noc int, price int)")
def add_record():
    database()
    bookid=input("Enter the book id=")
    bname=input("Enter the book Name=")
    aname=input("Enter the Author Name=")
    pub=input("Enter the publisher name=")
    price=int(input("Enter the Price="))
    noc=int(input("Enter the no of copies="))
    isbn=input("Enter the ISBN no=")
    st = "insert into book(bookid,bname,aname,pub,isbn,noc,price)values('{}','{}','{}','{}','{}',{},{})".format(bookid,bname,aname,pub,isbn,noc,price)
    cursor.execute(st)
    print("Record Added Successfully")
    print("-------------------------------------------------------------")
    mycon.commit()
#######################################################################################
'''
def display_record():
    database()
    x=[]
    y=[]
    st1="select * from book"
    cursor.execute(st1)
    data = cursor.fetchall()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    for row in data:
        x.append(row[2])
        y.append(row[6])
        print('Sl No: ',row[0],'Bookid: ',row[1],'BookName: ',row[2],'AuthorName: ',row[3],'Publisher: ',row[4],'ISBN: ',row[5],'NO of Copies: ',row[6],'Price: ',row[7])
    plt.ylim(0, 50)
    plt.yticks(range(0, 51, 10))
    plt.bar(x, y,  align='center', width=[0.5,0.5],color=['r','y'])
    plt.show()
    print("------------------------------------------------------------------------------------------------------------------------------------------------------------")
'''
#######################################Search Record#########################################
def search_record():
    database()

    print("a-Search by Book name")
    print("b-search by Author name")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    c=input("Enter your option between a/b=")

    if c=='a':
     srch=input("Enter the book name to search=")
     st = "select * from book where  bname='{}'".format(srch)
     cursor.execute(st)
     data = cursor.fetchall()
     if data:
      for row in data:
         print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
         print('Bookid: ',row[1],'\n''BookName: ',row[2],'\n''AuthorName: ',row[3],'\n''Publisher: ',row[4],'\n''ISBN: ',row[5],'\n''NO of Copies: ',row[6],'\n''Price: ',row[7])
         print("-------------------------------------------------------------")


     else:
        print("No Record Found")
        print("-------------------------------------------------------------")

    elif c=='b':
     srch = input("Enter the Author name to search=")
     st = "select * from book where  aname='{}'".format(srch)
     cursor.execute(st)
     data = cursor.fetchall()
     if data:
      for row in data:
         print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
         print('Bookid: ', row[1], '\n''BookName: ' , row[2], '\n''AuthorName: ' , row[3], '\n''Publisher: ',
               row[4], '\n''ISBN: ', row[5], '\n''NO of Copies: ', row[6], '\n''Price: ', row[7])
         print("------------------------------------------------------------------------")
     else:
        print("No Record Found")
        print("-------------------------------------------------------------------------")
    else:
        print("-------------------------------------------------------------------------")
        print("You Entered a wrong option")
#####################################Delete Record#####################################
def delete_record():
    database()
    print("a-Delete by Book name")
    print("b-Delete by Author name")
    print("-------------------------------------------------------------")
    c = input("Enter your option between a/b=")
    if c == 'a':
        cursor = mycon.cursor(buffered=True)
        srch = input("Enter the book name to Delete=")
        st1 = "select * from book where  bname='{}'".format(srch)
        cursor.execute(st1)

        if (cursor.rowcount == 1):
            st = "delete from book where  bname='{}'".format(srch)
            data=cursor.execute(st)
            mycon.commit()
            print("Data Deleted successfully")
            print("-------------------------------------------------------------")
        else:
            print("Failed to Delete record from table")
            print("-------------------------------------------------------------")

    elif c == 'b':
        cursor = mycon.cursor(buffered=True)
        srch = input("Enter the Author name to Delete=")
        st1 = "select * from book where  aname='{}'".format(srch)
        cursor.execute(st1)
        if (cursor.rowcount == 1):
            st = "delete from book where  aname='{}'".format(srch)
            cursor.execute(st)
            mycon.commit()
            print("Data Deleted successfully")
            print("-------------------------------------------------------------")
        else:
            print("Failed to Delete record from table")
            print("-------------------------------------------------------------")


    else:
        print("You Entered a wrong Option")
        print("-------------------------------------------------------------")

################################Update Record############################

def update_record():
    database()
    slno=int(input("Enter the slno to be update="))
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ')
    print("| a-Update Book Name            |")
    print("| b-Update Author Name          |")
    print("| c-Update ISBN No              |")
    print("| d-Update Price                |")
    print("| e-Update Publisher Name       |")
    print("| f-Update Book and Author Name |")
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ')
    ch=input("Enter the choice between a/b/c/d/e/f=")
    if ch=='a':
        srch=input("Enter the  Corrected Book name value=")
        st="update book set bname='{}' where slno={}".format(srch,slno)
        cursor.execute(st)
        mycon.commit()
        print("Data Update sucessfully")
    elif ch=='b':
        srch = input("Enter the  New Author name value=")
        st = "update book set aname='{}' where slno={}".format(srch, slno)
        cursor.execute(st)
        mycon.commit()
        print("Data Update sucessfully")
    elif ch=='c':
        srch = input("Enter the  New ISBN no=")
        st = "update book set isbn='{}' where slno={}".format(srch, slno)
        cursor.execute(st)
        mycon.commit()
        print("Data Update sucessfully")
    elif ch=='d':
        srch = input("Enter the  New Price=")
        st = "update book set price='{}' where slno={}".format(srch, slno)
        cursor.execute(st)
        mycon.commit()
        print("Data Update sucessfully")
    elif ch=='e':
        srch = input("Enter the  Corrected Publisher value=")
        st = "update book set pub='{}' where slno={}".format(srch, slno)
        cursor.execute(st)
        mycon.commit()
        print("Data Update sucessfully")
    elif ch=='f':
        srch = input("Enter the  Corrected Book value=")
        srch2 = input("Enter the  Corrected Author value=")
        st = "update book set bname='{}',aname='{}' where slno={}".format(srch,srch2,slno)
        cursor.execute(st)
        mycon.commit()
        print("Data Update sucessfully")
####################################################################################


def display_record():
    database()
    x = []
    y = []
    st1="select * from book"
    cursor.execute(st1)
    data = cursor.fetchall()
    table = BeautifulTable(maxwidth=120)
    table.set_style(BeautifulTable.STYLE_GRID)
    table.columns.alignment = BeautifulTable.ALIGN_RIGHT
    table.columns.header = ["SlNo", "Book Id", "BookName","Author Name ","Publisher","ISBN","NO of Copies","Price"]
    for r in data:
        table.rows.append(r)
        x.append(r[2])
        y.append(r[6])
    print(table)
    plt.ylim(0, 50)
    plt.yticks(range(0, 51, 10))
    plt.bar(x, y, align='center', width=[0.5, 0.5], color=['r', 'y'])
    plt.show()

#################################Main Section########################################
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("Library management system\n\n\t\t\t\t *** Developed by Mrinmoy Bhattacharjee ***")
print("#################################################################")
while True:
    print("1-- Add Book Record")
    print("2-- Display Book Record")
    print("3-- Search Book Record")
    print("4-- Delete particlar Book Record")
    print("5-- Update  Book Record")
    print("6-- Exit")
    print("-------------------------------------------------------------")
    choice=int(input("Enter your choice="))
    if choice==1:
        add_record()
    elif choice==2:
        display_record()
    elif choice==3:
        search_record()
    elif choice==4:
        delete_record()
    elif choice==5:
        update_record()
    elif choice == 6:
        break

