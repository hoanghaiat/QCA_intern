import re

capital_text = "Today is a good day. My name is Hoa. How are you?"

pattern = r'\s*([A-Z][a-z]*)'

sentences = re.split(r'[.!?]\s*', capital_text)

capital_words = []

for sentence in sentences:
    match = re.match(pattern, sentence)
    if match:
        capital_words.append(match.group(1))

print("Từ viết hoa đầu câu:", capital_words)

