class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    def make_deposit(self, amount):	
        self.account_balance += amount
        return self
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account_balance}")
        # return self
    def transfer_money(from_name, to_name, amount):
        from_name.make_withdrawal(amount)
        to_name.make_deposit(amount)
    

mitchell = User("Mitchell Caldwell", "mitchel@python.com")
kristy = User("Kristy Blair", "kristy@python.com")
darin = User("Darin James", "darin@python.com")

mitchell.make_deposit(250).make_deposit(550).make_deposit(100).make_withdrawal(200).display_user_balance()

kristy.make_deposit(200).make_deposit(250).make_withdrawal(100).make_withdrawal(175).display_user_balance()

darin.make_deposit(800).make_withdrawal(200).make_withdrawal(300).make_withdrawal(250).display_user_balance()

mitchell.transfer_money(darin, 100)
mitchell.display_user_balance()
darin.display_user_balance()