""" Bank Management System (Console Based)
This project demonstrates basic Object-Oriented Programming in Python.
Features:
- User login authentication
- Security PIN verification
- Check balance
- Deposit and withdraw functionality"""
#Bank operating system
class Bank:
  def __init__(self):
    self.balance=1000
    self.userid=''
    self.pw=''
    self.id=''
    self.create_pin()
    self.login()
# To login the app by verifying the username and password
  def login(self):
   while(True):
     print("Welcome to ABC BANK\n""Please Login")
     username=input("Enter your app username")
     password=input("Enter your password of app")
     if(username==self.userid and password==self.pw):
        self.menu()
        break

     else:
        print("Invalid username or password ")

# To  provide the user with the menu to operate
  def menu(self):
     user_input=int(input("""Welcome to HDFC BANK APP
                            Press 1 to checkbalance
                            Press 2 to deposit
                            press 3 to withdraw
                            press 4 to exit """))
     if user_input==1:
           self.checkbalance()
     elif user_input==2:
           self.deposit()
     elif user_input==3:
           self.withdraw()
     elif user_input==4:
            print("Thank you for using HDFC Bank")
            return
     else:
        print("Invalid choice")
        self.menu()

# To create password, username and pin for the firat time sign in

  def create_pin(self):
    print("Set  your password and username ")
    set_username=input("set your app username")
    self.userid=set_username
    set_password=input("set your passward of app")
    self.pw=set_password
    set_pin=int(input("set 4 digit security pin"))
    self.id=set_pin

#  To check the balance of the user.

  def checkbalance(self):
          pin=int(input("Enter your 4 digit pin to check balance"))
          if pin==self.id:
             print("Available balance:",self.balance)
          else:
            print("Invalid pin")
          self.menu()


# To deposit the amount by the user
  def deposit(self):
      amount=int(input("Enter amount to deposit"))
      self.balance+=amount
      print("New balance :",self.balance)
      self.menu()

# To withdraw the amount

  def withdraw(self):
      security_pin=int(input("Enter your 4 digit pin "))
      if security_pin==self.id:
            amount=int(input("Enter amount to withdraw"))
            if self.balance>=amount :
                self.balance=self.balance-amount
                print("Withdrwan succesfullly", amount)
                print("Current balance is " ,self.balance)
            else:
                print("Insufficient balance")
      else:
         print("Incorrect pin")


      self.menu()







