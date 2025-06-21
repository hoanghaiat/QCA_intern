import re

number_text = "Nhiệt độ hôm nay là -10.5 độ, hôm qua là 25 và ngày mai có thể là -3."
pattern = r'[-+]?\d+(\.\d+)?'

numbers = re.findall(pattern, number_text)

matches = re.finditer(r'[-+]?\d+(?:\.\d+)?', number_text)
results = [match.group() for match in matches]

print("Các số tìm được:", results)


