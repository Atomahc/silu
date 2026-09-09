import re

with open('index.html', 'r') as f:
    content = f.read()

old_script = """      function setRem() {
        const docEl = document.documentElement;
        const clientHeight = docEl.clientHeight;
        const rem = clientHeight / 9;
        docEl.style.fontSize = rem + 'px';
      }"""

new_script = """      function setRem() {
        const docEl = document.documentElement;
        // 使用屏幕宽度来计算rem，以保证所有元素与视口宽度(vw)及自适应画卷保持绝对的同比例缩放
        // 假设原设计稿比例接近16:9，用 clientWidth / 16 替代 clientHeight / 9
        const clientWidth = docEl.clientWidth;
        const rem = clientWidth / 16;
        docEl.style.fontSize = rem + 'px';
      }"""

if old_script in content:
    content = content.replace(old_script, new_script)
else:
    print("Script not found!")

with open('index.html', 'w') as f:
    f.write(content)

