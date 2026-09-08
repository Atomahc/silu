import re

with open('src/App.vue', 'r') as f:
    content = f.read()

# 1. Remove the currently wrong added CSS blocks
bad_blocks = [
    # marker-modal-backdrop I added
    r'\.marker-modal-backdrop \{.*?align-items: center;\n\}',
    r'\.marker-modal \{.*?\n\}',
    r'\.html-modal \{.*?\n\}',
    r'\.modal-close \{.*?\n\}',
    r'\.modal-divider \{.*?\n\}',
    r'\.modal-html-content \{.*?\n\}',
    r'@keyframes scaleIn \{.*?\n\}',
    # right-popup I added
    r'\.right-popup \{.*?\n\}',
    r'\.right-popup-inner \{.*?\n\}',
    r'\.popup-bg \{.*?\n\}',
    r'\.popup-close \{.*?\n\}',
    r'\.popup-title \{.*?\n\}',
    r'\.popup-content \{.*?\n\}',
    r'\.slide-right-enter-active, \.slide-right-leave-active \{.*?\n\}',
    r'\.slide-right-enter-from, \.slide-right-leave-to \{.*?\n\}',
    # scroll-footer I added
    r'\.scroll-footer \{.*?backdrop-filter: blur\(4px\);\n\}',
    r'\.flexdvv \{.*?\n\}',
    r'\.footer-nav-cell \{.*?\n\}'
]

for block in bad_blocks:
    content = re.sub(block, '', content, flags=re.DOTALL)

# 2. Append the exact original CSS
original_css = """
/* 详情弹窗 Modal */
.marker-modal-backdrop {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.1);
  z-index: 99999999;
}

.marker-modal {
  width: 8rem;
  background: rgba(255, 252, 247, 0.75);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border: 0.02rem solid rgba(212, 175, 55, 0.6);
  border-radius: 0.16rem;
  padding: 0.24rem;
  box-shadow: 0 0.12rem 0.32rem rgba(0, 0, 0, 0.15);
  position: absolute;
  top: 50%;
  left: 0.5rem;
  height:calc(100% - .6rem);
  z-index: 9999;
  transform: translateY(-50%);
  animation: slideInLeft 0.4s cubic-bezier(0.25, 0.8, 0.25, 1);
}

@keyframes slideInLeft {
  from { opacity: 0; transform: translate(-2rem, -50%); }
  to { opacity: 1; transform: translate(0, -50%); }
}

.modal-close {
  position: absolute;
  top: 0.14rem;
  right: 0.16rem;
  background: none;
  border: none;
  font-size: 0.2rem;
  color: #8c6a38;
  cursor: pointer;
}

.marker-modal h3 {
  font-size: 0.22rem;
  color: #4a2f07;
  margin-bottom: 0.1rem;
  font-family: "STKaiti", "KaiTi", serif;
}

.modal-divider {
  height: 0.02rem;
  background: linear-gradient(90deg, #e65c00 0%, #ff9d1e 50%, transparent 100%);
  margin-bottom: 0.14rem;
}

.marker-modal p {
  font-size: 0.14rem;
  line-height: 1.6;
  color: #554433;
  margin-bottom: 0.2rem;
}

.modal-html-content {
  overflow-y: auto;
  max-height: calc(100% - 0.8rem);
  font-size: 0.14rem;
  color: #333;
  line-height: 1.6;
}

.modal-html-content p {
  margin-bottom: 0.1rem;
}

.modal-html-content img {
  max-width: 100%;
  height: auto;
}

.modal-stats {
  display: flex;
  gap: 0.16rem;
  background: rgba(230, 92, 0, 0.06);
  border-radius: 0.1rem;
  padding: 0.12rem;
}

.stat-item {
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.stat-value {
  font-size: 0.18rem;
  font-weight: bold;
  color: #e65c00;
}

.stat-label {
  font-size: 0.12rem;
  color: #776655;
  margin-top: 0.04rem;
}

/* 底部 Golden 卷轴五大板块栏 */
.scroll-footer {
  height: 0.6rem;
  display: flex;
  align-items: center;
  justify-content: space-around;
  padding: 0 0.2rem;
  box-sizing: border-box;
  z-index: 100;
  position: absolute;
  
  background: radial-gradient( 277.74% 169.73% at 190.57% -18.33%, rgba(0,0,0,0.8) 0%, rgba(102,102,102,0) 100%), rgba(0,0,0,0.12);
  bottom: .23rem;
  left: 50%;
  transform: translateX(-50%);
  width: 100%;
  overflow: hidden;
  white-space: nowrap;
}

.footer-nav-cell {
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  width: 6rem;
  position: relative;
  transition: all 0.3s ease;
}

.footer-nav-cell:last-child {
  border-right: none;
}

.footer-nav-cell.active,
.footer-nav-cell:hover {
  background: linear-gradient(180deg, #c49438 0%, #855f19 100%);
}
.flexdvv{
  display: flex;
  width: 10rem;
  height: 100%;

}
.nav-text {
  font-family: "STKaiti", "KaiTi", serif;
  font-size: 0.2rem;
  font-weight: bold;
  color: #f7eedb;
  letter-spacing: 0.04rem;
  text-shadow: 0 0.02rem 0.04rem rgba(0, 0, 0, 0.6);
}

.right-popup {
  position: absolute;
  top: 0.8rem;
  right: 0.6rem;
  bottom: 0.8rem;
  width: 9rem; /* 大约占比 */
  z-index: 200000;
  display: flex;
  justify-content: flex-end;
  pointer-events: none;
}

.right-popup-inner {
  position: relative;
  width: 100%;
  height: 100%;
  pointer-events: auto;
}

.popup-bg {
  width: 100%;
  height: 100%;
  position: absolute;
  top: 0;
  left: 0;
  z-index: 1;
  opacity: .8;
}

.popup-close {
  position: absolute;
  top: -0rem;
  right: -0.1rem;
  width: 0.3rem;
  height: 0.3rem;
  z-index: 10;
  cursor: pointer;
  transition: transform 0.3s;
}

.popup-close:hover {
  transform: scale(1.1) rotate(90deg);
}

.popup-title {
  position: absolute;
  top: 0.05rem;
  left: 50%;
  transform: translateX(-50%);
  z-index: 5;
  font-size: 0.22rem;
  font-weight: bold;
  color: #FFF5CB;
  letter-spacing: 0.06rem;
  font-family: "STKaiti", "KaiTi", serif;
}

.popup-content {
  position: absolute;
  top: 0.6rem;
  left: 0.3rem;
  right: 0.3rem;
  bottom: 0.3rem;
  z-index: 2;
  /* background: rgba(255, 0, 0, 0.1); 占位测试可取消注释 */
}

/* 弹出框过渡动画 */
.slide-right-enter-active,
.slide-right-leave-active {
  transition: all 0.4s cubic-bezier(0.25, 0.8, 0.25, 1);
}
.slide-right-enter-from,
.slide-right-leave-to {
  opacity: 0;
  transform: translateX(1rem);
}
"""

timeline_css = """
<style>
.custom-timeline {
  display: flex;
  flex-direction: column;
  padding: 10px 0;
}
.custom-timeline .timeline-item {
  display: flex;
  align-items: stretch;
  margin-bottom: 0px;
}
.custom-timeline .timeline-left {
  width: 140px;
  flex-shrink: 0;
  display: flex;
  align-items: flex-start;
  justify-content: flex-end;
  padding-top: 2px;
}
.custom-timeline .timeline-left img {
  width: 100%;
  border-radius: 6px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.15);
}
.custom-timeline .timeline-divider {
  width: 36px;
  display: flex;
  flex-direction: column;
  align-items: center;
  position: relative;
  flex-shrink: 0;
}
.custom-timeline .timeline-divider .dot {
  width: 12px;
  height: 12px;
  border-radius: 50%;
  background-color: #fff;
  border: 3px solid #e65c00;
  margin-top: 6px;
  z-index: 2;
  box-shadow: 0 0 0 2px rgba(230, 92, 0, 0.2);
}
.custom-timeline .timeline-divider .line {
  position: absolute;
  top: 22px;
  bottom: -6px;
  width: 2px;
  background-color: #e65c00;
  opacity: 0.4;
  z-index: 1;
}
.custom-timeline .timeline-item:last-child .timeline-divider .line {
  display: none;
}
.custom-timeline .timeline-right {
  flex: 1;
  padding-bottom: 25px;
}
.custom-timeline .timeline-title {
  font-size: 18px;
  font-weight: bold;
  color: #a00;
  margin-bottom: 6px;
  font-family: "STKaiti", "KaiTi", serif;
}
.custom-timeline .timeline-desc {
  font-size: 14px;
  color: #443322;
  line-height: 1.6;
}
.custom-timeline .timeline-desc strong {
  color: #a00;
}
</style>
"""

content = content.replace('</style>', original_css + '\n</style>' + timeline_css)

# Clean up any potential multiple empty lines
content = re.sub(r'\n{3,}', '\n\n', content)

with open('src/App.vue', 'w') as f:
    f.write(content)

