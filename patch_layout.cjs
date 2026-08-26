const fs = require('fs');

let content = fs.readFileSync('src/App.vue', 'utf8');

// 1. Move <header> and <footer>
// Extract header
const headerMatch = content.match(/<header class="header">[\s\S]*?<\/header>/);
const headerHtml = headerMatch ? headerMatch[0] : '';
content = content.replace(headerHtml, '');

// Extract footer
const footerMatch = content.match(/<footer class="scroll-footer">[\s\S]*?<\/footer>/);
const footerHtml = footerMatch ? footerMatch[0] : '';
content = content.replace(footerHtml, '');

// Add bindings to header and footer
const newHeaderHtml = headerHtml.replace('<header class="header">', '<header class="header" :class="{ \'is-opening\': isOpening, \'is-opened\': isOpened }">');
const newFooterHtml = footerHtml.replace('<footer class="scroll-footer">', '<footer class="scroll-footer" :class="{ \'is-opening\': isOpening, \'is-opened\': isOpened }">');

// Insert header and footer into scroll-container
content = content.replace('<!-- 32:9 比例固定宽高比容器 (自动居中适应) -->', 
  newHeaderHtml + '\n    <!-- 32:9 比例固定宽高比容器 (自动居中适应) -->');

content = content.replace('</template>', 
  '  ' + newFooterHtml + '\n  </div>\n</template>'); // Insert footer before the closing tag of scroll-container. Wait, the template ends with:
//     </div>
//   </div>
// </template>
// Let's replace more accurately
content = content.replace(/<\/div>\n  <\/div>\n<\/template>/, 
  '  ' + newFooterHtml + '\n    </div>\n  </div>\n</template>');


// 2. CSS Updates
content = content.replace(/\.header \{[\s\S]*?\}/, `.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0rem 0.5rem 0 0.5rem;
  z-index: 100;
  width: 100vw;
  position: fixed;
  left: 0;
  top: 0;
  box-sizing: border-box;
}`);

content = content.replace(/\.scroll-footer \{[\s\S]*?\}/, `.scroll-footer {
  height: 0.68rem;
  background: linear-gradient(180deg, #3d2b15 0%, #1e1308 100%);
  border-top: 0.02rem solid #d49c25;
  display: flex;
  align-items: center;
  justify-content: space-around;
  padding: 0 0.2rem;
  z-index: 100;
  position: fixed;
  left: 0;
  bottom: 0;
  width: 100vw;
  box-sizing: border-box;
}`);

// Update animation classes
content = content.replace(/\.ratio-box\.is-opening \.panoramic-container,\s*\.ratio-box\.is-opening \.header,\s*\.ratio-box\.is-opening \.scroll-footer \{/, 
  `.ratio-box.is-opening .panoramic-container,
.header.is-opening,
.scroll-footer.is-opening {`);

// Update scroll-container to reserve space for footer
content = content.replace(/\.scroll-container \{[\s\S]*?\}/, `.scroll-container {
  width: 100vw;
  height: 100vh;
  background-color: transparent;
  overflow-x: auto;
  overflow-y: hidden;
  position: relative;
  transition: background-color 0.5s ease;
  box-sizing: border-box;
  padding-bottom: 0.68rem;
}
.scroll-container::-webkit-scrollbar {
  display: none;
}`);

// Make ratio-box height 100% (which will be 100vh - 0.68rem)
content = content.replace(/\.ratio-box \{[\s\S]*?\}/, `.ratio-box {
  height: 100%;
  width: max-content;
  position: relative;
}`);


fs.writeFileSync('src/App.vue', content);
console.log("Layout patch applied.");
