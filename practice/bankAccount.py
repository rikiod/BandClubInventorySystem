# this programs aims to be a basic bank account system. the inputs are the user's first name, last name, account number
# , pin number, balance, age, and contact information

# it has the following functions: checkBalance, deposit, withdraw,

customer1 = {'firstName': 'Filip', 'lastName': 'Keitaro', 'accountNumber': '00001', 'PIN': '1119', 'Balance': '5', 'Age': '18', 'Contact Information': 'filip@keitaro.jp'}
print(customer1)

def checkBalance(customer):
    print(f'Balance: {customer["Balance"]}')

def deposit(customer, amount):
    # this function deposits an amount into the customer's account as recorded in the dict
    customer['Balance'] += amount
    print(f'New Balance: {customer["Balance"]}')

def withdraw(customer, amount):
    if amount > customer['Balance']:
        customer['Balance'] -= amount
        print(f'New Balance: {customer["Balance"]}')
    else:
        print("The amount you wish to withdraw exceeds your current balance.")

checkBalance(customer1)
