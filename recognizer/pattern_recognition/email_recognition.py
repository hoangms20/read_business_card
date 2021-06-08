import re

# Make a regular expression
# for validating an Email
regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
 
# Define a function for
# for validating an Email
 
 
def check(email):
 
    # pass the regular expression
    # and the string in search() method
    if(re.search(regex, email)):
        return True
 
    return False

def is_email(txt):
    #txt = txt.encode().decode('utf8').lower()
    # return (len(txt) >= 5 and txt.find("@") > 0 and txt.find(".") > 0)

    emails =  txt.split()
    for res in emails:
        if check(res):
            return True

    return False

if __name__ == '__main__':
 
    # Enter the email
    email = "E-mail ankitrai326@gmail.com"
 
    # calling run function
    is_email(email)
 
    email = "my.ownsite@our-earth.org"
    is_email(email)
 
    email = "ankitrai326@.com"
    is_email(email)