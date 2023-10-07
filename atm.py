class ATM:
    def __init__(self,balance=0):
        self.balance=balance

    def check_balance(self):
        return f"Your balance is ${self.balance}"

    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            return f"${amount} has been deposited."
        else:
            return "Invalid amount.Deposit amount must be greater than zero."

    def withdraw(self,amount ):
        if amount>0 and amount <=self.balance:
            self.balance-=amount
            return f"${amount}has been withdraw."
        elif amount<=0:
            return "Invalid amount.Witdrawal amount must be greater than zero."
        else:
            return ("Invalid balance.")
def main():
    atm =ATM()
    while True:
        print("ATM Menu:")
        print("1.Check Balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit")

        choice=input("Select an option{1/2/3/4}:")

        if choice=='1':
            print(atm.check_balance())
        elif choice=='2':
            amount=float(input("Enter the amount to deposit: $"))
            print(atm.deposit(amount))
        elif choice=='3':
            amount=float(input("Enter the amount to withdraw: $"))
            print(atm.withdraw(amount))
        elif choice=='4':
            print("Thak u for using ATM.")
            break
        else:
            print("Invalid choice.Please select valid option.")

if __name__=="__main__":
    main()