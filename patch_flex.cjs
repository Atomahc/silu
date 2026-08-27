const fs = require('fs');
let code = fs.readFileSync('src/App.vue', 'utf8');

code = code.replace(
`      <!-- 卷轴轴柄 - 左边 (绝对定位在 scroll-container 的边缘) -->
      <div class="scroll-handle handle-left" @mouseenter="startScroll('left')" @mouseleave="stopScroll">
        <img src="/Group 2@2x.png" alt="">
      </div>

      <!-- 卷轴轴柄 - 右边 (绝对定位在 scroll-container 的边缘) -->
      <div class="scroll-handle handle-right" @mouseenter="startScroll('right')" @mouseleave="stopScroll">
        <img src="/Group 3@2x.png" alt="">
      </div>

      <!-- Ratio Box (100% width) -->
      <div class="ratio-box" :class="{ 'is-opening': isOpening, 'is-opened': isOpened }">
        <div class="scroll-wrapper">`,
`      <!-- Ratio Box (100% width) -->
      <div class="ratio-box" :class="{ 'is-opening': isOpening, 'is-opened': isOpened }">
        <div class="scroll-wrapper">
          <!-- 卷轴轴柄 - 左边 (绝对定位在 scroll-container 的边缘) -->
          <div class="scroll-handle handle-left" @mouseenter="startScroll('left')" @mouseleave="stopScroll">
            <img src="/Group 2@2x.png" alt="">
          </div>`
);

code = code.replace(
`          </div>
        </div>
      </div>
      
      <!-- 底部 Footer (固定在 scroll-container) -->`,
`          </div>
          <!-- 卷轴轴柄 - 右边 (绝对定位在 scroll-container 的边缘) -->
          <div class="scroll-handle handle-right" @mouseenter="startScroll('right')" @mouseleave="stopScroll">
            <img src="/Group 3@2x.png" alt="">
          </div>
        </div>
      </div>
      
      <!-- 底部 Footer (固定在 scroll-container) -->`
);

code = code.replace(
`.handle-left {
  height: 100%;
  position: absolute;
  left: .2rem;
  top: 0;
  z-index: 99999;
  pointer-events: auto;
  cursor: pointer;
  transform: translateX(-30%);
  transition: transform 0.3s;
}`,
`.handle-left {
  height: 100%;
  position: relative;
  z-index: 99999;
  pointer-events: auto;
  cursor: pointer;
  transform: translateX(10%);
  transition: transform 0.3s;
}`
);

code = code.replace(
`.handle-right {
  height: 100%;
  position: absolute;
  right: .2rem;
  top: 0;
  z-index: 99999;
  pointer-events: auto;
  cursor: pointer;
  transform: translateX(30%);
  transition: transform 0.3s;
}`,
`.handle-right {
  height: 100%;
  position: relative;
  z-index: 99999;
  pointer-events: auto;
  cursor: pointer;
  transform: translateX(-10%);
  transition: transform 0.3s;
}`
);

fs.writeFileSync('src/App.vue', code);
