def is_email(txt):
    txt = txt.encode().decode('utf8').lower()
    return (len(txt) >= 5 and txt.find("@") > 0 and txt.find(".") > 0)