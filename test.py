
from array import *

s =[ 
    "123",
    "555"
]

s.append("321")
l =len(s)
s[l - 1] += "456"

print(s)