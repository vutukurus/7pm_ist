#DATABASE
import sqlite3

#Connect to the database..
con = sqlite3.connect("demo.db")
print ("Connected to db")

try:
    #Reading data from db..
    cmd_to_read = "select * from COMPANY"
    a = con.execute(cmd_to_read)
    t = a.fetchall()
    for i in t:
        print (i[6])


#insert the data to the table company..
#def insert_data(id, name,age):
#    cmd_to_insert = ''' INSERT INTO COMPANY(ID,NAME,AGE) VALUES({},'{}', {})'''.format(id,name,age)
#    con.execute(cmd_to_insert)
#    con.commit()

#insert_data(1,'python', 25)
#insert_data(2,'perl', 40)
#insert_data(3,'shell', 50)


#Read data, #write
#cmd = ''' CREATE TABLE COMPANY(ID INT, NAME TEXT, AGE INT)'''
#con.execute(cmd)
#print ("Table created")


except:
    #Always close the databse..
    con.close()


