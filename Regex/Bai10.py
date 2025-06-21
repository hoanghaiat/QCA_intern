import re

nums = ["3.14", "0.5", "10.0", ".", "3.", "abc", "-1.2"]
pattern = r'^[0-9]+\.[0-9]+$'

for num in nums:
    if re.match(pattern, num):
        print(f"{num}  Hợp lệ")
    else:
        print(f"{num}  Không hợp lệ")
        
        
