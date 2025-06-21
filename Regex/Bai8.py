import re

urls = ["https://www.google.com", "http://facebook.com", "https://news.yahoo.com"]

pattern = r'https?://(?:www\.|news\.)?([a-zA-Z0-9-]+)\.'

for url in urls:
    match = re.search(pattern, url)
    if match:
        print(f"{url} ➜ {match.group(1)}")
        

