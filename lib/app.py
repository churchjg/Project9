import peewee
from peewee import *



db = PostgresqlDatabase('people', user='peopleuser', password='jon',
                        host='localhost', port=5432)

db.connect()

class BaseModel(Model):
    class Meta:
        database = db

class Contacts(BaseModel):
    first_name = CharField()
    last_name = CharField()
    number = CharField()
   

db.drop_tables([Contacts])
db.create_tables([Contacts])


will = Contacts(first_name='Will', last_name='Drougas', number='555-111-9999' )
will.save()


steph = Contacts(first_name='Stephanie', last_name='Becker', number='333-555-9999' )
steph.save()

andrea = Contacts(first_name='Andrea', last_name='Church', number='111-777-8888' )
andrea.save()

dad = Contacts(first_name='Jon', last_name='Church Sr.', number='999-111-8888' )
dad.save()

sarah = Contacts(first_name='Sarah', last_name='Braatz', number='555-666-9999' )
sarah.save()

shawn = Contacts(first_name='Shawn', last_name='Clement', number='555-666-9999' )
shawn.save()




def directory():
    print('Welcome to your contacts directory, you can use \n 1: Contacts \n 2: Add New Contact \n 3: Find Contact \n 4: Exit')
    pick = int(input('Enter Number: '))
    if pick == 1:
        show_contacts()
    elif pick == 2: 
        create_contact()
    elif pick == 3:
        find_contact()
    else:
        exit()

# Show all Contact
def show_contacts():
    contacts = Contacts.select()
    for contact in contacts:
        print(f'Full Name: {contact.first_name} {contact.last_name}  \n Number: {contact.number}')
    
    exit = input('To exit press $')
    if exit == '$':
        directory()


# create
def create_contact():
    new_first_name = input('Enter first name: ')
    new_last_name = input('Enter last name: ')
    new_phone_number = input('Enter new phone number: ')

    new = Contacts(
        first_name = new_first_name,
        last_name = new_last_name,
        number = new_phone_number
    )
    new.save()
    directory()

# find contact by first name 
def find_contact():
    search = input("Enter the name of the contact you wish to search: ")
    search_contact = Contacts.select().where(Contacts.first_name == search)
    for contact in search_contact:
        print(f'Full Name: {contact.first_name} {contact.last_name} \n Number: {contact.number}')
    
    directory()
        


directory()




