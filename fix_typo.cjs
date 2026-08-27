const fs = require('fs');
let code = fs.readFileSync('src/App.vue', 'utf8');

code = code.replace(
`.ratio-box.is-opening .panoramic-container,

.scroll-footer.is-opening {`,
`.ratio-box.is-opening .panoramic-container {
  animation: scrollContentFadeIn 3.6s ease forwards;
}

.scroll-footer.is-opening {`
);

fs.writeFileSync('src/App.vue', code);
