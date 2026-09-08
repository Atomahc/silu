import re

with open('src/App.vue', 'r') as f:
    content = f.read()

# Add align-items: center to scroll-content to see if it fixes it
if 'align-items: center;' not in content.split('.scroll-content {')[1].split('}')[0]:
    content = content.replace('.scroll-content {\n  width: 100%;\n  height: auto;\n  display: flex;\n  flex-direction: column;', '.scroll-content {\n  width: 100%;\n  height: auto;\n  display: flex;\n  flex-direction: column;\n  align-items: center;')

with open('src/App.vue', 'w') as f:
    f.write(content)

