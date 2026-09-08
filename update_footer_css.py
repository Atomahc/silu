import re

with open('src/App.vue', 'r') as f:
    content = f.read()

old_css = """
.scroll-footer {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  position: absolute;
  bottom: 0.23rem;
  left: 0;
  z-index: 100;
  box-sizing: border-box;
}

.flexdvv {
  display: flex;
  gap: 0.2rem;
}

.footer-nav-cell {
  cursor: pointer;
  color: #c0b090;
  padding: 0.05rem 0.15rem;
  border: 1px solid transparent;
  transition: all 0.3s;
}

.footer-nav-cell.active {
  color: #f0e0c0;
  border-color: #d4af37;
  border-radius: 0.2rem;
  background: rgba(212, 175, 55, 0.15);
}
"""

new_css = """
.scroll-footer {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  position: absolute;
  bottom: 0.23rem;
  left: 0;
  z-index: 100;
  box-sizing: border-box;
}

.flexdvv {
  display: flex;
  gap: 0.15rem;
  background: rgba(0, 0, 0, 0.65);
  padding: 0.08rem 0.2rem;
  border-radius: 0.3rem;
  backdrop-filter: blur(8px);
  border: 1px solid rgba(212, 175, 55, 0.3);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.5);
}

.footer-nav-cell {
  cursor: pointer;
  color: #c0b090;
  padding: 0.06rem 0.16rem;
  border: 1px solid transparent;
  transition: all 0.3s;
  font-size: 0.18rem;
  font-weight: 500;
  letter-spacing: 0.02rem;
}

.footer-nav-cell.active {
  color: #fff;
  border-color: rgba(212, 175, 55, 0.8);
  border-radius: 0.2rem;
  background: rgba(212, 175, 55, 0.25);
  text-shadow: 0 0 8px rgba(212, 175, 55, 0.6);
}
"""

content = content.replace(old_css, new_css)

with open('src/App.vue', 'w') as f:
    f.write(content)

