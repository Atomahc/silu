import re
with open('/data/data/com.termux/files/home/porject/silu/dist/index-CXTfdaYe.js', 'r', encoding='utf-8') as f:
    js_content = f.read()

# Let's find the array containing "数字大建", "数字政务", "数字经济", "数字社会", "数字文化"
match = re.search(r'\[([^\]]*?"数字政务"[^\]]*?)\]', js_content)
if match:
    print(match.group(0))
