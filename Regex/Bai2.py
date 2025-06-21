import re

phone_text = "Liên hệ 091-234-5678 hoặc 123-4567-890 để được tư vấn. Gọi 987-654-3210 ngay!"

pattern = r'\b(\d{3}-\d{3}-\d{4}|\d{3}-\d{4}-\d{3})\b'

phone = re.findall(pattern, phone_text)

print("Số điện thoại hợp lệ gồm đúng 10 số chia bởi dấu '-':", phone)

