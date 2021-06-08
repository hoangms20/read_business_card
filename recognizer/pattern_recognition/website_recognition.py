def is_website(txt):
    txt = txt.encode().decode('utf8').lower()
    return txt.find("www.") >= 0 or txt.find('https://') >= 0 or txt.find('http://') >= 0
