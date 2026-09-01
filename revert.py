import re
import os
import shutil

app_vue_path = '/data/data/com.termux/files/home/porject/silu/src/App.vue'
html_dir = '/data/data/com.termux/files/home/porject/silu/src/html_contents'

with open(app_vue_path, 'r', encoding='utf-8') as f:
    app_content = f.read()

# 1. Remove the imports
app_content = re.sub(r"import htmlContent_\d+ from '\./html_contents/marker_\d+\.html\?raw'\n", '', app_content)

# 2. Re-inline the htmlContent
if os.path.exists(html_dir):
    for filename in os.listdir(html_dir):
        if filename.startswith('marker_') and filename.endswith('.html'):
            m_id = filename.split('_')[1].split('.')[0]
            file_path = os.path.join(html_dir, filename)
            
            with open(file_path, 'r', encoding='utf-8') as f:
                html_val = f.read()
            
            # Decide whether to use backticks or single quotes. 
            # In JS, backticks are safer for multi-line.
            # We need to escape any backticks inside the HTML
            escaped_html = html_val.replace('`', '\\`')
            inline_str = f"`{escaped_html}`"
            
            # In App.vue, replace `htmlContent: htmlContent_X` with `htmlContent: \`...\``
            target = f"htmlContent: htmlContent_{m_id}"
            
            # It might have spaces around it or in front of it
            # Let's use re.sub for safety, but str.replace is exact
            app_content = app_content.replace(target, f"htmlContent: {inline_str}")

with open(app_vue_path, 'w', encoding='utf-8') as f:
    f.write(app_content)

# 3. Remove the directory
if os.path.exists(html_dir):
    shutil.rmtree(html_dir)

print("Reverted successfully.")
