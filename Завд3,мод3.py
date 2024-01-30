# не знаю як це скласти до купи
import re

def normalize_phone(phone_number):
    phone_number = '''
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   "
    '''
    patern = r"[\s|()|+|\\|\-|a-z]"
    repl = ""
    normalize_phone = re.sub(patern, repl, phone_number) 

    if len(normalize_phone) == 10:
        normalize_phone.insert(0, "+38")
    elif len(normalize_phone) == 11:
        normalize_phone.insert(0, "+3")
    elif len(normalize_phone) == 12:
        normalize_phone.insert(0, "+")
    elif len(normalize_phone) == 13:
        print(normalize_phone)
    elif len(normalize_phone) > 13:
        print("Wrong format")
    return normalize_phone

print(normalize_phone(phone_number))



                          