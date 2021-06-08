import os
import re
path = os.path.dirname(os.path.abspath(__file__))

from difflib import SequenceMatcher

common_name_jp = []
common_name_vi = []
common_name_en = []

SIMILAR_THRESHOLD = 0.80
MIN_LENGTH = 5

# Load data
with open(file= path + '/../data/common_name_en', mode='r', encoding="utf8") as en_name:
    for line in en_name:
        name = line.strip().lower()
        common_name_en.append(name)

with open(file= path + '/../data/common_name_jp', mode='r', encoding="utf8") as jp_name:
    for line in jp_name:
        name = line.strip().lower()
        common_name_jp.append(name)

with open(file= path + '/../data/common_name_vi', mode='r', encoding="utf8") as vi_name:
    for line in vi_name:
        name = line.strip().lower()
        common_name_vi.append(name)


def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


def scan_line(line, dict):
    sub_tokens = [tok.encode().decode('utf8').lower() for tok in line.split()]
    best_guess, best_name = 0, ''

    for sub_token in sub_tokens:
        token_guess, token_match = check(sub_token, dict)
        if token_guess > best_guess:
            best_guess, best_name = token_guess, token_match
    return [best_guess, best_name]


def check(token, dict):
    best_guess, guess_name = 0, ''

    for name in dict:
        guess = similar(token, name)
        if guess > best_guess:
            best_guess, guess_name = guess, name
    return [best_guess, guess_name]


# Find highest probability of a token may be a name
def find_best_guessed_name(tokens):
    best_jp_guess, best_jp_name, full_jp_name = 0, '', ''
    best_en_guess, best_en_name, full_en_name = 0, '', ''
    best_vi_guess, best_vi_name, full_vi_name = 0, '', ''

    for token in tokens:
        en_guess, en_name = scan_line(token, common_name_en)
        jp_guess, jp_name = scan_line(token, common_name_jp)
        vi_guess, vi_name = scan_line(token, common_name_vi)
        print("en" , (token, en_guess, en_name))
        print("ja" , (token, jp_guess, jp_name))

        if en_guess > best_en_guess:
            best_en_guess, best_en_name, full_en_name = en_guess, en_name, token
        if jp_guess > best_jp_guess:
            best_jp_guess, best_jp_name, full_jp_name = jp_guess, jp_name, token
        if vi_guess > best_vi_guess:
            best_vi_guess, best_vi_name, full_vi_name = vi_guess, best_vi_name, token

    # print('en', best_en_guess, best_en_name)
    # english for now
    # return [best_en_guess, best_en_name, full_en_name]

    best_guess, best_name, full_name = 0, '', ''
    if best_en_guess > best_guess:
        best_guess, best_name, full_name = best_en_guess, best_en_name, full_en_name

    if best_jp_guess > best_guess:
        best_guess, best_name, full_name = best_jp_guess, best_jp_name, full_jp_name

    if best_vi_guess > best_guess:
        best_guess, best_name, full_name = best_vi_guess, best_vi_name, full_vi_name

    return [best_guess, best_name, full_name]


def is_name(token):
    sub_tokens = [tok.encode().decode('utf8').lower() for tok in token.split()]
    a= len(sub_tokens)
    if (a <= 1 or a >= 3):
        return False

    for sub_token in sub_tokens:
        if is_en_name(sub_token) or is_jp_name(sub_token) or is_vn_name(sub_token):
            return True
    return False


def is_jp_name(token):
    sub_tokens = [tok.encode().decode('utf8').lower() for tok in token.split()]
    a= len(sub_tokens)
    m = re.findall(r'\w', token)
    n = re.findall(r'\d', token)


    if(len(token) - a + 1 != len(m) - len(n)):
        return False

    if (a <= 1 or a >= 4):
        return False

    for sub_token in sub_tokens:
        for name_jp in common_name_jp:
            if sub_token == name_jp:
                return True
    return False


def is_vn_name(token):
    sub_tokens = [tok.encode().decode('utf8').lower() for tok in token.split()]
    a= len(sub_tokens)

    m = re.findall(r'\w', token)
    n = re.findall(r'\d', token)

    if(len(token) - a + 1 != len(m) - len(n)):
        return False

    if (a <= 2 or a >= 5):
        return False

    first_name = sub_tokens[0] +' ' + sub_tokens[1]

    for name_vi in common_name_vi:
        if first_name == name_vi:
            return True

    return False


def is_en_name(token):
    # best_guess, name = check(token, common_name_en)
    # if best_guess > SIMILAR_THRESHOLD:
    #     return True

    sub_tokens = [tok.encode().decode('utf8').lower() for tok in token.split()]
    a= len(sub_tokens)
    m = re.findall(r'\w', token)
    n = re.findall(r'\d', token)


    if(len(token) - a + 1 != len(m) - len(n)):
        return False

    if (a <= 1 or a >= 4):
        return False

    for sub_token in sub_tokens:
        for name_en in common_name_en:
            if sub_token == name_en:
                return True
    return False

if __name__ == '__main__':
    val = "Masuo Fukada"
    if(is_en_name(val) or is_jp_name(val) or is_vn_name(val)):
        print("True")

    else:
        print("False")