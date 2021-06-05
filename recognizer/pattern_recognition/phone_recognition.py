import re

def is_phone(txt):
    m = re.findall(r'\d', txt)
    if len(m) >= 10:
        return True
    return False