const fs = require('fs');

let content = fs.readFileSync('src/App.vue', 'utf8');

content = content.replace(/\.scroll-container \{[\s\S]*?\}/, `.scroll-container {
  width: 100vw;
  height: 100vh;
  background-color: transparent;
  overflow-x: auto;
  overflow-y: hidden;
  position: relative;
  transition: background-color 0.5s ease;
}`);

content = content.replace(/\.ratio-box \{[\s\S]*?\}/, `.ratio-box {
  height: 100vh;
  width: max-content;
  position: relative;
}`);

content = content.replace(/\.scroll-wrapper \{[\s\S]*?\}/, `.scroll-wrapper {
  display: flex;
  justify-content: center;
  align-items: center;
  width: max-content;
  height: 100%;
  position: relative;
  padding:0.3rem 0.45rem;
  box-sizing: border-box;
}`);

content = content.replace(/\.panoramic-container \{[\s\S]*?\}/, `.panoramic-container {
  flex: 1;
  position: relative;
  overflow: hidden;
  width: max-content;
}`);

content = content.replace(/\.panoramic-bg \{[\s\S]*?\}/, `.panoramic-bg {
  height: 100%;
  width: auto;
  object-position: center;
  display: block;
}`);

content = content.replace(/@keyframes scrollPhysicalExpand \{[\s\S]*?\}/, `@keyframes scrollPhysicalExpand {
  0% {
    width: 0.1vw;
    box-shadow: inset 0 0 0px rgba(100, 60, 20, 0);
  }
  100% {
    width: 100%;
    box-shadow: inset 0 0 40px rgba(100, 60, 20, 0.15);
  }
}`);

fs.writeFileSync('src/App.vue', content);
console.log("Patched App.vue");
