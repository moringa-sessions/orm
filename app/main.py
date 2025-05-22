from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from  models import User, Category, Task, Base
import os
# SQLITE DB connection
engine =  create_engine("sqlite:///database.db",echo=False )
Session = sessionmaker(bind=engine)

session = Session()


# ========================USER
def create_user():
    username = input("Enter your username : ")
    email =    input("Enter your email    : ")

    if not username or not email:
        print("Username/email required")
    
    user = User(username=username, email=email)
    session.add(user)
    session.commit()

    print(username, " created successfully!")

def fetch_users():
    users = session.query(User).all()
    for user in users:
        print(f"ID : {user.id}  USERNAME : {user.username} EMAIL : {user.email}")

#FETCH
def fetch_user_by_id():
    user_id = input("Enter user ID : ")
    user = session.query(User).get(user_id)
    if user:
        print(f"ID : {user.id}  USERNAME : {user.username} EMAIL : {user.email}")
    else:
        print("User not found!")
# Update
def update_user():
    user_id = input("Enter user ID : ")
    user = session.query(User).filter_by(id=user_id).first()
    if user:
        username = input("Enter new username : ")
        email = input("Enter new email : ")
        user.username = username
        user.email = email
        session.commit()
        print("User updated successfully!")
    else:
        print("User not found!")
# Delete
def delete_user():
    user_id = input("Enter user ID : ")
    user = session.query(User).filter_by(id=user_id).first()
    if user:
        session.delete(user)
        session.commit()
        print("User deleted successfully!")
    else:
        print("User not found!")


#============================Category
def create_category():
    name = input("Enter category name : ")
    

    category = Category(name=name)
    session.add(category)
    session.commit()

    print(name, " created successfully!")
def fetch_categories():
    categories = session.query(Category).all()
    for category in categories:
        print(f"ID : {category.id}  NAME : {category.name} ")
 #FETCH
def fetch_category_by_id():
    category_id = input("Enter category ID : ")
    category = session.query(Category).get(category_id)
    if category:
        print(f"ID : {category.id}  NAME : {category.name} ")
    else:
        print("Category not found!")

#UPDATE
def update_category():
    category_id = input("Enter category ID : ")
    category = session.query(Category).filter_by(id=category_id).first()
    if category:
        name = input("Enter new category name : ")
        
        category.name = name
      
        session.commit()
        print("Category updated successfully!")
    else:
        print("Category not found!")

#DELETE
def delete_category():
    category_id = input("Enter category ID : ")
    category = session.query(Category).filter_by(id=category_id).first()
    if category:
        session.delete(category)
        session.commit()
        print("Category deleted successfully!")
    else:
        print("Category not found!")


#=======================TASK
def create_task():
    title = input("Enter task title : ")
    description = input("Enter task description : ")
    user_id = input("Enter user ID : ")
    category_id = input("Enter category ID : ")
    deadline = input("Enter due date(YYYY-MM-DD) or none : ")
    due_date = datetime.strptime(deadline, "%Y-%m-%d") if deadline else None

    

    category = session.query(Category).filter_by(id=category_id).first()
    user = session.query(User).filter_by(id=user_id).first()
    if category and user:   
        task = Task(title=title, description=description, user_id=user_id, category_id=category_id, due_date=due_date)
        session.add(task)
        session.commit()

        print(title, " created successfully!")
    else:
        print("Category or User not found!")

def fetch_tasks():
    tasks = session.query(Task).all()
    for task in tasks:
        print(f"ID : {task.id}  TITLE : {task.title} DESCRIPTION : {task.description} USER : {task.user.username} CATEGORY : {task.category.name}")

 #FETCH
def fetch_task_by_id():
    task_id = input("Enter task ID : ")
    task = session.query(Task).get(task_id)
    if task:
        print(f"ID : {task.id}  TITLE : {task.title} DESCRIPTION : {task.description} USER : {task.user.username} CATEGORY : {task.category.name}")
    else:
        print("Task not found!") 

#UPDATE
def update_task():
    task_id = input("Enter task ID : ")
    task = session.query(Task).filter_by(id=task_id).first()
    if task:
        title = input("Enter new task title : ")
        description = input("Enter new task description : ")
        category_id = input("Enter new category ID : ")

        deadline = input("Enter due date(YYYY-MM-DD) or none : ")
        due_date = datetime.strptime(deadline, "%Y-%m-%d") if deadline else None

        task.title = title
        task.description = description
        task.due_date = due_date
        task.category_id = category_id
        session.commit()
        print("Task updated successfully!")
    else:
        print("Task not found!")

#DELETE
def delete_task():
    task_id = input("Enter task ID : ")
    task = session.query(Task).filter_by(id=task_id).first()
    if task:
        session.delete(task)
        session.commit()
        print("Task deleted successfully!")
    else:
        print("Task not found!")




def main():
    while True:
        print("============TASK MANAGER=============")
        print("1. Manage Users ")
        print("2. Manage Categories ")
        print("3. Manage Tasks ")
        main_choice = input("Enter your choice : ")
        
        if main_choice=="1":
            os.system("clear")
            print("\n=== User Management ===")
            print("1. Create User ")
            print("2. List Users ")
            print("3. Fetch User by ID ")
            print("4. Update User ")
            print("5. Delete User ")
            print("0. Exit ")

            choice = input("Enter your choice : ")

            if choice=="1":
                create_user()
            elif choice=="2":
                fetch_users()
            elif choice=="3":
                fetch_user_by_id()
            elif choice=="4":
                update_user()
            elif choice=="5":
                delete_user()
            elif choice=="0":
                print("Bye! Bye!")
                break
            else:
                print("Invalid input! Try again!")

        elif main_choice=="2":
            os.system("clear")
            print("\n=== Category Management ===")
            print("1. Create Category ")
            print("2. List Categories ")
            print("3. Fetch Category by ID ")
            print("4. Update Category ")
            print("5. Delete Category ")
            print("0. Exit ")


            choice = input("Enter your choice : ")
            # Category options
            if choice=="1":
                create_category()
            elif choice=="2":
                fetch_categories()
            elif choice=="3":
                fetch_category_by_id()
            elif choice=="4":
                update_category()
            elif choice=="5":
                delete_category()
            elif choice=="0":
                print("Bye! Bye!")
                break
            else:
                print("Invalid input! Try again!")
        
        # Task options
        elif main_choice=="3":
            os.system("clear")
            print("\n=== Task Management ===")
            print("1. Create Task ")
            print("2. List Tasks ")
            print("3. Fetch Task by ID ")
            print("4. Update Task ")
            print("5. Delete Task ")
            print("0. Exit ")

            
            if choice=="1":
                create_task()
            elif choice=="2":
                fetch_tasks()
            elif choice=="3":
                fetch_task_by_id()
            elif choice=="4":
                update_task()
            elif choice=="5":
                delete_task()
            elif choice=="0":
                print("Bye! Bye!")
                break
            else:
                print("Invalid input! Try again!")


main()