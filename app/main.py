from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from  models import User, Category, Task, Base
import os
# SQLITE DB connection
engine =  create_engine("sqlite:///database.db",echo=False )
Session = sessionmaker(bind=engine)

session = Session()


# USER
def create_user():
    username = input("Enter your username : ")
    email =    input("Enter your email    : ")
    
    user = User(username=username, email=email)
    session.add(user)
    session.commit()

    print(username, " created successfully!")

def fetch_users():
    users = session.query(User).all()
    for user in users:
        print(f"ID : {user.id}  USERNAME : {user.username} EMAIL : {user.email}")

# Assignment
# Delete, Update, fetch single user

# CATEGORY
# Assignment
# ALL CRUD operations for category

# TASK
# CRUD 

# 

def main():
    while True:
        print("============TASK MANAGER=============")
        print("1. Create User ")
        print("2. List Users ")
        print("0. Exit ")
        choice = input("Enter your choice : ")

        if choice=="1":
            # os.system("clear")
            create_user()
        elif choice=="2":
            fetch_users()
        elif choice=="0":
            print("Bye! Bye!")
            break
        else:
            print("Invalid input! Try again!")


main()