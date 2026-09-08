import re

with open('src/App.vue', 'r') as f:
    content = f.read()

# Replace .marker-modal
old_modal = """  position: absolute;
  top: 50%;
  left: 0.5rem;
  height:calc(100% - .6rem);
  z-index: 9999;
  transform: translateY(-50%);
  animation: slideInLeft 0.4s cubic-bezier(0.25, 0.8, 0.25, 1);"""

new_modal = """  position: absolute;
  top: 50%;
  left: 50%;
  height:calc(100% - .6rem);
  z-index: 9999;
  transform: translate(-50%, -50%);
  animation: scaleInCenter 0.4s cubic-bezier(0.25, 0.8, 0.25, 1);"""

content = content.replace(old_modal, new_modal)

# Replace keyframes
old_keyframes = """@keyframes slideInLeft {
  from { opacity: 0; transform: translate(-2rem, -50%); }
  to { opacity: 1; transform: translate(0, -50%); }
}"""

new_keyframes = """@keyframes scaleInCenter {
  from { opacity: 0; transform: translate(-50%, -45%) scale(0.95); }
  to { opacity: 1; transform: translate(-50%, -50%) scale(1); }
}"""

content = content.replace(old_keyframes, new_keyframes)

with open('src/App.vue', 'w') as f:
    f.write(content)

