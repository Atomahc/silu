import os
import re

html_dir = 'src/html'

for file_name in os.listdir(html_dir):
    if not file_name.endswith('.html'):
        continue
        
    file_path = os.path.join(html_dir, file_name)
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    def replacer(match):
        size = match.group(1)
        # Convert px to rem by dividing by 100
        rem_size = float(size) / 100
        return f"font-size: {rem_size}rem"

    new_content = re.sub(r'font-size:\s*(\d+)\.?\d*px', replacer, content)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

print("Updated HTML font sizes.")
