from generator.data_generators import *
from model.contact import Contact


testdata = [
    Contact(lastname=random_name(6), firstname=random_name(12), address=random_string(10),
            email=random_email(6, "bor.com"), email2=random_email(7, "@test"),
            email3=random_email(10, "@kom.biz"), homephone=random_phone("+381", 7),
            mobilephone=random_phone("+7(952)", 8), workphone=random_phone("+7-981", 4),
            fax=random_phone("9-1-2", 8))
    for i in range(3)
]