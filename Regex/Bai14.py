import re

postal_codes = ["70000", "123456", "ABCDE", "00000", "7500"]

pattern = r'^\d{5}$'  

for code in postal_codes:
    if re.fullmatch(pattern, code):
        print(f"{code} Mã hợp lệ")
    else:
        print(f"{code} Mã không hợp lệ")
        
