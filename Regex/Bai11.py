import re

email_text = "Liên hệ qua email: support@example.com, admin@domain.org hoặc hello.world123@gmail.com."

pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

emails = re.findall(pattern, email_text)

print("Các email tìm được:", emails)

