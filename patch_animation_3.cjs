const fs = require('fs');
let code = fs.readFileSync('src/App.vue', 'utf8');

// Add :class="{ 'is-opening': isOpening, 'is-opened': isOpened }" to handles
code = code.replace(
  /<div class="scroll-handle handle-left"/,
  '<div class="scroll-handle handle-left" :class="{ \'is-opening\': isOpening, \'is-opened\': isOpened }"'
);
code = code.replace(
  /<div class="scroll-handle handle-right"/,
  '<div class="scroll-handle handle-right" :class="{ \'is-opening\': isOpening, \'is-opened\': isOpened }"'
);

const cssToAdd = `
.handle-left.is-opening {
  animation: handleLeftExpand 3.6s cubic-bezier(0.25, 0.1, 0.25, 1) forwards;
}

.handle-right.is-opening {
  animation: handleRightExpand 3.6s cubic-bezier(0.25, 0.1, 0.25, 1) forwards;
}

@keyframes handleLeftExpand {
  0% {
    left: 50%;
    transform: translateX(-50%);
  }
  100% {
    left: 0.2rem;
    transform: translateX(-30%);
  }
}

@keyframes handleRightExpand {
  0% {
    right: 50%;
    transform: translateX(50%);
  }
  100% {
    right: 0.2rem;
    transform: translateX(30%);
  }
}
`;

code = code.replace(/@keyframes scrollPhysicalExpand/, cssToAdd + '\n@keyframes scrollPhysicalExpand');

fs.writeFileSync('src/App.vue', code);
