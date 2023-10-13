import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',passwd='tiger',database='testfg')
mycursor=mydb.cursor()

mycursor.execute("CREATE TABLE PARTTIME(No INTEGER PRIMARY KEY,NAME VARCHAR(20),STIPEND INTEGER,PROFESSION VARCHAR(30),GRADE CHAR(1))")
print("Table Created")

mycursor.execute("INSERT INTO PARTTIME VALUES(1,'Karan',1000,'Accounts','A')")
mycursor.execute("INSERT INTO PARTTIME VALUES(2,'Manu',2000,'Medical','A')")
mycursor.execute("INSERT INTO PARTTIME VALUES(3,'Jyothi',800,'Clerical','C')")
mycursor.execute("INSERT INTO PARTTIME VALUES(4,'Vikas',500,'Clerical','D')")
mycursor.execute("INSERT INTO PARTTIME VALUES(5,'Anil',1200,'Medical','B')")
print("Values Inserted")


mydb.commit()
