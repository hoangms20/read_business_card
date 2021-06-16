

from array import *

#import modules
from .pattern_recognition import common_name_recognition as name_recog
from .pattern_recognition.address_name_recognition import *
from .pattern_recognition.email_recognition import is_email
from .pattern_recognition.job_title_recognition import is_job_title
from .pattern_recognition.phone_recognition import is_phone
from .pattern_recognition.website_recognition import is_website
from .pattern_recognition.company_name_recognition import is_company_name
from . import card_region_detector as region_detector


class Contact(object):
    def __init__(self):
        self.name = 'N/A'
        self.emails = []
        self.phones = []
        self.job_title = []
        self.company = 'N/A'
        self.website = 'N/A'
        self.addr = []
        self.other_info = []

    def process_data(self, tokens):
        mask = array('i', [])

        for token in tokens:
            mask.append(0)
            print(token)

        print("****find****")
        i = -1
        l = len(mask)

        for token in tokens:
            i += 1

            if mask[i] != 0 :
                continue

            if is_website(token):
                mask[i] = 1
                self.website = token
                continue

            if is_email(token):
                mask[i] = 2
                self.emails.append(token)
                continue

            if is_phone(token):
                mask[i] = 3
                self.phones.append(token)
                continue

            if is_job_title(token):
                mask[i] = 4
                self.job_title.append(token)
                continue

            if is_address(token):
                mask[i] = 5
                self.addr.append(token)
                continue

            if is_company_name(token):
                mask[i] = 6
                self.company = token
                continue

            if name_recog.is_en_name(token) or name_recog.is_jp_name(token) or name_recog.is_vn_name(token):
                mask[i] = 7
                self.name = token
                continue
            
            j = i - 1
            if(j >= 0 and j <= l - 1):
                if mask[j] == 4 or mask[j] == 7:
                    mask[i] = 4
                    self.job_title.append(token)
                    continue
                
                if mask[j] == 5 and tokens[j][len(tokens[j]) - 1] == ',':
                    mask[i] = 5
                    lengcon = len(self.addr)
                    self.addr[lengcon - 1] += token
                    continue

                if mask[j] == 6:
                    mask[i] = 5
                    self.addr.append(token)
                    continue

            self.other_info.append(token)
            
        print("****finished****")
        print(tokens)
        i = -1
        for token in tokens:
            i+=1
            print(token +"-------" + str(mask[i]))

