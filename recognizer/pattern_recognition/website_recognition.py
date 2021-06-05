def is_website(txt):
    txt = txt.encode().decode('utf8').lower()
    return txt.find("\\\\") >= 0 or txt.find("www") >= 0 or txt.find('http') >= 0
