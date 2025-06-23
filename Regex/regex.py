import re

def bai_1():
    # 1. Viết regex để kiểm tra xem một chuỗi có phải là email hợp lệ không.
    # Email hợp lệ có dạng: chữ cái/số + @ + tên miền + .com
    emails = ["test123@gmail.com", "abc@xyz", "user@domain.com", "invalid@.com"]
    print("\nRun bai_1")
    pattern = r'^[a-zA-Z0-9._]+@[a-zA-Z0-9]+\.(com)$'
    for email in emails:
        if re.match(pattern, email):
            print(f"{email} ➜ Hợp lệ")
        else:
            print(f"{email} ➜ Không hợp lệ")

def bai_2():
    # 2. Tìm tất cả số điện thoại (gồm đúng 10 số, chia bởi dấu -)
    phone_text = "Liên hệ 091-234-5678 hoặc 123-4567-890 để được tư vấn. Gọi 987-654-3210 ngay!"
    print("\nRun bai_2")
    pattern_phone = r'\b\d{3}-\d{3}-\d{4}\b'
    phone_number = re.findall(pattern_phone, phone_text)
    if not phone_number:
        print("Không tìm thấy số điện thoại hợp lệ")
    else:
        print("Các số điện thoại hợp lệ",phone_number)


def bai_3():
    # 3. Cho chuỗi đầu vào, kiểm tra xem trong chuỗi có ít nhất một chữ số không.
    digit_text = "Tôi có 2 con mèo và 1 con chó."
    
    print("\nRun bai_3")
    pattern_digit = r'\d'
    if re.search(pattern_digit, digit_text):
        print("Chuỗi chứa ít nhất một chữ số")
    else:
        print("Chuỗi không chứa chữ số nào")


def bai_4():
   # 4. Cho một chuỗi, loại bỏ toàn bộ ký tự không phải chữ cái.
    dirty_text = "Hello! This is test123 #2025."     
    
    print("\nRun bai_4")
    pattern_clean = r'[^a-zA-Z\s]'
    cleaned_text = re.sub(pattern_clean, '', dirty_text)
    print("Chuỗi sau khi loại bỏ ký tự không phải chữ cái", cleaned_text)

def bai_5():
    # 5. Kiểm tra chuỗi mật khẩu có phải là mật khẩu mạnh không.
    # Tiêu chí: Tối thiểu 8 ký tự, ít nhất 1 chữ hoa, 1 chữ thường, 1 số
    passwords = ["Abc12345", "abcdef", "ABC123456", "abcD1"]
    print("\nRun bai_5")
    pattern_password = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,}$'
    for password in passwords:
        if re.match(pattern_password, password):
            print(f"{password} ➜ Mật khẩu mạnh")
        else:
            print(f"{password} ➜ Mật khẩu yếu")


def bai_6():
    # 6. Kiểm tra chuỗi có phải là ngày hợp lệ theo định dạng dd/mm/yyyy không
    # (không xét tính hợp lệ theo lịch thực tế)
    dates = ["18/06/2025", "31/13/2022", "00/12/2020", "5/6/2020"]
        
    print("\nRun bai_6")
    pattern_date = r'^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}$'
    for date in dates:
        if re.match(pattern_date, date):
            print(f"{date} ➜ Ngày hợp lệ")
        else:
            print(f"{date} ➜ Ngày không hợp lệ")


def bai_7():
    # 7. Tìm tất cả các từ viết hoa đứng đầu câu trong đoạn văn.
    capital_text = "Today is a good day. My name is Hoa. How are you?"    
    
    print("\nRun bai_7")
    pattern_capital = r'\b[A-Z][a-z]*\b'
    capital_word = re.findall(pattern_capital, capital_text)
    print("Các từ viết hoa đứng đầu câu:", capital_word)


def bai_8():
    # 8. Từ danh sách URL, trích ra phần tên miền chính (ví dụ: google, facebook).
    urls = ["https://www.google.com", "http://facebook.com", "https://news.yahoo.com"]
 
    print("\nRun bai_8")
    url_regex = r'https?://(?:www\.|news\.)?([a-zA-Z0-9]+)\.'
    for url in urls:
        match = re.search(url_regex,url)
        if match:
            domain = match.group(1)
            print(domain)


def bai_9():
    # 9. Tìm tất cả từ khóa bắt đầu bằng # trong đoạn văn bản.
    hashtag_text = "Tôi yêu #Python và #MachineLearning, bạn có thích #AI không?"    
    
    print("\nRun bai_9")
    pattern_hashtag = r'#\w+'
    hashtag_word = re.findall(pattern_hashtag, hashtag_text)
    print("Các từ khóa bắt đầu bằng #:", hashtag_word)


def bai_10():
    # 10. Kiểm tra xem chuỗi có phải là số thực dương (thập phân) không.
    # Hợp lệ: "3.14", "0.5", "10.0"
    # Không hợp lệ: ".", "3.", "abc", "-1.2"
    nums = ["3.14", "0.5", "10.0", ".", "3.", "abc", "-1.2"]    
    
    print("\nRun bai_10")
    pattern_float = r'^\d+(\.\d+)?$'
    for num in nums:
        if re.match(pattern_float, num):
            print(f"{num} ➜ Là số thực dương")
        else:
            print(f"{num} ➜ Không phải số thực dương")


def bai_11():
    # 11. Tìm và in ra tất cả các email trong chuỗi văn bản.
    email_text = "Liên hệ qua email: support@example.com, admin@domain.org hoặc hello.world123@gmail.com."    
    
    print("\nRun bai_11")
    pattern_email = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    emails = re.findall(pattern_email, email_text)
    if emails:
        print("Các email tìm thấy:", emails)
    else:
        print("Không tìm thấy email nào hợp lệ")

def bai_12():
    # 12. Tìm các số nguyên hoặc thập phân dương/âm trong chuỗi.
    number_text = "Nhiệt độ hôm nay là -10.5 độ, hôm qua là 25 và ngày mai có thể là -3."    
    
    print("\nRun bai_12")
    pattern_number = r'[-+]?\d+(\.\d+)?'
    numbers = re.findall(pattern_number, number_text)
    print("Các số nguyên hoặc thập phân dương/âm:", numbers)

def bai_13():
    # 13. Tìm tất cả các từ dài hơn 6 ký tự trong câu.
    long_word_text = "Programming in Python is sometimes enjoyable and sometimes frustrating."    
    
    print("\nRun bai_13")
    pattern_long_word = r'\b\w{7,}\b'
    long_word = re.findall(pattern_long_word, long_word_text)
    print("Từ dài hơn 6 ký tự", long_word)
 

def bai_14():
    # 14. Mã bư`u điện VN gồm 5 chữ số. Kiểm tra chuỗi có phải mã hợp lệ không.
    postal_codes = ["70000", "123456", "ABCDE", "00000", "7500"]
    
    print("\nRun bai_14")
    pattern_postal_code = r'^\d{5}$'
    for postal_code in postal_codes:
        if re.match(pattern_postal_code, postal_code):
            print(f"{postal_code} ➜ Là mã bưu điện hợp lệ")
        else:
            print(f"{postal_code} ➜ Không phải mã bưu điện hợp lệ")


def bai_15():
    # 15. Trích xuất tất cả từ viết hoa toàn bộ (ví dụ như tên viết tắt, hoặc từ nhấn mạnh).
    uppercase_text = "Chúng tôi làm việc với NASA, WHO và các tổ chức như UNICEF, nhưng không phải USAID."    
    
    print("\nRun bai_15")
    pattern_uppercase = r'\b[A-Z]{2,}\b'
    uppercase_words = re.findall(pattern_uppercase, uppercase_text)
    print("Các từ viết hoa toàn bộ", uppercase_words)



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