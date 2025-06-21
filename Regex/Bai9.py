import re

hashtag_text = "Tôi yêu #Python và #MachineLearning, bạn có thích #AI không?"
pattern = r'#\w+'

hashtags = re.findall(pattern, hashtag_text)
print("Các hashtag tìm được:", hashtags)

