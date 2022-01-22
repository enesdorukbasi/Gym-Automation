from Databases import DatabaseContext

def List():
    cursor = DatabaseContext.con.cursor()
    cursor.execute("SELECT * FROM dbo_Payments")
    rows = cursor.fetchall()
    for row in rows:
        print(f"""
        Id {row[0]},""")
        if row[1] != None:
            print(f"""
        LearnerId {row[1]},""")
        if row[2] != None:
             print(f"""
        TrainerId {row[2]},""")
        print(f"""
        Pay {row[3]},
        PaymentType {row[4]},
            
        False = Teacher Salary : True = Student Fee
        *******************************************
        """)

def Create(learnerId,trainerId,pay):
    if trainerId == "" and learnerId == "":
        print("Two values cannot be empty(TrainerId, LearnerId)...")
    elif trainerId != "" and learnerId != "":
        print("Two values cannot be filled in at once (TrainerId, LearnerId)...")
    elif learnerId != "":
        cursor = DatabaseContext.con.cursor()
        cursor.execute("INSERT INTO dbo_Payments(LearnerId,Pay,PaymentType) VALUES ({},{},{});".format(int(learnerId), pay, True))
        DatabaseContext.con.commit()
    elif trainerId != "":
        cursor = DatabaseContext.con.cursor()
        cursor.execute("INSERT INTO dbo_Payments(TrainerId,Pay,PaymentType) VALUES ({},{},{});".format(int(trainerId), pay, False))
        DatabaseContext.con.commit()

def Remove(id):
    if id != int(None):
        cursor = DatabaseContext.con.cursor()
        cursor.execute("DELETE FROM dbo_Payments WHERE Id = {};".format(id))
        DatabaseContext.con.commit()
    else:
        print("Id cannot be null!")
