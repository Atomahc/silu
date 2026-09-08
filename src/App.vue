<template>
  <div class="app-shell">
    <div class="scroll-container" :class="{ 'is-night': isNight }">
      
      <!-- 头部 Header (固定在 scroll-container) -->
      <header class="header" :class="{ 'is-opening': isOpening, 'is-opened': isOpened }">
        <div class="header-left">
          <div class="time-update">
            <div class="icon-refresh">
                <img src="/Frame@2x.png" alt="">
            </div>
            <div class="update-time">更新时间：{{ lastUpdated }}</div>
          </div>
        </div>
        <div class="header-center">
          <img src="/标题@2x-1.png" alt="霍尔果斯口岸数字名片" class="header-title-img" />
        </div>
        <div class="header-right">
          <div class="current-time">
            <div class="icon-clock">
                <img src="/Frame@2x(1).png" alt="">
            </div>
            <div>{{ currentTime }}</div>
          </div>
          <div class="weather-info">
            <div class="icon-weather">
              <img src="/image 2@2x.png" alt="">
            </div>
            <div>24~32°C</div>
          </div>
        </div>
      </header>

      <!-- 卷轴轴柄 - 左边 (绝对定位在 scroll-container 的边缘) -->
      <div class="scroll-handle handle-left" :class="{ 'is-opening': isOpening, 'is-opened': isOpened }" @mouseenter="startScroll('left')" @mouseleave="stopScroll">
        <img src="/Group 2@2x.png" alt="">
      </div>

      <!-- 卷轴轴柄 - 右边 (绝对定位在 scroll-container 的边缘) -->
      <div class="scroll-handle handle-right" :class="{ 'is-opening': isOpening, 'is-opened': isOpened }" @mouseenter="startScroll('right')" @mouseleave="stopScroll">
        <img src="/Group 3@2x.png" alt="">
      </div>

      <!-- Ratio Box (100% width) -->
      <div class="ratio-box" :class="{ 'is-opening': isOpening, 'is-opened': isOpened }">
        <div class="scroll-wrapper">
          <!-- 这里使用 ref 处理真正的横向滚动 -->
          <div class="scroll-content" ref="scrollContainer" 
               @mousedown="startDrag" 
               
               :class="{ 'is-dragging': isDragging }">
            <!-- 中间全景展示大图与交互热点区域 -->
            <div class="panoramic-container">
              <!-- 背景画卷 -->
              <img src="/Group 1@2x.png" alt="霍尔果斯口岸全景图" class="panoramic-bg" />
              <TouristCard v-if="activeMarker && activeMarker.id === 1" style="top: 61.5%; left: 5.8%; transform: translate(-50%, calc(-100% - 1.5rem));" />

              

              <!-- 数据面板 -->
              <DataBox v-if="activeMarker && activeMarker.id === 4" style="top: 80%; left: 29.5%; transform: translate(-50%, calc(-100% - 1.5rem)); z-index: 100;" />
              <DataBoxIndustry v-if="activeMarker && activeMarker.id === 14" style="top: 89%; left: 77.0%; transform: translate(-50%, calc(-100% - 1.5rem)); z-index: 100;" />
              <DataBoxGovernance v-if="activeMarker && activeMarker.id === 13" style="top: 67.5%; left: 90.0%; transform: translate(-80%, calc(-100% - 1.5rem)); z-index: 100;" />

              <!-- 地标与功能区热点标注标签 -->
              <div 
                v-for="marker in markers" 
                :key="marker.id"
                class="map-marker"
                :style="{ left: marker.x + '%', top: marker.y + '%' }"
                @click="activeMarker = activeMarker && activeMarker.id === marker.id ? null : marker"
              >
                <div class="marker-img-container" :style="{ width: marker.width || 'auto', height: marker.height || 'auto' }">
                  <img :src="marker.bgImg" class="marker-bg-img" alt="" />
                  <span class="marker-overlay-title">{{ marker.title }}</span>
                  <img v-if="marker.bottomImg" :src="marker.bottomImg" class="marker-bottom-img" alt="" />
                  <div v-if="marker.tag" class="marker-custom-tag">{{ marker.tag }}</div>
                </div>
              </div>

            </div>
          </div>
        </div>
      </div>
              <!-- 弹窗展示选中地标/板块的详细信息 -->
              <div v-if="activeMarker && activeMarker.id !== 4 && activeMarker.id !== 14 && activeMarker.id !== 13 && activeMarker.id !== 1" class="marker-modal-backdrop" @click.self="activeMarker = null">
                <div class="marker-modal" :class="{ 'html-modal': activeMarker.htmlContent }">
                  <button class="modal-close" @click="activeMarker = null">✕</button>
                  <h3>{{ activeMarker.title }}</h3>
                  <div class="modal-divider"></div>
                  <div v-if="activeMarker.htmlContent" class="modal-html-content custom-scrollbar" v-html="activeMarker.htmlContent"></div>
                  <template v-else>
                    <p>{{ activeMarker.desc }}</p>
                    <div class="modal-stats">
                      <div class="stat-item" v-for="(stat, idx) in activeMarker.stats" :key="idx">
                        <span class="stat-value">{{ stat.value }}</span>
                        <span class="stat-label">{{ stat.label }}</span>
                      </div>
                    </div>
                  </template>
                </div>
              </div>

      
      
      <!-- 右侧弹出框 -->
      <transition name="slide-right">
        <div class="right-popup" v-if="currentNavIndex !== '' && currentNavIndex !== null">
          <div class="right-popup-inner">
            <img class="popup-bg" src="/Group 130@2x.png" alt="" draggable="false" />
            <img class="popup-close" src="/Group 40@2x.png" @click="currentNavIndex = ''" alt="close" draggable="false" />
            <div class="popup-title">{{ footerNavs[currentNavIndex] }}</div>
            <div class="popup-content">
              <component :is="panels[currentNavIndex]" v-if="currentNavIndex !== '' && currentNavIndex !== null" />
            </div>
          </div>
        </div>
      </transition>

      <!-- 底部 Footer (固定在 scroll-container) -->
      <footer class="scroll-footer" :class="{ 'is-opening': isOpening, 'is-opened': isOpened }">
        <div class="flexdvv">
                  <div 
          v-for="(nav, index) in footerNavs" 
          :key="index" 
          class="footer-nav-cell"
          :class="{ active: currentNavIndex === index }"
          @click="currentNavIndex = index"
        >
          <span class="nav-text">{{ nav }}</span>
        </div>
        </div>

      </footer>

    </div>
  </div>
</template>


<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

import Panel0 from './components/Panel0.vue'
import Panel1 from './components/Panel1.vue'
import Panel2 from './components/Panel2.vue'
import Panel3 from './components/Panel3.vue'
import Panel4 from './components/Panel4.vue'
import DataBox from './components/DataBox.vue'
import DataBoxIndustry from './components/DataBoxIndustry.vue'
import DataBoxGovernance from './components/DataBoxGovernance.vue'
import TouristCard from './components/TouristCard.vue'

import marker1Html from './html/marker_1.html?raw'
import marker2Html from './html/marker_2.html?raw'
import marker3Html from './html/marker_3.html?raw'
import marker6Html from './html/marker_6.html?raw'
import marker10Html from './html/marker_10.html?raw'
import marker12Html from './html/marker_12.html?raw'
import marker13Html from './html/marker_13.html?raw'
import marker14Html from './html/marker_14.html?raw'



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

const isNight = ref(false)
const lastUpdated = ref('2026/07/03')
const currentTime = ref('2026/07/03')
const activeMarker = ref(null)

// 卷轴动画状态
const isOpening = ref(true)
const isOpened = ref(false)

const currentNavIndex = ref("")
const panels = [Panel0, Panel1, Panel2, Panel3, Panel4]
const footerNavs = ref([
  '数字党建',
  '数字政务',
  '数字经济',
  '数字社会',
  '数字文化',
  '平安霍尔果斯'
])


// 拖拽滚动逻辑
const isDragging = ref(false)
const startX = ref(0)
const scrollLeftStart = ref(0)

const startDrag = (e) => {
  if (!scrollContainer.value) return
  e.preventDefault(); // 阻止默认的图片拖拽和选中行为
  startX.value = e.pageX - scrollContainer.value.offsetLeft;
  scrollLeftStart.value = scrollContainer.value.scrollLeft;
  
  // 绑定到 window 以防止鼠标移出容器导致拖拽断断续续
  window.addEventListener('mousemove', onDrag);
  window.addEventListener('mouseup', stopDrag);
}

const onDrag = (e) => {
  if (!scrollContainer.value) return;
  const x = e.pageX - scrollContainer.value.offsetLeft;
  if (Math.abs(x - startX.value) > 5) {
    isDragging.value = true;
  }
  if (!isDragging.value) return;
  
  e.preventDefault();
  const walk = (x - startX.value) * 1.5; // 滚动系数
  
  // 使用 requestAnimationFrame 保证渲染平滑
  requestAnimationFrame(() => {
    if (scrollContainer.value) {
      scrollContainer.value.scrollLeft = scrollLeftStart.value - walk;
    }
  });
}

const stopDrag = () => {
  // 延迟恢复以避免触发点击
  setTimeout(() => {
    isDragging.value = false;
  }, 50);
  window.removeEventListener('mousemove', onDrag);
  window.removeEventListener('mouseup', stopDrag);
}

const triggerScrollAnimation = () => {
  isOpening.value = true
  isOpened.value = false
  setTimeout(() => {
    isOpening.value = false
    isOpened.value = true
  }, 3800)
}

const replayScrollAnimation = () => {
  triggerScrollAnimation()
}

const toggleDayNight = () => {
  isNight.value = !isNight.value
}

// 定时更新实时时间
let timer = null
onMounted(() => {
  triggerScrollAnimation()
  timer = setInterval(() => {
    const now = new Date()
    const year = now.getFullYear()
    const month = String(now.getMonth() + 1).padStart(2, '0')
    const day = String(now.getDate()).padStart(2, '0')
    const hours = String(now.getHours()).padStart(2, '0')
    const minutes = String(now.getMinutes()).padStart(2, '0')
    currentTime.value = `${year}/${month}/${day}`
  }, 1000)
})

onUnmounted(() => {
  if (timer) clearInterval(timer)
})

// 地标数据定义 - 100%使用 public/ 中的 Group 92@2x 包含光柱及图文贴图的精美背景图片 (坐标已校准: x - 1, y + 3)
const markers = ref([
  { id: 1, x: 5.8, y: 50.5, title: '驿站溯源', bgImg: './laby1.png', bottomImg: './labyb.png', width: 'auto', height: '.4rem', desc: '古代丝绸之路重要的商埠与通关驿站，见证千年丝路文明与商业贸易繁荣。', stats: [{ label: '建驿历史', value: '1000+年' }, { label: '遗址面积', value: '15.6公顷' }], htmlContent: marker1Html },
  { id: 2, x: 14.5, y: 45.0, title: '六代国门', bgImg: './laby1.png', bottomImg: './labyb.png', width: 'auto', height: '.4rem', desc: '霍尔果斯历经六代国门的建设与演变，展现了中国边境口岸的沧桑巨变与辉煌发展。', stats: [{ label: '演进历程', value: '6代迭代' }, { label: '通关能力', value: '提升100倍' }], htmlContent: marker2Html },
  { id: 4, x: 29.5, y: 68.0, title: '公路口岸通关区', bgImg: './labb3.png', bottomImg: './labbb.png', width: '1.7rem', height: '.4rem', desc: '高效智能的现代公路物流通关区，集查验、通关、物流于一体，实现快速高效通关。', stats: [{ label: '日均通关车次', value: '2500+辆' }, { label: '平均通关时间', value: '15分钟' }] },
  { id: 5, x: 20.0, y: 64.5, title: '中欧班列', tag: '实有人口7.1万', bgImg: './labb1.png', bottomImg: './labbb.png', width: 'auto', height: '.4rem', desc: '亚欧陆路交通干线核心枢纽节点，累计开行中欧班列数万列，辐射欧亚多个国家。', stats: [{ label: '开行线路', value: '75条' }, { label: '通达国家', value: '18个' }], htmlContent: marker3Html },
  { id: 8, x: 44.8, y: 29.0, title: '经济开发区', bgImg: './labb3.png', bottomImg: './labbb.png', width: 'auto', height: '.4rem', desc: '国家级经济开发区，推动跨境产业与新兴工业全产业链高质量发展。', stats: [{ label: '开发区面积', value: '73k㎡' }, { label: '投产项目', value: '210个' }] },
  { id: 9, x: 52.5, y: 58.5, title: '自贸区', bgImg: './labg2.png', bottomImg: './labgb.png', width: 'auto', height: '.4rem', desc: '中国（新疆）自由贸易试验区霍尔果斯片区。', stats: [{ label: '企业注册', value: '1200+' }, { label: '政策扶持', value: '全方位' }], htmlContent: marker6Html },
  { id: 11, x: 65.5, y: 42.5, title: '中哈合作中心', bgImg: './labg3.png', bottomImg: './labgb.png', width: '1.6rem', height: '.4rem', desc: '全球首个跨国边境自由贸易合作区，实现中哈两国人员、车辆与货物的自由流动。', stats: [{ label: '免税额度', value: '8000元/人' }, { label: '日均客流', value: '2.5万人' }], htmlContent: marker10Html },
  { id: 12, x: 73.2, y: 24.0, title: '城市天际线', bgImg: './labg3.png', bottomImg: './labgb.png', width: 'auto', height: '.4rem', desc: '展现现代化口岸新城向现代化高科技城市迈进的雄伟城市轮廓。', stats: [{ label: '建筑地标', value: '12座' }, { label: '绿化覆盖率', value: '42%' }], htmlContent: marker12Html },
  { id: 13, x: 90.0, y: 67.5, title: '智慧治理指挥中心', bgImg: './labp1.png', bottomImg: './labpb.png', width: 'auto', height: '.4rem', desc: '依托大屏监控与全域感知系统，实现口岸人流、物流、车流及城市的精细化全天候运营管理。', stats: [{ label: '全域感知设备', value: '12000+' }, { label: '事件处置率', value: '99.8%' }], htmlContent: marker13Html },
  { id: 14, x: 77.0, y: 89.0, title: '产业园区', bgImg: './labg3.png', bottomImg: './labgb.png', width: 'auto', height: '.4rem', desc: '涵盖先进制造、农产品深加工、高端装备制造的跨境优势产业集群。', stats: [{ label: '产值规模', value: '180亿元' }, { label: '科技企业', value: '68家' }] },
  { id: 15, x: 95.5, y: 82.0, title: '未来规划蓝图', bgImg: './labp2.png', bottomImg: './labpb.png', width: 'auto', height: '.4rem', desc: '立足亚欧黄金通道，规划打造全球顶级的绿色、智能、人文、包容的国际一流智慧口岸。', stats: [{ label: '规划面积', value: '120k㎡' }, { label: '远期贸易额', value: '1000亿' }], htmlContent: marker14Html }
])
</script>

<style scoped>
/* 整个页面与背景 */
.app-shell {
  width: 100%;
  height: 100%;
  padding:  0.5rem;
  box-sizing: border-box;
  position: relative;
  overflow: hidden;
  background: #000;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.scroll-container {
  width: 100%;
  height: auto;
  background-color: transparent;
  overflow: hidden;
  position: relative;
  transition: background-color 0.5s ease;
  box-sizing: border-box;
}

.scroll-container.is-night {
  background-color: #03060a;
}
.scroll-container.is-night .ratio-box {
  filter: brightness(0.85) contrast(1.1);
}
.time-update ,.current-time ,.weather-info{
  display: flex;
  align-items: center;
  gap: 0.08rem;
  font-size: 0.2rem;
  color: #5c4015;
}

.icon-refresh{
  font-size: 0px;
}
.icon-clock{
  font-size: 0px;
}
.icon-refresh img{
  width: 0.3rem;
}
.icon-clock img{
  width: 0.3rem;
}
.icon-weather img{
  width: 0.6rem;
}
.icon-weather{
  font-size: 0px;
}

.update-time{
  font-size: 0.2rem;
  color: #5c4015;
  flex-wrap: nowrap;
}

/* 32:9 比例适配外框 */
.ratio-box {
  height: auto;
  width: 100%;
  position: relative;
}

/* 卷轴主体包裹器 */
.scroll-wrapper {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: auto;
  position: relative;
  padding:0.23rem 0.3rem ;
  box-sizing: border-box;
}

/* 卷轴内部展布画布区域（居中展开） */
.scroll-content {
  width: 100%;
  height: auto;
  display: flex;
  flex-direction: column;
  background: #fbf6ec;
  position: relative;
  overflow-x: auto;
  overflow-y: hidden;
  overscroll-behavior-x: none;
  box-shadow: inset 0 0 40px rgba(100, 60, 20, 0.15);
}


.scroll-content {
  cursor: grab;
  user-select: none;
  -webkit-user-select: none;
}
.scroll-content img {
  -webkit-user-drag: none;
}
.scroll-content.is-dragging {
  cursor: grabbing;
}
.scroll-content.is-dragging * {
  pointer-events: none; /* 防止拖拽时误触内部元素 */
}

.scroll-content::-webkit-scrollbar {
  display: none;
}

/* 轴柄定位：绝对绑定在 scroll-container 的左右边缘 */
.handle-left {
  height: 100%;
  position: absolute;
  left: .2rem;
  top: 0;
  z-index: 99999;
  pointer-events: auto;
  cursor: pointer;
  transform: translateX(-30%);
  transition: transform 0.3s;
}
.handle-left:hover {
  /* transform: translateX(-20%); */
}
.handle-left img {
  height: 100%;
  width: auto;
  object-fit: contain;
  filter: drop-shadow(-4px 0 8px rgba(0, 0, 0, 0.4));
}

.handle-right {
  height: 100%;
  position: absolute;
  right: .2rem;
  top: 0;
  z-index: 99999;
  pointer-events: auto;
  cursor: pointer;
  transform: translateX(30%);
  transition: transform 0.3s;
}
.handle-right:hover {
  /* transform: translateX(20%); */
}
.handle-right img {
  height: 100%;
  width: auto;
  object-fit: contain;
  filter: drop-shadow(4px 0 8px rgba(0, 0, 0, 0.4));
}

/* 卷轴展开动画控制：以 width 0% -> 100% 驱动物理伸展，轴柄绝对贴合跟随！ */
.ratio-box.is-opening .scroll-content {
  animation: scrollPhysicalExpand 3.6s cubic-bezier(0.25, 0.1, 0.25, 1) forwards;
}

.ratio-box.is-opening .panoramic-container {
  animation: scrollContentFadeIn 3.6s ease forwards;
}


.scroll-footer {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  position: absolute;
  bottom: 0.23rem;
  left: 0;
  z-index: 100;
  box-sizing: border-box;
}

.flexdvv {
  display: flex;
  gap: 0.2rem;
}

.footer-nav-cell {
  cursor: pointer;
  color: #c0b090;
  padding: 0.05rem 0.15rem;
  border: 1px solid transparent;
  transition: all 0.3s;
}

.footer-nav-cell.active {
  color: #f0e0c0;
  border-color: #d4af37;
  border-radius: 0.2rem;
  background: rgba(212, 175, 55, 0.15);
}

.scroll-footer.is-opening {
  animation: headerFooterExpand 3.6s cubic-bezier(0.25, 0.1, 0.25, 1) forwards;
}
.header.is-opening {
  animation: headerFooterExpand 3.6s cubic-bezier(0.25, 0.1, 0.25, 1) forwards;
}

/* 纯物理宽度展开关键帧 */

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


@keyframes headerFooterExpand {
  0% {
    width: 0.1vw;
    opacity: 0;
  }
  50% {
    opacity: 0;
  }
  100% {
    width: 100%;
    opacity: 1;
  }
}

@keyframes scrollPhysicalExpand {
  0% {
    width: 0.1vw;
    box-shadow: inset 0 0 0px rgba(100, 60, 20, 0);
  }
  100% {
    width: 100%;
    box-shadow: inset 0 0 40px rgba(100, 60, 20, 0.15);
  }
}

@keyframes scrollContentFadeIn {
  0% {
    opacity: 0;
    filter: blur(8px);
  }
  100% {
    opacity: 1;
    filter: blur(0);
  }
}

/* 顶部导航 Header */
.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding:0px .5rem;
  z-index: 100;
  width: 100%;
  position: absolute;
  left: 50%;
  transform: translateX(-50%);
  top: .23rem;
  box-sizing: border-box;
  overflow: hidden;
  white-space: nowrap;
}

.header-left, .header-right {
  display: flex;
  align-items: center;
  gap: 0.15rem;
  font-size: 0.12rem;
  color: #5c4015;
  font-weight: 500;

}
.header-right{
  justify-content: flex-end;
}

.header-center {
  width: 8rem;
  font-size:0px
}

.header-title-img {
  width: 100%;
  object-fit: contain;
}

/* 中间全景展示大图区域 */
.panoramic-container {
  height: auto;
  position: relative;
  overflow: hidden;
  width: 200%;
}

.panoramic-bg {
  height: auto;
  width: 100%;
  object-position: center;
  display: block;
}

/* 地标标注样式 - 使用 public 中的图片做为基底光柱和气泡框 */
@keyframes floatUpDown {
  0% { transform: translate(-50%, -100%); }
  50% { transform: translate(-50%, -105%); }
  100% { transform: translate(-50%, -100%); }
}

.map-marker {
  position: absolute;
  transform: translate(-50%, -100%);
  cursor: pointer;
  z-index: 4;
  transition: transform 0.3s ease;
  animation: floatUpDown 2.5s ease-in-out infinite;
}

.map-marker:hover {
  animation: none;
  transform: translate(-50%, -106%) scale(1.18);
  z-index: 15;
}

.marker-img-container {
  position: relative;
  display: flex;
  justify-content: center;
  align-items: flex-start;
}

.marker-bg-img {
  width: 100%;
  height: 100%;
  object-fit: contain;
  display: block;
  filter: drop-shadow(0 8px 16px rgba(0, 0, 0, 0.6));
}

.marker-bottom-img {
  position: absolute;
  bottom: -0.2rem;
  left: 50%;
  transform: translateX(-50%);
  width: 0.4rem;
  height: auto;
  pointer-events: none;
}

.marker-overlay-title {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  font-size: 0.24rem;
  font-weight: bold;
  color: #ffffff;
  white-space: nowrap;
  letter-spacing: 0.02rem;
  text-shadow: 0 0.02rem 0.06rem rgba(0, 0, 0, 0.95), 0 0 0.08rem rgba(0, 0, 0, 0.85);
  pointer-events: none;
}

.marker-custom-tag {
  position: absolute;
  top: 0;
  right: -0.6rem;
  background: #ff4d4f;
  color: white;
  padding: 0.02rem 0.06rem;
  border-radius: 0.1rem;
  font-size: 0.2rem;
  white-space: nowrap;
}
</style>
