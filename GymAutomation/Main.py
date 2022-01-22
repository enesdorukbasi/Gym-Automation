import sys
import Managements.LearnerManagement
import Managements.TrainerManagement
import Managements.SportsToolManagement
import Managements.PaymentManagement


MainMenu = """
(1)Learner Transactions
(2)Trainer Transactions
(3)Sports Tool Transactions
(4)Payment Transactions
(5)Exit
Please select an action...
"""
LearnerMenu = """
You have selected Learner operations
(1)List
(2)Create
(3)Update
(4)Remove
"""
TrainerMenu = """
You have selected Trainer operations
(1)List
(2)Create
(3)Update
(4)Remove
"""
SportsToolMenu = """
You have selected Sports Tool operations
(1)List
(2)Create
(3)Update
(4)Remove
"""
PaymentMenu = """
You have selected Payment operations
(1)List
(2)Create
(3)Remove
"""

while True:
    print(MainMenu)
    process = int(input(""))
    if process == 1:
        print(LearnerMenu)
        LearnerProcess = int(input(""))
        if LearnerProcess == 1:
            Managements.LearnerManagement.List()
        elif LearnerProcess == 2:
            name = input("Enter the name of the 'Learner' to be added : ")
            surname = input("Enter the surname of the 'Learner' to be added : ")
            phoneNumber = input("Enter the phone number of the 'Learner' to be added : ")
            Managements.LearnerManagement.Create(name,surname,phoneNumber)
        elif LearnerProcess == 3:
            Id = int(input("Enter the id of the 'Learner' to be update : "))
            name = input("Enter the name of the 'Learner' to be update : ")
            surname = input("Enter the surname of the 'Learner' to be update : ")
            phoneNumber = input("Enter the phone number of the 'Learner' to be update : ")
            Managements.LearnerManagement.Update(Id,name,surname,phoneNumber)
        elif LearnerProcess == 4:
            Id = int(input("Enter the id of the 'Learner' to be remove : "))
            Managements.LearnerManagement.Remove(Id)
        else:
            print("You entered an incorrect transaction code.")
    elif process == 2:
        print(TrainerMenu)
        TrainerProcess = int(input(""))
        if TrainerProcess == 1:
            Managements.TrainerManagement.List()
        elif TrainerProcess == 2:
            name = input("Enter the name of the 'Trainer' to be added : ")
            surname = input("Enter the surname of the 'Trainer' to be added : ")
            phoneNumber = input("Enter the phone number of the 'Trainer' to be added : ")
            salary = float(input("Enter the salary of the 'Trainer' to be added : "))
            Managements.TrainerManagement.Create(name,surname,phoneNumber,salary)
        elif TrainerProcess == 3:
            Id = int(input("Enter the id of the 'Trainer' to be update : "))
            name = input("Enter the name of the 'Trainer' to be update : ")
            surname = input("Enter the surname of the 'Trainer' to be update : ")
            phoneNumber = input("Enter the phone number of the 'Trainer' to be update : ")
            salary = float(input("Enter the salary of the 'Trainer' to be update : "))
            Managements.TrainerManagement.Update(Id,name,surname,phoneNumber,salary)
        elif TrainerProcess == 4:
            Id = int(input("Enter the id of the 'Trainer' to be remove : "))
            Managements.TrainerManagement.Remove(Id)
        else:
            print("You entered an incorrect transaction code.")
    elif process == 3:
        print(SportsToolMenu)
        SportsToolProcess = int(input(""))
        if SportsToolProcess == 1:
            Managements.SportsToolManagement.List()
        elif SportsToolProcess == 2:
            name = input("Enter the name of the 'SportsTool' to be added : ")
            traderMark = input("Enter the trader mark of the 'SportsTool' to be added : ")
            Managements.SportsToolManagement.Create(name,traderMark)
        elif SportsToolProcess == 3:
            Id = int(input("Enter the id of the 'SportsTool' to be update : "))
            name = input("Enter the name of the 'SportsTool' to be update : ")
            traderMark = input("Enter the trader mark of the 'SportsTool' to be update : ")
            Managements.SportsToolManagement.Update(Id,name,traderMark)
        elif SportsToolProcess == 4:
            Id = int(input("Enter the id of the 'SportsTool' to be remove : "))
            Managements.SportsToolManagement.Remove(Id)
        else:
            print("You entered an incorrect transaction code.")
    elif process == 4:
        print(PaymentMenu)
        PaymentProcess = int(input(""))
        if PaymentProcess == 1:
            Managements.PaymentManagement.List()
        elif PaymentProcess == 2:
            print("""
            Enter "TrainerId" if paid salary will be given... 
            If received salary will be given, enter "LearnerId"...
            """)
            learnerId = input("Enter the learnerId of the 'Payment' to be added : ")
            trainerId = input("Enter the trainerId of the 'Payment' to be added : ")
            pay = float(input("Enter the pay of the 'Payment' to be added : "))
            Managements.PaymentManagement.Create(learnerId,trainerId,pay)
        elif PaymentProcess == 3:
            Id = int(input("Enter the id of the 'Payment' to be remove : "))
            Managements.PaymentManagement.Remove(Id)
        else:
            print("You entered an incorrect transaction code.")
    elif process == 5:
        print("Checking out...")
        sys.exit()
    else:
        print("You entered an incorrect transaction code.")