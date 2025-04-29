from colorama import Fore, Style, init
from openpyxl import Workbook
from datetime import datetime
import logging
import hashlib
import getpass
import os

init(autoreset=True)
financial_records = Workbook()

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

def activate_func(log, func):
    if len(user_db) == 0:
        print('Create a user to run this function!')
    else:
        logging.info(log) 
        func() 

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
        print('❌ Some fields are empty')
    else:
        if not check_password(user_password, password_check):
            logging.error('❌ Passwords do not match')
            print('❌ Passwords do not match')
        else:
            logging.info(f'✅ Profile created successfully! {username}')
            print('✅ Profile created successfully!')

            hashed_password = hash_password(user_password)
            user_db.append({'username': username, 'password': hashed_password, 'expenses': {}})

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

    input_category = input('Please enter a category: ').lower()
    input_sum = input('Enter the amount you spent: ')

    if not input_category or not input_sum:
        logging.error('❌ Some fields are empty')
        print('❌ Some fields are empty')
    else:
        try:
            input_sum = int(input_sum)

            user_password = getpass.getpass('Enter password: ').lower()
            hashed_password = hash_password(user_password)

            if current_user['password'] == hashed_password:
                current_user['expenses'].update({input_category: input_sum})

                logging.info(f'✅ Added new category with expenses')
                print('✅ Added new category with expenses')
            else:
                logging.error('❌ Incorrect password')
                print('❌ Incorrect password')
        except ValueError as e:
            logging.error(f'❌ {e}')
            print(f'❌ {e}')

def delete_specific_financial_record():
    global current_user

    input_category = input('Please enter a category: ').lower()

    if not input_category in current_user['expenses'] or not input_category:
        logging.error('❌ There is no such category')
        print('❌ There is no such category')       
    else:
        user_password = getpass.getpass('Enter password: ').lower()
        hashed_password = hash_password(user_password)

        if current_user['password'] == hashed_password:
            logging.error('✅ Category removed!')
            print('✅ Category removed!')   

            categories = current_user['expenses']
            categories.pop(input_category)
        else:
            logging.error('❌ Incorrect password')
            print('❌ Incorrect password')

def delete_all_financial_records():
    global current_user

    user_password = getpass.getpass('Enter password: ').lower()
    hashed_password = hash_password(user_password)

    if current_user['password'] == hashed_password:
        logging.error('✅ Financial records have been deleted!')
        print('✅ Financial records have been deleted!')   

        current_user['expenses'].clear()
    else:
        logging.error('❌ Incorrect password')
        print('❌ Incorrect password')

def download_as_excel_file():
    global current_user

    user_password = getpass.getpass('Enter password: ').lower()
    hashed_password = hash_password(user_password)

    if current_user['password'] == hashed_password:
        sheet = financial_records.active
        sheet.title = 'Financial records'

        for index, (key, value) in enumerate(current_user['expenses'].items()):
            sheet[f'A{index + 1}'] = f'{key}: {value}'

            financial_records.save("Financial recordss.xlsx")
            print('The file is saved to the root project folder.')
    else:
        logging.error('❌ Incorrect password')
        print('❌ Incorrect password')

def main():
    global current_user

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

        if input_option == '1':
            logging.info(f'☑️ Create profile')
            create_profile()
            
        if input_option == '2':
            logging.info(f'☑️ Output all users')
            for index, user in enumerate(user_db):
                print(f'{index + 1}: {user['username']} {user['expenses']}')                

        if input_option == '3':
            activate_func(log='☑️ Creating a financial entry', func=create_financial_record)

        if input_option == '4':
            logging.info(f'☑️ Output all financial records')
            financial_records = current_user['expenses']

            for key, value in financial_records.items():
                print(f'{key}: {value}')

        if input_option == '5':
            activate_func(log='☑️ Delete specific financial record', func=delete_specific_financial_record)

        if input_option == '6':
            activate_func(log='☑️ Delete all financial records', func=delete_all_financial_records)

        if input_option == '7':
            activate_func(log='☑️ Change user', func=change_user)
        
        if input_option == '8':
            activate_func(log='☑️ Download as Excel file', func=download_as_excel_file)

        if input_option == '9':
            logging.info('☑️ The program has completed its work.')
            break

if __name__ == '__main__':
    main()