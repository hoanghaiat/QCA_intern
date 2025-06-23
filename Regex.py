import re

def bai_1():
    print("\n== Bài 1: Kiểm tra email hợp lệ ==")
    emails = ["test123@gmail.com", "abc@xyz", "user@domain.com", "invalid@.com"]
    pattern = r'^[a-zA-Z0-9._]+@[a-zA-Z0-9]+\.(com)$'
    for email in emails:
        print(f"{email} ➜ {'Hợp lệ' if re.match(pattern, email) else 'Không hợp lệ'}")

def bai_2():
    print("\n== Bài 2: Tìm số điện thoại định dạng 10 số có dấu gạch ==")
    text = "Liên hệ 091-234-5678 hoặc 123-4567-890 để được tư vấn. Gọi 987-654-3210 ngay!"
    pattern = r'\b\d{3}-(\d{3}-\d{4}|\d{4}-\d{3})\b'
    phones = re.findall(pattern, text)
    for phone in phones:
        print("Số điện thoại:", f"***-{phone}")

def bai_3():
    print("\n== Bài 3: Kiểm tra chuỗi có chứa chữ số không ==")
    text = "Tôi có 2 con mèo và 1 con chó."
    print("Có chứa chữ số!" if re.search(r'\d', text) else "Không chứa chữ số.")

def bai_4():
    print("\n== Bài 4: Loại bỏ ký tự không phải chữ cái ==")
    text = "Hello! This is test123 #2025."
    cleaned = re.sub(r'[^A-Za-z\s]', '', text)
    print("Chuỗi sau làm sạch:", cleaned.strip())
import re

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
    print("\n== Bài 6: Kiểm tra ngày định dạng dd/mm/yyyy ==")
    dates = ["18/06/2025", "31/13/2022", "00/12/2020", "5/6/2020"]
    pattern = r'^(0?[1-9]|[12][0-9]|3[01])/(0?[1-9]|1[0-2])/\d{4}$'
    for date in dates:
        result = "Hợp lệ" if re.match(pattern, date) else "Không hợp lệ"
        print(f"{date} ➜ {result}")

def bai_7():
    print("\n== Bài 7: Từ viết hoa đầu câu ==")
    text = "Today is a good day. My name is Hoa. How are you?"
    words = re.findall(r'(?:^|(?<=\.\s))([A-Z][a-z]*)', text)
    print("Từ viết hoa đầu câu:", words)

def bai_8():
    print("\n== Bài 8: Trích tên miền chính từ URL ==")
    urls = ["https://www.google.com", "http://facebook.com", "https://news.yahoo.com"]
    for url in urls:
        match = re.search(r'https?://(?:www\.)?([a-zA-Z0-9-]+)', url)
        if match:
            print(f"{url} ➜ {match.group(1)}")

def bai_9():
    print("\n== Bài 9: Tìm từ khóa bắt đầu bằng # ==")
    text = "Tôi yêu #Python và #MachineLearning, bạn có thích #AI không?"
    hashtags = re.findall(r'#\w+', text)
    print("Hashtag:", hashtags)

def bai_10():
    print("\n== Bài 10: Kiểm tra số thực dương ==")
    nums = ["3.14", "0.5", "10.0", ".", "3.", "abc", "-1.2"]
    for num in nums:
        if re.fullmatch(r'(0|[1-9]\d*)\.\d+', num):
            print(f"{num} ➜ Hợp lệ")
        else:
            print(f"{num} ➜ Không hợp lệ")

def bai_11():
    print("\n== Bài 11: Tìm tất cả email trong chuỗi ==")
    text = "Liên hệ qua email: support@example.com, admin@domain.org hoặc hello.world123@gmail.com."
    emails = re.findall(r'[a-zA-Z0-9._]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', text)
    print("Email tìm được:", emails)

def bai_12():
    print("\n== Bài 12: Tìm số nguyên hoặc thập phân dương/âm ==")
    text = "Nhiệt độ hôm nay là -10.5 độ, hôm qua là 25 và ngày mai có thể là -3."
    numbers = re.findall(r'-?\d+(\d+)?', text)
    print("Số tìm được:", numbers)

def bai_13():
    print("\n== Bài 13: Tìm từ dài hơn 6 ký tự ==")
    text = "Programming in Python is sometimes enjoyable and sometimes frustrating."
    words = re.findall(r'\b\w{7,}\b', text)
    print("Từ dài hơn 6 ký tự:", words)

def bai_14():
    print("\n== Bài 14: Kiểm tra mã bưu điện Việt Nam (5 chữ số) ==")
    postal_codes = ["70000", "123456", "ABCDE", "00000", "7500"]
    pattern = r'\d{5}'  # Mã hợp lệ: đúng 5 chữ số

    for code in postal_codes:
        if re.fullmatch(pattern, code):
            print(f"{code} ➜ Hợp lệ")
        else:
            print(f"{code} ➜ Không hợp lệ")
def bai_15():
    print("\n== Bài 15: Trích các từ viết hoa toàn bộ ==")
    text = "Chúng tôi làm việc với NASA, WHO và các tổ chức như UNICEF, nhưng không phải USAID."
    result = re.findall(r'\b[A-Z]{2,}\b', text)
    print("Từ viết hoa toàn bộ:", result)


# === MENU CHẠY ===
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

if __name__ == "__main__":
    user_input = input("Nhập tên hàm (vd: bai_1, bai_2) hoặc 'all': ").strip().lower()
    if user_input == "all":
        print("== Chạy tất cả các bài ==")
        for func in function_list.values():
            func()
    else:
        selected = [f.strip() for f in user_input.split(',')]
        for name in selected:
            if name in function_list:
                function_list[name]()
            else:
                print(f"Hàm '{name}' không tồn tại.")
