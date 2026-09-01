import os
import re

html_dir = 'src/html'
img_dir = 'src/img'
valid_images = set(os.listdir(img_dir))

for file_name in os.listdir(html_dir):
    if not file_name.endswith('.html'):
        continue
        
    file_path = os.path.join(html_dir, file_name)
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Find all src attributes in img tags
    # It might be src="https://.../filename.png?auth..."
    # or src="./filename.png..."
    
    def replacer(match):
        full_url = match.group(1)
        # Extract filename (before ? or ")
        # e.g., https://.../filename.png?auth -> filename.png
        base = full_url.split('?')[0]
        filename = base.split('/')[-1]
        
        if filename in valid_images:
            return f'src="/src/img/{filename}"'
        elif filename == 'QXTDbeJF_LnbA.png': # already handled ones might just have /src/img/
            pass
        return match.group(0) # don't change if not found

    # Regex to match src="..."
    new_content = re.sub(r'src="([^"]+)"', replacer, content)
    
    # Also handle _src="..." just in case
    def _src_replacer(match):
        full_url = match.group(1)
        base = full_url.split('?')[0]
        filename = base.split('/')[-1]
        
        if filename in valid_images:
            return f'_src="/src/img/{filename}"'
        return match.group(0)
        
    new_content = re.sub(r'_src="([^"]+)"', _src_replacer, new_content)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

print("Updated HTML files.")
