import re

def bai_1():
    # 1. Viết regex để kiểm tra xem một chuỗi có phải là email hợp lệ không.
    # Email hợp lệ có dạng: chữ cái/số + @ + tên miền + .com
    emails = ["test123@gmail.com", "abc@xyz", "user@domain.com", "invalid@.com"]

    print("\nRun bai_1")


def bai_2():
    # 2. Tìm tất cả số điện thoại (gồm đúng 10 số, chia bởi dấu -)
    phone_text = "Liên hệ 091-234-5678 hoặc 123-4567-890 để được tư vấn. Gọi 987-654-3210 ngay!"
    
    print("\nRun bai_2")


def bai_3():
    # 3. Cho chuỗi đầu vào, kiểm tra xem trong chuỗi có ít nhất một chữ số không.
    digit_text = "Tôi có 2 con mèo và 1 con chó."
    
    print("\nRun bai_3")


def bai_4():
   # 4. Cho một chuỗi, loại bỏ toàn bộ ký tự không phải chữ cái.
    dirty_text = "Hello! This is test123 #2025."     
    
    print("\nRun bai_4")


def bai_5():
    # 5. Kiểm tra chuỗi mật khẩu có phải là mật khẩu mạnh không.
    # Tiêu chí: Tối thiểu 8 ký tự, ít nhất 1 chữ hoa, 1 chữ thường, 1 số
    passwords = ["Abc12345", "abcdef", "ABC123456", "abcD1"]    
    
    print("\nRun bai_5")


def bai_6():
    # 6. Kiểm tra chuỗi có phải là ngày hợp lệ theo định dạng dd/mm/yyyy không
    # (không xét tính hợp lệ theo lịch thực tế)
    dates = ["18/06/2025", "31/13/2022", "00/12/2020", "5/6/2020"]    
    
    print("\nRun bai_6")


def bai_7():
    # 7. Tìm tất cả các từ viết hoa đứng đầu câu trong đoạn văn.
    capital_text = "Today is a good day. My name is Hoa. How are you?"    
    
    print("\nRun bai_7")


def bai_8():
    # 8. Từ danh sách URL, trích ra phần tên miền chính (ví dụ: google, facebook).
    urls = ["https://www.google.com", "http://facebook.com", "https://news.yahoo.com"]    
    
    print("\nRun bai_8")


def bai_9():
    # 9. Tìm tất cả từ khóa bắt đầu bằng # trong đoạn văn bản.
    hashtag_text = "Tôi yêu #Python và #MachineLearning, bạn có thích #AI không?"    
    
    print("\nRun bai_9")


def bai_10():
    # 10. Kiểm tra xem chuỗi có phải là số thực dương (thập phân) không.
    # Hợp lệ: "3.14", "0.5", "10.0"
    # Không hợp lệ: ".", "3.", "abc", "-1.2"
    nums = ["3.14", "0.5", "10.0", ".", "3.", "abc", "-1.2"]    
    
    print("\nRun bai_10")


def bai_11():
    # 11. Tìm và in ra tất cả các email trong chuỗi văn bản.
    email_text = "Liên hệ qua email: support@example.com, admin@domain.org hoặc hello.world123@gmail.com."    
    
    print("\nRun bai_11")


def bai_12():
    # 12. Tìm các số nguyên hoặc thập phân dương/âm trong chuỗi.
    number_text = "Nhiệt độ hôm nay là -10.5 độ, hôm qua là 25 và ngày mai có thể là -3."    
    
    print("\nRun bai_12")


def bai_13():
    # 13. Tìm tất cả các từ dài hơn 6 ký tự trong câu.
    long_word_text = "Programming in Python is sometimes enjoyable and sometimes frustrating."    
    
    print("\nRun bai_13")
 

def bai_14():
    # 14. Mã bư`u điện VN gồm 5 chữ số. Kiểm tra chuỗi có phải mã hợp lệ không.
    postal_codes = ["70000", "123456", "ABCDE", "00000", "7500"]
    
    print("\nRun bai_14")


def bai_15():
    # 15. Trích xuất tất cả từ viết hoa toàn bộ (ví dụ như tên viết tắt, hoặc từ nhấn mạnh).
    uppercase_text = "Chúng tôi làm việc với NASA, WHO và các tổ chức như UNICEF, nhưng không phải USAID."    
    
    print("\nRun bai_15")



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
