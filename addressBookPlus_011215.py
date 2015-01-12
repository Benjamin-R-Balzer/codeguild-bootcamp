#create a command loop with these commands:
# - quit
# - add
# - list
# - remove
#
#Allows storage of name and phone #
#
#Add 'find' capability, a save-to-disk, and a reload
#
#What's up with Pickle: http://j.mp/PickleInPython

#filename addressBookPlus.py
# next steps: utilize name, Name, email, Email, phone, Phone.

import pickle
import os


class Contact:
    def __init__(self,name,email,phone):
        self.name=name
        self.email=email
        self.phone=phone
        
    def __str__(self):
        return "Name:{0}\nEmail address:{1}\nPhone:{2}".format(self.name,self.email,self.phone)
        
    def change_name(self,name):
        self.name=Name
        
    def change_email(self,email):
        self.email=Email
        
    def change_phone(self,phone):
        self.phone=Phone
        
def add_contact():
    address_book_plus_file=open("address_book_plus_file","r")
    #open file to read size
    is_file_empty=os.path.getsize("address_book_plus_file")==0
    #for error handling?
    if not is_file_empty:
        list_contacts=pickle.load(address_book_plus_file)
        #load to write all at once
    else:
        list_contacts=[]
    try:
        contact=collect_info()
    #assign "contact"
        address_book_plus_file=open("address_book_plus_file","wb")
    #open to write to file in binary
        list_contacts.append(contact)
    #add contents of "contact" to bottom of list_contacts
        pickle.dump(list_contacts,address_book_plus_file)
    #Write list_contacts in pickle format to address_book_plus_file
        print "Contact successfully added. Hot diggety.\n"
        menu()
    #return to menu
    except KeyboardInterrupt:
        print "You hit the brakes. The contact was not added. Crisis averted.\n"
        menu()
    except EOFError:
        print "End of file, Program. You're out of bounds. Contact not added.\n"
        menu()
    finally:
    #rem    address_book_plus_file.close() ??
        menu()
    
def collect_info():
    try:
        contact_name=raw_input("Enter contact name:\n")
        contact_email=raw_input("Enter contact email:\n")
        contact_phone=raw_input("Enter contact phone number:\n")
        contact=[contact_name,contact_email,contact_phone]
    #assign contact three raw_inputs above
        address_book_plus_file = open('address_book_plus_file','wb')
    #open file to write binary
        pickle.dump(contact,address_book_plus_file)
    ##Write contents of contact in pickle format to address_book_plus_file
        print contact, "Contact successfully added. Hot diggety.\n"
    #confirm for user contact add
        address_book_plus_file.close()
    #close file
        menu()
    #return to menu
        return contact
    #still needed?
    except EOFError as e:
        print "MCP says 'End of file.' Contact was not added.\n"
        raise e

    except KeyboardInterrupt as e:
        print "You hit the brakes. The contact was not added. What gives?\n"
        raise e

    
def browse_contacts():
    address_book_plus_file=open("address_book_plus_file","r")
    is_file_empty=os.path.getsize("address_book_plus_file")==0
    if not is_file_empty:
        list_contacts=pickle.load(address_book_plus_file)
        for each_contact in list_contacts:
            print each_contact
            restart()
    else:
        print "Address book empty. No contact to search. You should probably get out more, Krieger.\n"
        return

    
def search_contacts():
    search_name=raw_input("Enter the name to search by:\n")
    address_book_plus_file=open("address_book_plus_file","r")
    is_file_empty=os.path.getsize("address_book_plus_file")==0
    if not is_file_empty:
        search_name=raw_input("Enter the name to search by:\n")
        is_contact_found=False
        list_contacts=pickle.load(address_book_plus_file)
        for each_contact in list_contacts:
            contact_name=each_contact.name
            search_name=search_name.lower()
            contact_name=contact_name.lower()
            if contact_name==search_name:
                print each_contact
                is_contact_found=True
                restart()
        if not is_contact_found:
            print "No contact found with the provided search name. You sure she gave you her real name, Champ?\n"
            restart()
    else:
        print "Address book empty. No contact to search. You should probably get out more, Krieger.\n"
        address_book_plus_file.close()
        menu()

def del_contact():
    name=raw_input("Enter the name to be deleted:\n")
    address_book_plus_file=open("address_book_plus_file","r")
    is_file_empty=os.path.getsize("address_book_plus_file")==0
    if not is_file_empty:
        name=raw_input("Enter the name to be deleted:\n")
        list_contacts=pickle.load(address_book_plus_file)
        is_contact_deleted=False
        for i in range(0,len(list_contacts)):
            each_contact=list_contacts[i]
            if each_contact.name==name:
                del list_contacts[i]
                is_contact_deleted=True
                print "Contact has been disintegrated. Nice shootin', Tex.\n"
                address_book_plus_file=open("address_book_plus_file","w")
                if len(list_contacts)==0:
                    address_book_plus_file.write("")
                else:
                    pickle.dump(list_contacts,address_book_plus_file)
                restart()
        if not is_contact_deleted:
            print "Maaaan. We ain't found sh**.\n"
            menu()
            
    else:
        print "Address book empty. Damn. You should probably get out more, Krieger.\n"
    address_book_plus_file.close()
    menu()
    
def mod_contact():
    address_book_plus_file=open("address_book_plus_file","r")
    is_file_empty=os.path.getsize("address_book_plus_file")==0
    if not is_file_empty:
        name=raw_input("Enter the name of the contact to be modified:\n")
        list_contacts=pickle.load(address_book_plus_file)
        is_contact_modified=False
        for each_contact in list_contacts:
            if each_contact.name==name:
                do_modification(each_contact)
                address_book_plus_file=open("address_book_plus_file","w")
                pickle.dump(list_contacts,address_book_plus_file)
                is_contact_modified=True
                print "High-five, user! Contact has been modified.\n"
                restart()
        if not is_contact_modified:
            print "Maaaan. We ain't found sh**.\n"
            menu()
    else:
        print "Address book empty. Damn. You should probably get out more, Krieger.\n"
        address_book_plus_file.close()
        restart()

def do_modification(contact):
    try:
        while True:
            print ("Enter ['a'] to modify a contact's name, or ['b'] to modify their email, or ['c'] to modify their phone number, or ['d'] to quit without modifying.\n")
            choice=raw_input()
            if choice=="a":
                new_name=raw_input("Enter the name to change to:\n")
                contact.change_name(new_name)
                menu()
            elif choice=="b":
                new_email=raw_input("Enter new email:\n")
                contact.change_email(new_email)
                menu()
            elif choice=="c":
                new_phone=raw_input("Enter new phone number:\n")
                contact.change_phone(new_phone)
                menu()
            elif choice=="d":
                menu()
            else:
                print "You talkin' jive, turkey? Let's take it again from the top.\n"
                menu()
    except EOFError:
        print "End of file, Program. Contact not added.\n"
    except KeyboardInterrupt:
        print "You hit the brakes. The contact was not added. Crisis averted.\n"
        restart()

  
def menu():
    while True:
        print("\nIn this command line address book, you may:\nadd, delete, modify, search for,\nand/or view your contacts in a list.")
        print("Also, all of this information is saved (pickle) to disk. \nIn order for changes to show, please restart program.\n")
        print("To begin, please choose from the following:\nadd contact [enter '1'],\ndelete contact [enter '2'],")
        print("modify current info [enter '3'],\nsearch contacts [enter '4'],\nbrowse contacts [enter '5'],\nor exit [enter '6']")
        choice = raw_input()
        if choice == '1':
            print("You may add a contact to the address book.\n")
            collect_info()
        elif choice == '2':
            print("You may now completely delete a contact's info.\n")
            del_contact()
        elif choice == '3':
            print("Proceed modifying an existing contact's info.\n")
            mod_contact()
        elif choice == '4':
            print("Let's search for a specific contact.\n")
            search_contacts()
        elif choice == '5':
            print("You may browse your current list and relevant info.\n")
            browse_contacts()
        elif choice == '6':
            print("Leaving already? Will you at least call?\n")
            restart()
        else:
            print("You talkin' jive, turkey? Let's take it again from the top.\n")
            menu()
            
def restart():
    userinput = raw_input("Would you like to close out entirely, or stick around a bit and perform another operation? [y/n]\n ")
    if userinput == 'y':
        menu()
    elif userinput == 'n':
        print("Thank you, User, for giving me purpose! Come back soon! I'll be right here.\n")
    else:
        print("I don't understand your crazy moon-language, human. Restarting. Pull it together already.\n")
        restart()       

menu()
