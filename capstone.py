class Account(object):
    id = 0
    balance = 0
    annualInterestRate = 0/100
    dateCreated = 0

    def __init__(self, id, balance):
        self.id = id
        self.balance = balance
        self.annualInterestRate = 8

    def __str__(self):
        return self.id

    def summary(self):
        print("Acc No : " + str(self.id) + " | Created(" + str(self.dateCreated) + ") | Int. Rate = "+str(self.annualInterestRate)+" %")
        print("Balance is: R " + str(self.balance))
        self.showOptions()
    
    def changeValue(self, value):
        if value == 1:
            new_id = input("What would you like to change it to: ")
            self.id = new_id
            print("Done - New ID is "+new_id)
        elif value == 2:
            input("What would you like to set it to ? ")
            print("Nice try")
        else:
            print("Not an option. Please try again.")

    def showBalance(self):
        print('Your balance is : R '+str(self.balance))
        self.showOptions()

    def showDateCreated(self):
        print("Your account was created on "+self.dateCreated)
        self.showOptions()

    def getMonthlyInterestRate(self):
        print("Monthly interest rate is "+self.annualInterestRate/12)
        self.showOptions()

    def getMonthlyInterestBalance(self):
        print("Monthly interest return is :"+ self.balance * (self.annualInterestRate/12))
        self.showOptions()

    def withdraw(self):
        withdraw_amount = (int(input('What amount would you like to withdraw ? : R ')))
        
        if (self.balance - withdraw_amount) >= 0:
            print('Withdrawing......')
            self.balance = self.balance - withdraw_amount
            print('Balance: R ' + str(self.balance))
        else:
            print('Sorry, you dont have that amount of cash')
            print('You have only R '+ str(self.balance))
            self.withdraw()
        self.showOptions()

    def deposit(self):
        deposit_amount = (int(input('What amount to be deposited ? : ')))
        print("Depositing......")
        self.balance = self.balance + deposit_amount
        print('Balance: '+str(self.balance))
        self.showOptions()

    def exitAccount(self):
        exitButton = input('Are you sure you want to exit ? Type Y to exit or N to return to menu')
        if exitButton.lower() == 'y':
            print("See you later")
            exit()
        elif exitButton.lower() == 'n':
            self.showOptions()
        else:
            print('That is not a correct option')
            self.exitAccount()
        
    def showOptions(self):
        print('What would you like to do ?\nMain Menu')
        actionButton = (int(input('1 - Check Balance | 2 - Withdraw | 3 - Deposit | 4 - exit : ')))
        if actionButton == 1:
            self.showBalance()
        elif actionButton == 2:
            self.withdraw()
        elif actionButton == 3:
            self.deposit()
        elif actionButton == 4:
            self.exitAccount()
        else:
            print("Not Applicable. Try Again")
            self.showOptions()
        
    
account1 = Account(1,100)
account2 = Account(2,200)
account3 = Account(3,300)
account4 = Account(4,400)
account5 = Account(5,500)
account6 = Account(6,600)
account7 = Account(7,700)
account8 = Account(8,800)
account9 = Account(9,900)
account10 = Account(10,1000)

listAccounts = [account1,account2,account3,account4,account5,account6,account7,account8,account9,account10]


id_lookup = (int(input("Enter a valid ID pass : ")))

try:
    if listAccounts[id_lookup-1]:
        listAccounts[id_lookup-1].summary()
except IndexError:
        print("Incorrect ID - BYE...............")