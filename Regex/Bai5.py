import re

passwords = ["Abc12345", "abcdef", "ABC123456", "abcD1"]
pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$'

for pw in passwords:
    if re.match(pattern, pw):
        print(f"{pw} Mạnh")
    else:
        print(f"{pw} Yếu")
        


