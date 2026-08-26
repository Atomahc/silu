const fs = require('fs');
let content = fs.readFileSync('src/App.vue', 'utf8');

// We want to replace everything starting from "<!-- 底部卷轴 五大板块导航栏 -->" to "</template>"
const idx = content.indexOf('<!-- 底部卷轴 五大板块导航栏 -->');
if (idx > -1) {
  const start = content.substring(0, idx);
  const endHtml = `<!-- 底部卷轴 五大板块导航栏 -->
        </div>
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
</template>
`;
  
  // Find </template>
  const afterTemplate = content.substring(content.indexOf('</template>') + '</template>'.length);
  fs.writeFileSync('src/App.vue', start + endHtml + afterTemplate);
  console.log("Replaced template end");
} else {
  console.log("Could not find anchor");
}

