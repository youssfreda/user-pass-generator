import random
import openpyxl

def generate_password():
    return str(random.randint(0, 9999)).zfill(4)

def generate_usernames_and_passwords():
    num_users = int(input("How many users do you want to generate? "))
    first_username = input("What is the first username? ")
    user_data = []

    for i in range(num_users):
        username = str(int(first_username) + i)
        password = generate_password()
        user_data.append((username, password))

    generate_again = input("Do you want to generate another set of usernames and passwords? (Y/N) ")
    if generate_again.lower() == "y":
        generate_usernames_and_passwords()

    return user_data

def export_to_excel(user_data):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.append(['Username', 'Password'])
    for user in user_data:
        ws.append(user)
    filename = input("Enter a filename to save the data (without the extension): ")
    wb.save(f"{filename}.xlsx")

user_data = generate_usernames_and_passwords()
export_to_excel(user_data)
