from colorama import Fore, Style, init
from openpyxl import workbook
from datetime import datetime
import logging
import hashlib
import getpass
import os

init(autoreset=True)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
log_path = os.path.join(BASE_DIR, 'M-Finance.log')

logging.basicConfig(
    level=logging.DEBUG,
    filename=log_path,
    filemode='w',
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logging.info('☑️ The program has started working')

hello_text = f'Hello! To get started, create a profile. Current date and time: {datetime.now()}'
user_db = []
current_user = None
current_username = None

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def check_password(password1, password2):
    return password1 == password2

def create_profile():
    global user_db
    global current_user
    global current_username
    global hello_text

    username = input('Enter your first and last name: ')
    user_password = getpass.getpass('Enter new password: ').lower()
    password_check = getpass.getpass('Please enter your password again: ').lower()

    if not user_password or not password_check or not username:
        logging.error('❌ Some fields are empty')
        print('❌ Passwords do not match')
    else:
        if not check_password(user_password, password_check):
            logging.error('❌ Passwords do not match')
            print('❌ Passwords do not match')
        else:
            logging.info(f'✅ Profile created successfully! {username}')
            print('✅ Profile created successfully!')

            hashed_password = hash_password(user_password)
            user_db.append({'username': username, 'password': hashed_password})

            current_user = user_db[0]
            current_username = current_user['username']

            hello_text = f'Hello {current_username}! Current date and time: {datetime.now()}'

def change_user():
    global current_user
    global current_username
    global hello_text

    input_username = input('Enter username: ')
    user_password = getpass.getpass('Enter password: ').lower()

    hashed_password = hash_password(user_password)

    for index, user in enumerate(user_db):
        if user['username'] == input_username and user['password'] == hashed_password:
            current_user = user_db[index]
            current_username = current_user['username']

            hello_text = f'Hello {current_username}! Current date and time: {datetime.now()}'

            logging.info(f'✅ Account change was successful! {current_username}')
            print('✅ Account change was successful!')

            return
            
    logging.error('❌ Incorrect username or password')
    print('❌ Incorrect username or password')
    
def create_financial_record():
    global current_user

    input_category = input('Please enter a category: ')
    input_limit = input('Enter the limit: ')

def main():
    while True:
        print()
        print(f"{Fore.BLUE}8888ba.88ba            88888888b oo                                              ")
        print(f"{Fore.BLUE}88  `8b  `8b           88                                                       ")
        print(f"{Fore.BLUE}88   88   88          a88aaaa    dP 88d888b. .d8888b. 88d888b. .d8888b. .d8888b. ")
        print(f"{Fore.BLUE}88   88   88 88888888  88        88 88'  `88 88'  `88 88'  `88 88'      88ooood8 ")
        print(f"{Fore.BLUE}88   88   88           88        88 88    88 88.  .88 88    88 88.  ... 88.  ... ")
        print(f"{Fore.BLUE}dP   dP   dP           dP        dP dP    dP `88888P8 dP    dP `88888P' `88888P' ")
        print(f"{Fore.BLUE}oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo")
        print()
        print(hello_text)
        print()
        print('1. Create profile \n2. Show all profiles \n3. Create financial record \n4. Show all financial records \n5. Delete specific financial record \n6. Delete all financial records \n7. Change user \n8. Download as Excel file \n9. Exit')
        print()

        input_option = input(f'{Fore.YELLOW}Select an option: {Style.RESET_ALL}')

        try:
            input_option = int(input_option)

            if input_option == 1:
                logging.info(f'☑️ Create profile')
                create_profile()
            
            if input_option == 2:
                logging.info(f'☑️ Output all users')
                for index, user in enumerate(user_db):
                    print(f'{index + 1}: {user['username']}')

            if input_option == 7:
                logging.info(f'☑️ Change user')
                change_user()
            
            if input_option == 9:
                logging.info('☑️ The program has completed its work.')
                break
        except ValueError:
            logging.error('❌ Invalid option')
            print('❌ Invalid option')

if __name__ == '__main__':
    main()