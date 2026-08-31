const fs = require('fs');
let code = fs.readFileSync('src/App.vue', 'utf8');

// Insert imports
const imports = `
import Panel0 from './components/Panel0.vue'
import Panel1 from './components/Panel1.vue'
import Panel2 from './components/Panel2.vue'
import Panel3 from './components/Panel3.vue'
import Panel4 from './components/Panel4.vue'
`;

code = code.replace(
  /import { ref, onMounted, onUnmounted } from 'vue'/,
  `import { ref, onMounted, onUnmounted } from 'vue'\n${imports}`
);

// Add panels array
code = code.replace(
  /const footerNavs = ref\(\[/,
  `const panels = [Panel0, Panel1, Panel2, Panel3, Panel4]\nconst footerNavs = ref([`
);

// Replace popup-content placeholder with <component>
code = code.replace(
  /<div class="popup-content">\s*<!-- 内容区域预留位置 -->\s*<\/div>/,
  `<div class="popup-content">
              <component :is="panels[currentNavIndex]" v-if="currentNavIndex !== '' && currentNavIndex !== null" />
            </div>`
);

fs.writeFileSync('src/App.vue', code);
