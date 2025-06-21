import re

digit_text = "Tôi có 2 con mèo và 1 con chó."
pattern = r'\d'
if re.search(pattern, digit_text):
    print("Chuỗi có ít nhất một chữ số.")
else:
    print("Chuỗi KHÔNG có chữ số nào.")
    
        
