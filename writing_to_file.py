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
    print (t)
    
        
    
    with open("sample_db.txt","a") as f:
        for i in t:
            data = []
            c = 0
            for j in i:
                f.write(str(j))
                if c > 1:
                    pass
                else:
                    f.write("-")
                c = c+1
            f.write("\n")
        #f.write("This is my first line")
        #f.write("\n")
        #f.write("This is my second line")
except:
    pass
