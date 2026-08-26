const fs = require('fs');
let content = fs.readFileSync('src/App.vue', 'utf8');

// The end of the template is messed up. Let's find </template> and fix the tags before it.
// We know we want the footer INSIDE the scroll-container, or as a sibling.
// Since scroll-container has height:100vh, we can put footer inside it.

// Let's replace everything from panoramic-container closing to </template>
// We'll use a regex to match the end part.

content = content.replace(/<\/div>\s*<!-- 底部卷轴 五大板块导航栏 -->\s*<\/div>\s*<\/div>\s*<\/div>\s*<footer[\s\S]*?<\/footer>\s*<\/div>\s*<\/template>/, 
`          </div>
        </div>
      </div>
      <footer class="scroll-footer" :class="{ 'is-opening': isOpening, 'is-opened': isOpened }">
        <div 
          v-for="(nav, index) in footerNavs" 
          :key="index" 
          class="footer-nav-cell"
          :class="{ active: currentNavIndex === index }"
          @click="currentNavIndex = index"
        >
          <span class="nav-text">{{ nav }}</span>
        </div>
      </footer>
  </div>
</template>`);

fs.writeFileSync('src/App.vue', content);
console.log("Fixed tags");
