from Databases import DatabaseContext

def List():
    cursor = DatabaseContext.con.cursor()
    cursor.execute("SELECT * FROM dbo_Trainers")
    rows = cursor.fetchall()

    for row in rows:
        print(f"""
        Id {row[0]},
        Name-Surname {row[1]+' '+row[2]},
        PhoneNumber {row[3]},
        Salary{row[4]}
        *********************************
        """)

def Create(name,surname,phoneNumber,salary):
    cursor = DatabaseContext.con.cursor()
    cursor.execute("INSERT INTO dbo_Trainers(Name,Surname,PhoneNumber,Salary) VALUES('{}','{}','{}',{});".format(name,surname,phoneNumber,salary))
    DatabaseContext.con.commit()

def Update(Id,name,surname,phoneNumber,salary):
    cursor = DatabaseContext.con.cursor()
    cursor.execute("UPDATE dbo_Trainers SET Name = '{}',Surname = '{}', PhoneNumber = '{}', Salary = {} WHERE Id = {};".format(name,surname,phoneNumber,salary,Id))
    DatabaseContext.con.commit()

def Remove(Id):
    if Id != None:
        cursor = DatabaseContext.con.cursor()
        cursor.execute("DELETE FROM dbo_Trainers WHERE Id = {};".format(Id))
        DatabaseContext.con.commit()
    else:
        print("Id cannot be null!")