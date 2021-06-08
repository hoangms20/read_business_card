import re

def is_phone(txt):
    m = re.findall(r'\d', txt)
    if len(m) >= 10:
        return True

    return False

    # m = re.findall(r'\d', txt)
    # if len(m) >= 10:aa
    #     return True
    # return False

if __name__ == '__main__':
 
    # Enter the email
    email = "TEL +810-852-1140"
 
    # calling run function
    if is_phone(email):
        print(1)
 
    email = "dy +81 3 5361-6699 && +81 3 3353-5588"
    if is_phone(email):
        print(2)
 
    email = "FAX +04866598701"
    if is_phone(email):
        print(3)