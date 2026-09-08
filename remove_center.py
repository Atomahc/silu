import re

with open('src/App.vue', 'r') as f:
    content = f.read()

content = content.replace("  flex-direction: column;\n  align-items: center;\n  background: #fbf6ec;", "  flex-direction: column;\n  background: #fbf6ec;")

with open('src/App.vue', 'w') as f:
    f.write(content)

