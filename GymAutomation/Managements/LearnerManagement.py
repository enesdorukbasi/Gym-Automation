from Databases import DatabaseContext

def List():
    cursor = DatabaseContext.con.cursor()
    cursor.execute("SELECT * FROM dbo_Learners")
    rows = cursor.fetchall()

    for row in rows:
        print(f"""
        Id {row[0]},
        Name-Surname {row[1] + ' ' + row[2]},
        PhoneNumber {row[3]}
        *************************************
        """)

def Create(name,surname,phoneNumber):
    cursor = DatabaseContext.con.cursor()
    cursor.execute("INSERT INTO dbo_Learners(Name,Surname,PhoneNumber) VALUES('{}','{}','{}');".format(name,surname,phoneNumber))
    DatabaseContext.con.commit()

def Update(Id,name,surname,phoneNumber):
    cursor = DatabaseContext.con.cursor()
    cursor.execute("UPDATE dbo_Learners SET Name = '{}', Surname = '{}', PhoneNumber = '{}' WHERE Id = {};".format(name,surname,phoneNumber,Id))
    DatabaseContext.con.commit()

def Remove(Id):
    if Id != None:
        cursor = DatabaseContext.con.cursor()
        cursor.execute("DELETE FROM dbo_Learners WHERE Id = {};".format(Id))
    else:
        print("Id cannot be null!")