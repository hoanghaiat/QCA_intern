import re
from urllib.parse import urlparse

def bai_1():
    # 1. Viết regex để kiểm tra xem một chuỗi có phải là email hợp lệ không.
    # Email hợp lệ có dạng: chữ cái/số + @ + tên miền + .com
    emails = ["test123@gmail.com", "abc@xyz", "user@domain.com", "invalid@.com"]

    pattern = r'^[a-zA-Z0-9._]+@[a-zA-Z0-9]+\.(com)$'
    print("\nRun bai_1")
    for email in emails:
        if re.match(pattern, email):
            print(f"{email} ➜ Hợp lệ")
        else:
            print(f"{email} ➜ Không hợp lệ")

def bai_2():
    # 2. Tìm tất cả số điện thoại (gồm đúng 10 số, chia bởi dấu -)
    phone_text = "Liên hệ 091-234-5678 hoặc 123-4567-890 để được tư vấn. Gọi 987-654-3210 ngay!"
    
    print("\nRun bai_2")
    pattern = r'\b(\d{3}-\d{3}-\d{4}|\d{3}-\d{4}-\d{3})\b'
    phone = re.findall(pattern, phone_text)
    print("Số điện thoại hợp lệ gồm đúng 10 số chia bởi dấu '-':", phone)

def bai_3():
    # 3. Cho chuỗi đầu vào, kiểm tra xem trong chuỗi có ít nhất một chữ số không.
    digit_text = "Tôi có 2 con mèo và 1 con chó."
    
    print("\nRun bai_3")
    pattern = r'\d'
    if re.search(pattern, digit_text):
        print("Chuỗi có ít nhất một chữ số.")
    else:
        print("Chuỗi KHÔNG có chữ số nào.")

def bai_4():
   # 4. Cho một chuỗi, loại bỏ toàn bộ ký tự không phải chữ cái.
    dirty_text = "Hello! This is test123 #2025."     
    
    print("\nRun bai_4")
    pattern = r'[^a-zA-Z]'
    clean_text = re.sub(pattern, '', dirty_text)
    print("Chuỗi sau khi loại bỏ ký tự không phải chữ cái:", clean_text)

def bai_5():
    # 5. Kiểm tra chuỗi mật khẩu có phải là mật khẩu mạnh không.
    # Tiêu chí: Tối thiểu 8 ký tự, ít nhất 1 chữ hoa, 1 chữ thường, 1 số
    passwords = ["Abc12345", "abcdef", "ABC123456", "abcD1"]    
    
    print("\nRun bai_5")
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$'
    for pw in passwords:
        if re.match(pattern, pw):
            print(f"{pw} Mạnh")
        else:
            print(f"{pw} Yếu")

def bai_6():
    # 6. Kiểm tra chuỗi có phải là ngày hợp lệ theo định dạng dd/mm/yyyy không
    # (không xét tính hợp lệ theo lịch thực tế)
    dates = ["18/06/2025", "31/13/2022", "00/12/2020", "5/6/2020"]    
    
    print("\nRun bai_6")
    pattern = r'^(0?[1-9]|[12][0-9]|3[01])/(0?[1-9]|1[0-2])/\d{4}$'
    for date in dates:
        if re.match(pattern, date):
            print(f"{date} Định dạng hợp lệ ")
        else:
            print(f"{date} Định dạng không hợp lệ")

def bai_7():
    # 7. Tìm tất cả các từ viết hoa đứng đầu câu trong đoạn văn.
    capital_text = "Today is a good day. My name is Hoa. How are you?"    
    
    print("\nRun bai_7")
    sentences = re.split(r'[.!?]\s*', capital_text)
    capital_words = []

    for sentence in sentences:
        sentence = sentence.strip()
        if not sentence:
            continue
        match = re.match(r'[A-Z][a-z]*', sentence)
        if match:
            capital_words.append(match.group())

    print("Từ viết hoa đầu câu:", capital_words)

def bai_8():
    # 8. Từ danh sách URL, trích ra phần tên miền chính (ví dụ: google, facebook).
    urls = ["https://www.google.com", "http://facebook.com", "https://news.yahoo.com",  "https://blog.facebook.com"]    
    
    print("\nRun bai_8")
    for url in urls:
        domain = urlparse(url).netloc
        parts = domain.split('.')
        if len(parts) >= 2:
            main_domain = parts[-2]  # Lấy phần đứng trước TLD
            print(f"{url} ➜ {main_domain}")

def bai_9():
    # 9. Tìm tất cả từ khóa bắt đầu bằng # trong đoạn văn bản.
    hashtag_text = "Tôi yêu #Python và #MachineLearning, bạn có thích #AI không?"    
    
    print("\nRun bai_9")
    pattern = r'#\w+'
    hashtags = re.findall(pattern, hashtag_text)
    print("Các hashtag tìm được:", hashtags)

def bai_10():
    # 10. Kiểm tra xem chuỗi có phải là số thực dương (thập phân) không.
    # Hợp lệ: "3.14", "0.5", "10.0"
    # Không hợp lệ: ".", "3.", "abc", "-1.2"
    nums = ["3.14", "0.5", "10.0", ".", "3.", "abc", "-1.2"]    
    
    print("\nRun bai_10")
    pattern = r'^[0-9]+\.[0-9]+$'
    for num in nums:
        if re.match(pattern, num):
            print(f"{num}  Hợp lệ")
        else:
            print(f"{num}  Không hợp lệ")

def bai_11():
    # 11. Tìm và in ra tất cả các email trong chuỗi văn bản.
    email_text = "Liên hệ qua email: support@example.com, admin@domain.org hoặc hello.world123@gmail.com."    
    
    print("\nRun bai_11")
    pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    emails = re.findall(pattern, email_text)
    print("Các email tìm được:", emails)

def bai_12():
    # 12. Tìm các số nguyên hoặc thập phân dương/âm trong chuỗi.
    number_text = "Nhiệt độ hôm nay là -10.5 độ, hôm qua là 25 và ngày mai có thể là -3."    
    
    print("\nRun bai_12")
    pattern = r'[-+]?\d+(\.\d+)?'
    # numbers = re.findall(pattern, number_text)     ??????
    matches = re.finditer(r'[-+]?\d+(?:\.\d+)?', number_text)
    results = [match.group() for match in matches]
    print("Các số tìm được:", results)

def bai_13():
    # 13. Tìm tất cả các từ dài hơn 6 ký tự trong câu.
    long_word_text = "Programming in Python is sometimes enjoyable and sometimes frustrating."    
    
    print("\nRun bai_13")
    pattern = r'\b\w{7,}\b'
    long_words = re.findall(pattern, long_word_text)
    print("Các từ dài hơn 6 ký tự:", long_words)  

def bai_14():
    # 14. Mã bư`u điện VN gồm 5 chữ số. Kiểm tra chuỗi có phải mã hợp lệ không.
    postal_codes = ["70000", "123456", "ABCDE", "00000", "7500"]
    
    print("\nRun bai_14")
    pattern = r'^\d{5}$'  
    for code in postal_codes:
        if re.fullmatch(pattern, code):
            print(f"{code} Mã hợp lệ")
        else:
            print(f"{code} Mã không hợp lệ")

def bai_15():
    # 15. Trích xuất tất cả từ viết hoa toàn bộ (ví dụ như tên viết tắt, hoặc từ nhấn mạnh).
    uppercase_text = "Chúng tôi làm việc với NASA, WHO và các tổ chức như UNICEF, nhưng không phải USAID."    
    
    print("\nRun bai_15")
    pattern = r'\b[A-Z]{2,}\b'
    uppercase_words = re.findall(pattern, uppercase_text)
    print("Từ viết hoa toàn bộ:", uppercase_words)


user_input = input("Enter functions to run: ").strip()

function_list = {
    "bai_1": bai_1,
    "bai_2": bai_2,
    "bai_3": bai_3,
    "bai_4": bai_4,
    "bai_5": bai_5,
    "bai_6": bai_6,
    "bai_7": bai_7,
    "bai_8": bai_8,
    "bai_9": bai_9,
    "bai_10": bai_10,
    "bai_11": bai_11,
    "bai_12": bai_12,
    "bai_13": bai_13,
    "bai_14": bai_14,
    "bai_15": bai_15,
}
if user_input.lower() == "all":
    print("Running all functions:")
    for func in function_list.values():
        func()
else:
    selected_functions = [name.strip() for name in user_input.split(',')]
    for name in selected_functions:
        if name in function_list:
            function_list[name]()
        else:
            print(f"Function '{name}' does not exist.")
