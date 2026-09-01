import re
import os

app_vue_path = 'src/App.vue'
html_dir = 'src/html'

if not os.path.exists(html_dir):
    os.makedirs(html_dir)

with open(app_vue_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Pattern to find the marker objects with htmlContent
# It looks for something like: { id: 1, ... htmlContent: `...` }
# We need to be careful because the content inside `...` can have newlines.
pattern = re.compile(r"(\{.*?id:\s*(\d+).*?htmlContent:\s*)`([^`]*)`(\s*\})", re.DOTALL)

imports = []
def replacer(match):
    prefix = match.group(1)
    marker_id = match.group(2)
    html_content = match.group(3)
    suffix = match.group(4)
    
    file_name = f"marker_{marker_id}.html"
    file_path = os.path.join(html_dir, file_name)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
        
    import_statement = f"import marker{marker_id}Html from './html/{file_name}?raw'"
    imports.append(import_statement)
    
    return f"{prefix}marker{marker_id}Html{suffix}"

new_content = pattern.sub(replacer, content)

# Now inject the imports after the last import in the script block
# Find the last import
import_pattern = re.compile(r"(import .*?\n)(?!import)")
last_import_match = list(import_pattern.finditer(new_content))[-1]

insert_pos = last_import_match.end()
imports_str = "\n" + "\n".join(imports) + "\n"

new_content = new_content[:insert_pos] + imports_str + new_content[insert_pos:]

with open(app_vue_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f"Extracted {len(imports)} html contents.")
