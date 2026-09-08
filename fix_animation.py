import re

with open('src/App.vue', 'r') as f:
    content = f.read()

content = content.replace(""".panoramic-container {
  height: auto;
  position: relative;
  overflow: hidden;
  width: 200%;
}""", """.panoramic-container {
  height: auto;
  position: relative;
  overflow: hidden;
  width: 200vw;
}""")

with open('src/App.vue', 'w') as f:
    f.write(content)

