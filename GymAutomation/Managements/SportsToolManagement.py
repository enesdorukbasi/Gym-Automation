from Databases import DatabaseContext

def List():
    cursor = DatabaseContext.con.cursor()
    cursor.execute("SELECT * FROM dbo_SportsTools")
    rows = cursor.fetchall()

    for row in rows:
        print(f"""
        Id {row[0]},
        Name {row[1]},
        TraderMark {row[2]}
        *******************
        """)

def Create(name,traderMark):
    cursor = DatabaseContext.con.cursor()
    cursor.execute("INSERT INTO dbo_SportsTools(Name,TradeMark) VALUES ('{}','{}');".format(name,traderMark))
    DatabaseContext.con.commit()

def Update(id,name,traderMark):
    cursor = DatabaseContext.con.cursor()
    cursor.execute("UPDATE dbo_SportsTools SET Name = '{}', TradeMark = '{}' WHERE Id = {};".format(name,traderMark,id))
    DatabaseContext.con.commit()

def Remove(id):
    if id != None:
        cursor = DatabaseContext.con.cursor()
        cursor.execute("DELETE FROM dbo_SportsTools WHERE Id = {};".format(id))
        DatabaseContext.con.commit()
    else:
        print("Id cannot be null!")