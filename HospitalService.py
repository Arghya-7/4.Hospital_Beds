#USE THIS --> pip install mysql-connector-python
import sys
import mysql.connector
# attributs of hospital=(reg_no(primary key,hosp_name,password,loc,pincode,mobile,bed_no )
"""
Author : Arghya Dey
Date 20-05-2022
Place Kolkata

devrName :- Scott
Password :- Tiger
"""
devName = "Scott"
devPassword = "Tiger"

myHostDB="blzsehbaai1j29wb0q95-mysql.services.clever-cloud.com"
myUserDB="u51tyaz7vbyugubl"
myPasswordDb="H6Gjsh6cF8QaEpo56o8k"
myDataBaseDb="blzsehbaai1j29wb0q95"

mydb=mysql.connector.connect(host =myHostDB,user=myUserDB,passwd=myPasswordDb,database=myDataBaseDb)

mycursor=mydb.cursor()
# mycursor.execute("SHOW TABLES;")
# a=mycursor.fetchall()
# print(a)
class Devloper:
    def defineDatabase(self):
        sql="DROP TABLE hospital;"
        mycursor.execute(sql)
        sql="CREATE TABLE hospital(reg_no VARCHAR(20) PRIMARY KEY,hosp_name VARCHAR(20) NOT NULL,password VARCHAR(20),loc VARCHAR(20) NOT NULL,pincode VARCHAR(20) NOT NULL,moblile VARCHAR(20),bed_no VARCHAR(20));"
        mycursor.execute(sql)
        mydb.commit()
    def seeDatabase(self):
        sql="SELECT * FROM hospital;"
        mycursor.execute(sql)
        fp=mycursor.fetchall()
        print("{:<10} {:<20} {:13} {:<15} {:<10} {:<10} {:<10}".format("Reg.No", "Name", "Password", "Location", "Pincode", "Mobile No", "Bed_No"))
        for i in fp:
            # print(i)
            print("{:<10} {:<20} {:13} {:<15} {:<10} {:<10} {:<10}".format(i[0],i[1],i[2], i[3], i[4], i[5], i[6]))
    def control(self):
        print()
        print("*******Welcome Admin*******")
        while True:
            print("1 for define database")
            print("2 for see full database")
            print("0 for exit")
            ch=int(input("Enter the choice:"))
            if ch==0:
                exit(0)
            elif ch==1:
                self.defineDatabase()
            elif ch==2:
                self.seeDatabase()


class User:
    def seePincodeWise(self):
        pincode=input("Enter the pincode:")
        sql = "SELECT * FROM hospital WHERE pincode=" + pincode + ";"
        mycursor.execute(sql)
        fp=mycursor.fetchall()
        print("{:<20} {:<15} {:<10} {:<10} {:<10}".format('Name', 'Location','Pincode','Mobile_No','Bed_Number'))
        for i in fp:
            print("{:<20} {:<15} {:<10} {:<10} {:<10}".format(i[1], i[3], i[4], i[5], i[6]))
    def seeHospitalNameWise(self):
        name=input("Enter hospital name:").upper()
        sql = "SELECT * FROM hospital WHERE hosp_name LIKE '%" + name + "%' ;"
        mycursor.execute(sql)
        fp = mycursor.fetchall()
        print("{:<20} {:<15} {:<10} {:<10} {:<10}".format('Name', 'Location', 'Pincode', 'Mobile_No', 'Bed_Number'))
        for i in fp:
            print("{:<20} {:<15} {:<10} {:<10} {:<10}".format(i[1], i[3], i[4], i[5], i[6]))
    def control(self):
        print("1 for check pincode wise hospitals")
        print("2 for check Hospital name wise")
        ch=int(input("Enter the choice:"))
        if ch==1:
            self.seePincodeWise()
        elif ch==2:
            self.seeHospitalNameWise()
        else:
            print("Wrong Choice")

class Hospital:
    def registration(self):
        reg_no=input("Enter the registration number:")
        name=input("Enter your Hospital name:")
        password=input("Enter a suitable password:")
        reconfirmed_password=input("Enter the password again:")
        if password==reconfirmed_password:
            loc=input("Enter your location name:").upper()
            pin=input("Enter your pincode name:")
            mobile = input("Enter 10 digit mobile number of your hospital::")
            while True:
                if len(mobile) != 10:
                    print("Re-Enter Mobile number")
                else:
                    break
            sql="INSERT INTO hospital(reg_no,hosp_name,password,loc,pincode,moblile,bed_no) VALUES(%s,%s,%s,%s,%s,%s,%s);"
            val=(reg_no,name,password,loc,pin,mobile,0)
        mycursor.execute(sql,val)
        mydb.commit()
    def changeBedNumber(self):
        reg_no = input("Enter the registration number:")
        password = input("Enter registered password:")
        sql="SELECT password FROM hospital WHERE reg_no="+reg_no+";"
        mycursor.execute(sql)
        fp=mycursor.fetchall()
        if fp[0][0]==password:
            no_of_bed=input("Enter number of bed:")
            sql="UPDATE hospital SET bed_no='"+no_of_bed+"' WHERE reg_no='"+reg_no+"' ;"
            print(sql)
            mycursor.execute(sql)
            mydb.commit()
    def control(self):
        print("1 for registration:")
        print("2 for change bed number:")
        ch=int(input("Enter the choice:"))
        if ch==1:
            self.registration()
        elif ch==2:
            self.changeBedNumber()
        else:
            print("Wrong choice")

# x=Hospital()
# x.changeBedNumber()

# dev=Devloper()
# dev.seeDatabase()
def main():
    print("1 for develioper")
    print("2 for Hospital Authority")
    print("3 for User")
    ch=int(input("Enter thec hoice:"))
    if ch==1:
        name=input("Enter the Name:")
        password_=input("Enter password:")
        if name==devName and password_==devPassword:
            dev=Devloper()
            dev.control()
    elif ch==2:
        hos=Hospital()
        hos.control()
    elif ch==3:
        user=User()
        user.control()


if __name__=="__main__":
    main()