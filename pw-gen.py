#!/bin/python3
import random

up_case = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
           'W', 'X', 'Y', 'Z']

low_case = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

symbols = ["!", "@", '#', "$", "%", '^', '&', '*', '?', '+', '=']

#Randomize the lists
random.shuffle(up_case)
random.shuffle(low_case)
random.shuffle(numbers)
random.shuffle(symbols)

#Randomize the selection, and set amount selected from each list
part1 = random.choices(up_case, k=4)
part2 = random.choices(low_case, k=4)
part3 = random.choices(numbers, k=4)
part4 = random.choices(symbols, k=4)

#concatonate randomized list selections
all_lists = (part1 + part2 + part3 + part4)

#convert list to string format
rough = ' '.join(map(str, all_lists))

#eliminate spaces in output
final = rough.replace(" ", "")

#Greeting
print("Kudos on using strong passwords! \n")

#Collect input for entry name 
acc_name = input("\nEnter the name of the account you'd like to create a password for here:\n")


#Save PW to vault
def save_entry(pw,account_name):
    password = final
    with open('Passwords.txt', 'a') as password:
        password.write(str(f'{pw}' + f' -{account_name}-\n'))


#Creates a vault  for PWs
def database():
    with open('Passwords.txt', 'w') as Passwords:
        print('\nA Password Vault has been created for you.\n')
        save_entry(final,acc_name)



#Determines if vault is needed, and if so, creates one
def profile():
    vault = input('Do you have a Vault already? (Yes/No):')
    if vault.lower() == "no":
        database()
    elif vault.lower() == "yes":
        save_entry(final,acc_name)
    else:
        print("Please enter 'Yes', or 'No'.")
        profile()

#output password, and confirm saved entry 
def confirm():
    print(f'Your password is: {final} ')
    print('The password has been saved to your Vault for your convenience.')
    print('\nThank you for using PW-Gen!')

profile()
confirm()
