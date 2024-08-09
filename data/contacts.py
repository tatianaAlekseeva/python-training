from generator.data_generators import random_name, random_string, random_email, random_phone
from model.contact import Contact


testdata = [
    Contact(lastname=random_name(6), firstname=random_name(12), address=random_string(10),
            email2=random_email(7, "@test"), mobilephone=random_phone("+7(952)", 8))
]