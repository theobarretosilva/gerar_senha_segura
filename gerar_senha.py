import secrets
import string

size_pswd = int(input("What password length do you want?\n"))
itens = (string.ascii_letters + string.ascii_lowercase + string.ascii_uppercase + string.digits)
pswd = [secrets.choice(itens) for i in range(size_pswd)]
pswd = ''.join(pswd)
