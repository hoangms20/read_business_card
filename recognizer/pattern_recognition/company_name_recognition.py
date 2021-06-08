import os
path = os.path.dirname(os.path.abspath(__file__))

common_company_tokens = []

with open(path + '/../data/common_prefix_suffix_company') as company_tokens:
    for token in company_tokens:
        comp_token = token.encode().decode('utf8').strip().lower()
        if len(comp_token) > 0:
            common_company_tokens.append(comp_token)


def is_company_name(line):
    line = line.encode().decode('utf8').lower().split(' ')
    for token in common_company_tokens:
        if line.__contains__(token):
            return True
    return False

if __name__ == '__main__':
    val = "Newbees co, Itd."
    if (is_company_name(val)):
        print("True")
