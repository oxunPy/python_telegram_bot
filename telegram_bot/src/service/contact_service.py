from telebot.types import Contact

class ContactService:

    def saveContact(self, contact: Contact):
        print(contact)
        return True