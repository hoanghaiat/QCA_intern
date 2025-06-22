import re

def bai_1():
    print("\n== Bài 1: Kiểm tra email hợp lệ ==")
    emails = ["test123@gmail.com", "abc@xyz", "user@domain.com", "invalid@.com"]
    pattern = r'^[a-zA-Z0-9._]+@[a-zA-Z0-9]+\.(com)$'
    for email in emails:
        if re.match(pattern, email):
            print(f"{email} ➜ Hợp lệ")
        else:
            print(f"{email} ➜ Không hợp lệ")

def bai_2():
    print("\n== Bài 2: Tìm số điện thoại định dạng 10 số, có dấu gạch ==")
    text = "Liên hệ 091-234-5678 hoặc 123-4567-890 để được tư vấn. Gọi 987-654-3210 ngay!"
    pattern = r'\b(\d{3}-\d{3}-\d{4}|\d{3}-\d{4}-\d{3})\b'
    phones = re.findall(pattern, text)
    for phone in phones:
        print("Số điện thoại:", phone)

def bai_3():
    print("\n== Bài 3: Kiểm tra chuỗi có chứa chữ số không ==")
    text = "Tôi có 2 con mèo và 1 con chó."
    if re.search(r'\d', text):
        print("Chuỗi có chứa ít nhất một chữ số!")
    else:
        print("Chuỗi không chứa chữ số.")

def bai_4():
    print("\n== Bài 4: Loại bỏ ký tự không phải chữ cái ==")
    text = "Hello! This is test123 #2025."
    cleaned = re.sub(r'[^a-zA-Z\s]', '', text)
    print("Kết quả:", cleaned)

def bai_5():
    print("\n== Bài 5: Kiểm tra mật khẩu mạnh ==")
    passwords = ["Abc12345", "abcdef", "ABC123456", "abcD1"]
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$'
    for pwd in passwords:
        if re.match(pattern, pwd):
            print(f"{pwd} ➜ Mạnh")
        else:
            print(f"{pwd} ➜ Yếu")

def bai_6():
    print("\n== Bài 6: Kiểm tra định dạng ngày dd/mm/yyyy ==")
    dates = ["18/06/2025", "31/13/2022", "00/12/2020", "5/6/2020"]
    pattern = r'^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}$'
    for d in dates:
        if re.match(pattern, d):
            print(f"{d} ➜ Đúng")
        else:
            print(f"{d} ➜ Sai")

def bai_7():
    print("\n== Bài 7: Từ viết hoa đầu câu ==")
    text = "Today is a good day. My name is Hoa. How are you?"
    sentences = re.split(r'[.!?]\s*', text)
    words = []
    for s in sentences:
        if s:
            first_word = s.strip().split()[0]
            if first_word[0].isupper():
                words.append(first_word)
    print("Từ đầu câu:", words)

def bai_8():
    print("\n== Bài 8: Trích tên miền chính từ URL ==")
    urls = ["https://www.google.com", "http://facebook.com", "https://news.yahoo.com"]
    for url in urls:
        match = re.search(r'https?://(?:www\.|news\.)?([a-zA-Z0-9]+)\.', url)
        if match:
            print("Tên miền:", match.group(1))

def bai_9():
    print("\n== Bài 9: Tìm hashtag trong văn bản ==")
    text = "Tôi yêu #Python và #MachineLearning, bạn có thích #AI không?"
    print("Hashtags:", re.findall(r'#\w+', text))

def bai_10():
    print("\n== Bài 10: Kiểm tra số thực dương ==")
    nums = ["3.14", "0.5", "10.0", ".", "3.", "abc", "-1.2"]
    pattern = r'^[0-9]+\.[0-9]+$'
    for num in nums:
        if re.match(pattern, num):
            print(f"{num} ➜ Hợp lệ")
        else:
            print(f"{num} ➜ Không hợp lệ")

def bai_11():
    print("\n== Bài 11: Tìm email trong văn bản ==")
    text = "Liên hệ qua email: support@example.com, admin@domain.org hoặc hello.world123@gmail.com."
    print("Email tìm được:", re.findall(r'[a-zA-Z0-9._]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', text))

def bai_12():
    print("\n== Bài 12: Tìm số nguyên/thập phân dương và âm trong văn bản ==")
    text = "Nhiệt độ hôm nay là -10.5 độ, hôm qua là 25 và ngày mai có thể là -3."
    print("Các số:", re.findall(r'-?\d+(?:\.\d+)?', text))

def bai_13():
    print("\n== Bài 13: Tìm các từ dài hơn 6 ký tự ==")
    text = "Programming in Python is sometimes enjoyable and sometimes frustrating."
    print("Từ dài:", re.findall(r'\b\w{7,}\b', text))

def bai_14():
    print("\n== Bài 14: Kiểm tra mã bưu điện Việt Nam ==")
    codes = ["70000", "123456", "ABCDE", "00000", "7500"]
    pattern = r'^\d{5}$'
    for code in codes:
        if re.match(pattern, code):
            print(f"{code} ➜ Hợp lệ")
        else:
            print(f"{code} ➜ Không hợp lệ")

def bai_15():
    print("\n== Bài 15: Tìm từ viết hoa toàn bộ (tên viết tắt) ==")
    text = "Chúng tôi làm việc với NASA, WHO và các tổ chức như UNICEF, nhưng không phải USAID."
    print("Từ viết hoa:", re.findall(r'\b[A-Z]{2,}\b', text))

# Bộ chọn chạy hàm
function_list = {
    f"bai_{i}": globals()[f"bai_{i}"] for i in range(1, 16)
}

if __name__ == "__main__":
    user_input = input("Nhập các bài cần chạy (vd: bai_1,bai_2 hoặc all): ").strip().lower()
    if user_input == "all":
        for func in function_list.values():
            func()
    else:
        selected = [s.strip() for s in user_input.split(',')]
        for name in selected:
            if name in function_list:
                function_list[name]()
            else:
                print(f"Hàm '{name}' không tồn tại.")
