const fs = require('fs');

let content = fs.readFileSync('src/App.vue', 'utf8');

// 1. Add ref to scroll-container
content = content.replace('<div class="scroll-container" :class="{ \'is-night\': isNight }">',
  '<div class="scroll-container" :class="{ \'is-night\': isNight }" ref="scrollContainer">');

// 2. Move handles and add events
const leftHandleHtml = `
    <!-- 卷轴轴柄 - 左边 (固定在屏幕左侧，悬浮滚动) -->
    <div class="scroll-handle handle-left" @mouseenter="startScroll('left')" @mouseleave="stopScroll">
      <img src="/Group 2@2x.png" alt="">
    </div>
`;
const rightHandleHtml = `
    <!-- 卷轴轴柄 - 右边 (固定在屏幕右侧，悬浮滚动) -->
    <div class="scroll-handle handle-right" @mouseenter="startScroll('right')" @mouseleave="stopScroll">
      <img src="/Group 3@2x.png" alt="">
    </div>
`;

// Remove original left handle
content = content.replace(/<!-- 卷轴轴柄 - 左边（绝对定位在画卷左边缘外侧\/边缘） -->\s*<div class="scroll-handle handle-left">\s*<img src="\/Group 2@2x\.png" alt="">\s*<\/div>/, '');

// Remove original right handle
content = content.replace(/<!-- 卷轴轴柄 - 右边（绝对定位在画卷右边缘外侧\/边缘） -->\s*<div class="scroll-handle handle-right">\s*<img src="\/Group 3@2x\.png" alt="">\s*<\/div>/, '');

// Insert handles as direct children of scroll-container, before ratio-box
content = content.replace('<!-- 32:9 比例固定宽高比容器 (自动居中适应) -->', 
  leftHandleHtml + '\n    ' + rightHandleHtml + '\n    <!-- 32:9 比例固定宽高比容器 (自动居中适应) -->');


// 3. Add script variables and functions
const scriptInsert = `
const scrollContainer = ref(null)
let scrollAnimationFrame = null

const startScroll = (direction) => {
  const speed = 15; // 滚动速度
  const scrollStep = () => {
    if (scrollContainer.value) {
      if (direction === 'left') {
        scrollContainer.value.scrollLeft -= speed;
      } else {
        scrollContainer.value.scrollLeft += speed;
      }
    }
    scrollAnimationFrame = requestAnimationFrame(scrollStep);
  }
  scrollStep();
}

const stopScroll = () => {
  if (scrollAnimationFrame) {
    cancelAnimationFrame(scrollAnimationFrame);
    scrollAnimationFrame = null;
  }
}
`;

content = content.replace(/const isNight = ref\(false\)/, scriptInsert + '\nconst isNight = ref(false)');

// 4. Update CSS
content = content.replace(/\.handle-left \{[\s\S]*?\}/, `.handle-left {
  height: 100vh;
  position: fixed;
  left: 0;
  top: 0;
  z-index: 50;
  pointer-events: auto;
  cursor: pointer;
  transform: translateX(-30%);
  transition: transform 0.3s;
}
.handle-left:hover {
  transform: translateX(-20%);
}`);

content = content.replace(/\.handle-right \{[\s\S]*?\}/, `.handle-right {
  height: 100vh;
  position: fixed;
  right: 0;
  top: 0;
  z-index: 50;
  pointer-events: auto;
  cursor: pointer;
  transform: translateX(30%);
  transition: transform 0.3s;
}
.handle-right:hover {
  transform: translateX(20%);
}`);


fs.writeFileSync('src/App.vue', content);
console.log("Hover patch applied.");
