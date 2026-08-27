const fs = require('fs');
let code = fs.readFileSync('src/App.vue', 'utf8');

code = code.replace(
`.handle-left {
  height: 100%;
  position: relative;
  z-index: 99999;
  pointer-events: auto;
  cursor: pointer;
  transform: translateX(10%);
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
  flex-shrink: 0;
}`
);

code = code.replace(
`.handle-right {
  height: 100%;
  position: relative;
  z-index: 99999;
  pointer-events: auto;
  cursor: pointer;
  transform: translateX(-10%);
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
  flex-shrink: 0;
}`
);

// We need to adjust width to not overflow if 100% is set
code = code.replace(
`@keyframes scrollPhysicalExpand {
  0% {
    width: 0.1vw;
    box-shadow: inset 0 0 0px rgba(100, 60, 20, 0);
  }
  100% {
    width: 100%;
    box-shadow: inset 0 0 40px rgba(100, 60, 20, 0.15);
  }
}`,
`@keyframes scrollPhysicalExpand {
  0% {
    width: 0.1vw;
    box-shadow: inset 0 0 0px rgba(100, 60, 20, 0);
    flex-grow: 0;
  }
  100% {
    width: 100%;
    box-shadow: inset 0 0 40px rgba(100, 60, 20, 0.15);
    flex-grow: 1;
  }
}`
);

fs.writeFileSync('src/App.vue', code);
