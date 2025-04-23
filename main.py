from colorama import Fore, Style, init
from openpyxl import workbook
from datetime import datetime
import logging
import hashlib
import getpass

init(autoreset=True)

hello_text = f'Hello! To get started, create a profile. Current date and time: {datetime.now()}'
user_db = []
current_user = None

logging.basicConfig(
    level=logging.DEBUG,
    filename='./M-Finance.log',
    filemode='w',
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def check_password(password1, password2):
    return password1 == password2

def create_profile():
    global user_db
    global current_user
    global hello_text

    user_name = input('Enter your first and last name: ')
    user_password = getpass.getpass('Enter new password: ').strip()
    password_check = getpass.getpass('Please enter your password again: ').strip()

    if not user_name or not user_password or not password_check:
        logging.error('❌ Some fields are empty')
        print('❌ Some fields are empty')

    if not check_password(user_password, password_check):
        logging.error('❌ Some fields are empty')
        print('❌ Passwords do not match')
    
    logging.info(f'✅ Profile created successfully! {user_name}')
    print('✅ Profile created successfully!')

    hashed_password = hash_password(user_password)
    user_db.append({'user_name': user_name, 'password': hashed_password})

    current_user = user_db[0]['user_name']
    hello_text = f'Hello {current_user}! Current date and time: {datetime.now()}'

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
        print(hello_text)
        print('1. Create profile \n2. Show all profiles \n3. Create financial record \n4. Show all financial records \n5. Delete specific financial record \n6. Delete all financial records \n7. Change user \n8. Download as Excel file \n9. Exit')
        
        input_option = input(f'{Fore.YELLOW}Select an option:')

        try:
            input_option = int(input_option)

            if input_option == 1:
                create_profile()
            
            if input_option == 2:
                logging.info(f'Output all users')
                for index, user in enumerate(user_db):
                    print(f'{index + 1}: {user['user_name']}')
            
            if input_option == 9:
                logging.info('The program has completed its work.')
                break
        except ValueError:
            logging.error('❌ Invalid option')
            print('❌ Invalid option')

if __name__ == '__main__':
    main()