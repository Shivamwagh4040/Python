# Instance variable : Name,Amount,Address,AccountNo
# Instance method : CreateAccount(), Display AccountInfo
# Class Variable : Bank_Name, ROI_On_FD
#class method : DisplayBankInfoemation

class Bank_Account:

    Bank_Name = "HDFC bank PVT LTD"
    ROI_On_FD = 6.7

    def __init__(self):
        self.Name = ""
        self.Amount = 0
        self.Address = ""
        self.AccountNo = 0

    def CreateAccount(self):
        print("Enter your name :")
        self.Name = input()

        print("Enter your initial amount :")
        self.Amount = int(input())

        print("Enter your Address :")
        self.Address = input()

        print("Enter your Account Number :")
        self.AccountNo = int(input())

    def DisplayAccountInfo(self):
        print("-------Your Account information is as below-------")
        print("Name of Account Holder : ",self.Name)
        print("Account Number : ",self.AccountNo)
        print("Aaddress of Account Holder : ",self.Address)
        print("Current Amount in account : ",self.Amount)

    @classmethod
    def DisplayBankInformation(cls):
        print("Welcome to banking console")
        print("Name of our bank is : ",cls.Bank_Name)
        print("Rate of interest we offer on fixed deposite is : ",cls.ROI_On_FD)
    
    @staticmethod
    def DisplayKYCInfo():
        print("Please consider below KYC information")
        print("According to the rules of Government of India you have to submit below documents")
        print("1 : Clear and recent passport size photo")
        print("2 : Photo of aadhar card")
        print("3 : Photo of PAN card")

    def Deposit(self,value):
        self.Amount = self.Amount + value

    def Withdraw(self,value):
        self.Amount = self.Amount - value
        
def main():
    print("-----------------Banking Application---------------------------")

    print("---------------calling static method to display KYC info----------------")

    Bank_Account.DisplayKYCInfo()
    print("---------------Accessing the instance variables from main-------------------")
    print("Name of bank : ",Bank_Account.Bank_Name)
    print("Rate of Interest on Fixed Deposit : ",Bank_Account.ROI_On_FD)

    print("-----------------Calling the class method to display bank info-----------------")

    Bank_Account.DisplayBankInformation()

    print("--------------Creating the objects of class-------------------")

    User1 = Bank_Account()
    User2 = Bank_Account()

    print("Creating the first account")
    print("------------Enter details for first account holder-----------------")

    User1.CreateAccount()
    User2.CreateAccount()

    print("Creating the second account")
    print("---------------Enter details of second account holder-----------------")

    User1.DisplayAccountInfo()
    User2.DisplayAccountInfo()

    User1.Deposit(500)
    User2.Deposit(1200)
    print("Amount of {} after deposite is {}: ",format(User1.Name,User1.Amount))
    print("Amount of {} after deposite is {}: ",format(User2.Name,User2.Amount))

    User1.Withdraw(200)
    User2.Withdraw(3000)
    print("Amount of {} after Withdraw is {}: ",format(User1.Name,User1.Amount))
    print("Amount of {} after Withdraw is {}: ",format(User2.Name,User2.Amount))
    
if __name__=="__main__":
    main()