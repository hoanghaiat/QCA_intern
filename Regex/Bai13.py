import re

long_word_text = "Programming in Python is sometimes enjoyable and sometimes frustrating."

pattern = r'\b\w{7,}\b'

long_words = re.findall(pattern, long_word_text)

print("Các từ dài hơn 6 ký tự:", long_words)  