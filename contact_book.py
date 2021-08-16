'''
Program that simulates a contact book where you can
add, manage, show and delete contacs and keep them in a .txt file
Program is made trying to avoid any incorrect input keeping the style,
that is why several prints are repeated making code more extense than it
could be
'''
import os
import time

ADD, SHOW, MANAGE, EXIT = '1', '2', '3', '0'
contacts = {}
file_name = 'contacts_database.txt'

def add_to_file(contacts, file_name):
    with open(file_name, 'w') as file:
        for name, info in contacts.items():
            file.write(f'{name},{info[0]},{info[1]}\n') # info tuple of len(2)
                                                        # phone and mail
def load_from_file(contacts, file_name):
    try:
        with open(file_name, 'r') as file:
            for row in file:
                name, phone, mail = row.strip().split(',')
                contacts[name] = (phone, mail)
    except FileNotFoundError:
        with open(file_name, 'w') as file:  # create the file if don´t exist
            pass

def show_menu():
    os.system('cls')
    print('\t# MY CONTACT BOOK #\n')
    print(f'\t({ADD}) Add contact\n\t({SHOW}) Show contact'
        f'\n\t({MANAGE}) Manage contact\n\t({EXIT}) Exit')
    option = input('\n\n\t>> SELECT -> ')

    return option

def add_contact(contacts, banner='ADD'):
    name = ''
    while len(name) == 0:
        os.system('cls')
        print('\t# MY CONTACT BOOK #\n')
        print(f'|{banner} contact|{"-"*15}\n')
        name = input('>> NAME: ').strip()
        if name in contacts:
            over_write = ''
            while over_write != 'n' and over_write != 'y':
                os.system('cls')
                print('\t# MY CONTACT BOOK #\n')
                print(f'|{banner} contact|{"-"*15}\n')
                print('>> NAME: ', name)
                over_write = input('\nThat contact name already exist!!'
                                    '  Overwrite? (y) (n)   >> ').lower()
            if over_write == 'n':
                name = ''  # to loop again 
            else:
                break
    phone = ''
    while phone[1:].isdigit() == False or phone == '+':
        # just '+' loop again
        os.system('cls')
        print('\t# MY CONTACT BOOK #\n')
        print(f'|{banner} contact|{"-"*15}\n')
        print('   NAME:', name)
        phone = input('>> PHONE: ').strip()
    mail = ''
    while len(mail) == 0:
        os.system('cls')
        print('\t# MY CONTACT BOOK #\n')
        print(f'|{banner} contact|{"-"*15}\n')
        print('   NAME:', name)
        print('   PHONE:', phone)
        mail = input('>> EMAIL: ').strip()
    save_contact = ''
    while save_contact not in ('1', '0'):
        os.system('cls')
        print('\t# MY CONTACT BOOK #\n')
        print(f'|{banner} contact|{"-"*15}\n')
        print('   NAME:', name)
        print('   PHONE:', phone)
        print('   EMAIL:', mail)
        save_contact = input('\n\n(1)SAVE contact    (0)CANCEL    >> ')
        if save_contact == '1':
            contacts[name.lower()] = (phone, mail)  # data to contacts dict
            add_to_file(contacts, file_name)    # data to external file .txt
            print(f'\nContact {banner + "ED"} successfully!!\n\n\n')
            option = ''  # get the option loop for further actions
        elif save_contact == '0':
            option = '0'  # dont get in the option loop and exit to main menu
        else:
            print('\n\tInvalid option!!')
            time.sleep(1.5)
    while option not in ('1', '2', '0'):
        os.system('cls')
        print('\t# MY CONTACT BOOK #\n')
        print(f'|{banner} contact|{"-"*15}\n')
        print('   NAME:', name)
        print('   PHONE:', phone)
        print('   EMAIL:', mail)
        print('\n\n(1)SAVE contact    (0)CANCEL    >> 1')
        print(f'\nContact {banner + "ED"} successfully!!\n\n\n')
        option = input('(1) ADD more contacts    (2) EDIT contact'
                        '    (0) MAIN MENU   >> ')
        if option == '1':
            add_contact(contacts)
            # banner is changed to default (might be EDIT) to next add
        elif option == '2':
            manage_contact(contacts)
        elif option == '0':
            break
        else:
            print('\n\tInvalid option!!')
            time.sleep(1.5)
        
def show_contact(contacts):
    if len(contacts) > 0:
        name = ''
        while len(name) == 0:
            os.system('cls')
            print('\t# MY CONTACT BOOK #\n')
            print('|SHOW contacts|' + '-'*15 + '\n')
            name = input('Type /a to show ALL'
                            '\n\n\t>> SEARCH: ').lower().strip()
        contact_match = []   # contacts regarding name searched
        option = ''
        while option not in ('1', '2', '0'):
            if name == '/a':  # show all contacts
                os.system('cls')
                print('\t# MY CONTACT BOOK #\n')
                print('|SHOW contacts|-------- Showing ALL ----\n')
                for contact, info in contacts.items():
                    contact_match.append((contact, info[0], info[1]))
                    # filling a list (ALL contacts in this case)
                    print('·'*40)
                    print(f'\t· Name: {contact.title()}'
                        f'\n\t· Phone: {info[0]}'
                        f'\n\t· Email: {info[1]}')
                    print('·' *40 + '\n')
            else:  # Search criteria to match
                os.system('cls')
                print('\t# MY CONTACT BOOK #\n')
                print(f'|SHOW contacts|-------- Showing "{name}" ----\n')
                for contact, info in contacts.items():
                    if contact.startswith(name):
                        # any key of contacts starting with value in name
                        contact_match.append((contact, info[0], info[1]))
                        # filling a list with matches according to name
                        print('·'*40)
                        print(f'\t· Name: {contact.title()}'
                            f'\n\t· Phone: {info[0]}'
                            f'\n\t· Email: {info[1]}')
                        print('·'*40 + '\n')
                if len(contact_match) == 0:  # any contact matches
                    print('\nAny contact, matches the criteria!!')
            option = input('\n\n\n(1) SHOW new contact'
                            '   (2) EDIT contact'
                            '   (0) MAIN MENU   >> ')
            if option == '1':
                show_contact(contacts)
            if option == '2':
                manage_contact(contacts, contact_match)
                # function call saving memory using just matches
            elif option == '0':
                break   # go to main menu
            else:
                print('\n\n\tInvalid option!!!')
                time.sleep(1.5)
    else:
        os.system('cls')
        print('\t# MY CONTACT BOOK #\n')
        print('|SHOW contacts|' + '-'*15 + '\n\n')
        print('There are no contacts to be shown!!')
        time.sleep(1.5)

def manage_contact(contacts, contact_match=[]):
    if len(contacts) > 0:
        if contact_match:
            # just loop the list with name matches
            to_manage = ''  # will choose what dairy key work with
            while (to_manage.isdigit() == False or
                1 > int(to_manage) or
                int(to_manage) > len(contact_match)
                ):
                os.system('cls')
                print('\t# MY CONTACT BOOK #\n')
                print('|MANAGE contacts|' + '-'*15 + '\n')
                print('CHOOSE contact to MANAGE\n')
                for info in contact_match:
                # info will be a tuple (name,phone,mail)  
                    print(f'\t({contact_match.index(info) + 1}) '
                        f'-> {info[0]}') # contact name in tuple
                    # show matches and use index value to classify them
                    # starting at 1
                to_manage = input('\n\n\t>> MANAGE contact: ').strip()
            to_manage = int(to_manage) - 1
            # set real index in contact_match
            contact = contact_match[to_manage][0]  
            action = ''
            while action not in ('0', '1', '2'):
                os.system('cls')                      
                print('\t# MY CONTACT BOOK #\n')
                print('|MANAGE contacts|' + '-'*15 + '\n')
                print(f'--- Contact: <<{contact.title()}>>\n\n')
                action = input(f'What you would like to do with '
                            f'{contact.title()}?\n\n'
                            f'(1)EDIT   (2)DELETE   (0)CANCEL\n\n'
                            '\t    >> ').strip()
                if action == '0':
                    break
                elif action == '1':
                    contacts.pop(contact)
                    # popped to avoid add_contact to ask for overwrite
                    add_contact(contacts, banner='EDIT') 
                elif action == '2':
                    contacts.pop(contact)
                    print('\n\n\tContact succesfully deleted')
                    time.sleep(1.5)
                else:
                    print('\n\n\tInvalid option!!!')
                    time.sleep(1.5)
        else:
            # no contact matches, so call show_contact and search name
            # in order to be able to edit
            show_contact(contacts)
    else:
        os.system('cls')
        print('\t# MY CONTACT BOOK #\n')
        print('|EDIT contacts|' + '-'*15 + '\n\n')
        print('No contacts to be edited!!')
        time.sleep(1.5)
                
def main():
    load_from_file(contacts, file_name)
    run_contact_book = True
    while run_contact_book:
        opt = show_menu()
        if opt == ADD:
            add_contact(contacts)
        elif opt == SHOW:
            show_contact(contacts)
        elif opt == MANAGE:
            manage_contact(contacts)
        elif opt == EXIT:
            run_contact_book = False
        else:
            input('\n\nInvalid option!!! Press ENTER to continue...')
        
if __name__ == '__main__':
    main()
        


        







