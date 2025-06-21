import re

# 1. Viết regex để kiểm tra xem một chuỗi có phải là email hợp lệ không.
# Email hợp lệ có dạng: chữ cái/số + @ + tên miền + .com
emails = ["test123@gmail.com", "abc@xyz", "user@domain.com", "invalid@.com"]

pattern = r'^[a-zA-Z0-9._]+@[a-zA-Z0-9]+\.(com)$'

for email in emails:
    if re.match(pattern, email):
        print(f"{email} ➜ Hợp lệ")
    else:
        print(f"{email} ➜ Không hợp lệ")
# 2. Tìm tất cả số điện thoại (gồm đúng 10 số, chia bởi dấu -)
phone_text = "Liên hệ 091-234-5678 hoặc 123-4567-890 để được tư vấn. Gọi 987-654-3210 ngay!"

phone_regex = r'\b(?:\d{3}-\d{3}-\d{4}|\d{3}-\d{4}-\d{3})\b'
phone_numbers = re.findall(phone_regex,phone_text)
print("Các số điện thoại hợp lệ:  ")
for phone in phone_numbers:
    print(f"➜{phone}")

# 3. Cho chuỗi đầu vào, kiểm tra xem trong chuỗi có ít nhất một chữ số không.
digit_text = "Tôi có 2 con mèo và 1 con chó."

digit_regex = r'\d'
if re.search(digit_regex,digit_text):
    print("Chuỗi có chứa ít nhất một chữ số!!")
else:
    print("Chuỗi không có chứa chữ số nào !!")




# 4. Cho một chuỗi, loại bỏ toàn bộ ký tự không phải chữ cái.
dirty_text = "Hello! This is test123 #2025."

dirty_regex = r'[^a-zA-Z]'
cleaned_text = re.sub(digit_regex," ", dirty_text)
print("Chuỗi sau khi loại bỏ ký tự không pải chữ cái: ", cleaned_text)



# 5. Kiểm tra chuỗi mật khẩu có phải là mật khẩu mạnh không.
# Tiêu chí: Tối thiểu 8 ký tự, ít nhất 1 chữ hoa, 1 chữ thường, 1 số
passwords = ["Abc12345", "abcdef", "ABC123456", "abcD1"]

password_regex = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$'
for password in passwords:
    if re.match(password_regex,password):
        print(f"{password} : mật khẩu mạnh")
    else:
        print(f"{password} : mật khẩu yếu")

# 6. Kiểm tra chuỗi có phải là ngày hợp lệ theo định dạng dd/mm/yyyy không
# (không xét tính hợp lệ theo lịch thực tế)
dates = ["18/06/2025", "31/13/2022", "00/12/2020", "5/6/2020"]

date_regex = r'^\d{2}/\d{2}/\d{4}$'
for date in dates:
    if re.match(date_regex,date):
        print(f"{date} : đúng định dạng")
    else:
        print(f"{date} : không đúng định dạng")


# 7. Tìm tất cả các từ viết hoa đứng đầu câu trong đoạn văn.
capital_text = "Today is a good day. My name is Hoa. How are you?"

capital_regex = r'(?:^|(?<=\.))([A-Z][a-z]*)'
results = re.findall(capital_regex,capital_text)
print("Các từ viết hoa đầu câu là: ")
for word in results:
    print(f"{word}")

# 8. Từ danh sách URL, trích ra phần tên miền chính (ví dụ: google, facebook).
urls = ["https://www.google.com", "http://facebook.com", "https://news.yahoo.com"]

url_regex = r'https?://(?:www\.|news\.)?([a-zA-Z0-9]+)\.'
for url in urls:
    match = re.search(url_regex,url)
    if match:
        domain = match.group(1)
        print(domain)


# 9. Tìm tất cả từ khóa bắt đầu bằng # trong đoạn văn bản.
hashtag_text = "Tôi yêu #Python và #MachineLearning, bạn có thích #AI không?"

hashtag_regex = r'#\w+'
results_tag = re.findall(hashtag_regex,hashtag_text)
print("Các hashtag tìm được là : ")
for tag in results_tag:
    print(tag)

# 10. Kiểm tra xem chuỗi có phải là số thực dương (thập phân) không.
# Hợp lệ: "3.14", "0.5", "10.0"
# Không hợp lệ: ".", "3.", "abc", "-1.2"
nums = ["3.14", "0.5", "10.0", ".", "3.", "abc", "-1.2"]

num_regex = r'^[0-9]+\.[0-9]+$'
for num in nums:
    if re.match(num_regex,num):
        print(f"{num} : hợp lệ")
    else:
        print(f"{num} : không hợp lệ")




# 11. Tìm và in ra tất cả các email trong chuỗi văn bản.
email_text = "Liên hệ qua email: support@example.com, admin@domain.org hoặc hello.world123@gmail.com."

email_regex = r'[a-zA-Z0-9._]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
emails = re.findall(email_regex,email_text)
print("DS email tìm thấy: ")
for email in emails:
    print(email)





# 12. Tìm các số nguyên hoặc thập phân dương/âm trong chuỗi.
number_text = "Nhiệt độ hôm nay là -10.5 độ, hôm qua là 25 và ngày mai có thể là -3."

number_regex = r'-?\d+(?:\.\d+)?'
numbers = re.findall(number_regex,number_text)
print("DS các số tìm được: ")
for number in numbers:
    print(number)



# 13. Tìm tất cả các từ dài hơn 6 ký tự trong câu.
long_word_text = "Programming in Python is sometimes enjoyable and sometimes frustrating."

word_regex = r'\b\w{7,}\b'
words = re.findall(word_regex,long_word_text)
print("DS các từ dài hơn 6 kí tự: ")
for word in words:
    print(word)



# 14. Mã bưu điện VN gồm 5 chữ số. Kiểm tra chuỗi có phải mã hợp lệ không.
postal_codes = ["70000", "123456", "ABCDE", "00000", "7500"]

postal_code_regex = r'^\d{5}$'
print("Kết quả tìm kiếm: ")
for code in postal_codes:
    if re.match(postal_code_regex,code):
        print(f"{code} : hợp lệ")
    else:
        print(f"{code} : không hợp lệ")


# 15. Trích xuất tất cả từ viết hoa toàn bộ (ví dụ như tên viết tắt, hoặc từ nhấn mạnh).
uppercase_text = "Chúng tôi làm việc với NASA, WHO và các tổ chức như UNICEF, nhưng không phải USAID."

uppercase_regex = r'\b[A-Z]{2,}\b'
uppercase_words = re.findall(uppercase_regex,uppercase_text)
print("DS các từ viết hoa toàn bộ: ")
for up_word in uppercase_words:
    print(up_word)