import re

dirty_text = "Hello! This is test123 #2025."

pattern = r'[^a-zA-Z]'
clean_text = re.sub(pattern, '', dirty_text)

print("Chuỗi sau khi loại bỏ ký tự không phải chữ cái:", clean_text)

