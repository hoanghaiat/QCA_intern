import re

dates = ["18/06/2025", "31/13/2022", "00/12/2020", "5/6/2020"]
pattern = r'^\d{2}/\d{2}/\d{4}$'

for date in dates:
    if re.match(pattern, date):
        print(f"{date} Định dạng hợp lệ ")
    else:
        print(f"{date} Định dạng không hợp lệ")
        

