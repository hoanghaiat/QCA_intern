import re

uppercase_text = "Chúng tôi làm việc với NASA, WHO và các tổ chức như UNICEF, nhưng không phải USAID."

pattern = r'\b[A-Z]{2,}\b'

uppercase_words = re.findall(pattern, uppercase_text)

print("Từ viết hoa toàn bộ:", uppercase_words)