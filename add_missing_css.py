import re

with open('src/App.vue', 'r') as f:
    content = f.read()

missing_css = """
.marker-modal-backdrop {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.4);
  z-index: 200;
  display: flex;
  justify-content: center;
  align-items: center;
}

.marker-modal {
  background: rgba(30, 24, 15, 0.85);
  border: 1px solid rgba(212, 175, 55, 0.6);
  border-radius: 0.12rem;
  padding: 0.2rem 0.24rem;
  width: 3.6rem;
  color: #fff;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.6);
  position: relative;
  backdrop-filter: blur(8px);
  animation: scaleIn 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
}

.html-modal {
  width: 70vw !important;
  max-width: 800px;
  height: 80vh;
  display: flex;
  flex-direction: column;
}

.modal-close {
  position: absolute;
  top: 0.15rem;
  right: 0.15rem;
  background: transparent;
  border: none;
  color: #fff;
  font-size: 0.24rem;
  cursor: pointer;
  z-index: 10;
}

.modal-divider {
  width: 100%;
  height: 1px;
  background: linear-gradient(90deg, transparent, rgba(212, 175, 55, 0.6), transparent);
  margin: 0.1rem 0;
}

.modal-html-content {
  flex: 1;
  overflow-y: auto;
  color: #fff;
}

@keyframes scaleIn {
  from { opacity: 0; transform: scale(0.9); }
  to { opacity: 1; transform: scale(1); }
}

.right-popup {
  position: absolute;
  top: 0.23rem;
  right: 0;
  width: 4.5rem;
  height: calc(100% - 0.46rem);
  z-index: 200;
  display: flex;
  flex-direction: column;
  padding: 0;
  box-sizing: border-box;
}

.right-popup-inner {
  position: relative;
  width: 100%;
  height: 100%;
}

.popup-bg {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: fill;
  z-index: 1;
}

.popup-close {
  position: absolute;
  top: 0.3rem;
  right: 0.3rem;
  width: 0.4rem;
  cursor: pointer;
  z-index: 3;
}

.popup-title {
  position: absolute;
  top: 0.45rem;
  left: 0;
  width: 100%;
  text-align: center;
  font-size: 0.28rem;
  color: #fff;
  z-index: 2;
  font-weight: bold;
}

.popup-content {
  position: absolute;
  top: 1.2rem;
  left: 0.4rem;
  right: 0.4rem;
  bottom: 0.4rem;
  z-index: 2;
  overflow-y: auto;
}

.slide-right-enter-active, .slide-right-leave-active {
  transition: transform 0.3s ease;
}
.slide-right-enter-from, .slide-right-leave-to {
  transform: translateX(100%);
}
"""

if '.marker-modal-backdrop' not in content:
    content = content.replace('</style>', missing_css + '\n</style>')

with open('src/App.vue', 'w') as f:
    f.write(content)

