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
      <div class="scroll-handle handle-left" @mouseenter="startScroll('left')" @mouseleave="stopScroll">
        <img src="/Group 2@2x.png" alt="">
      </div>

      <!-- 卷轴轴柄 - 右边 (绝对定位在 scroll-container 的边缘) -->
      <div class="scroll-handle handle-right" @mouseenter="startScroll('right')" @mouseleave="stopScroll">
        <img src="/Group 3@2x.png" alt="">
      </div>

      <!-- Ratio Box (100% width) -->
      <div class="ratio-box" :class="{ 'is-opening': isOpening, 'is-opened': isOpened }">
        <div class="scroll-wrapper">
          <!-- 这里使用 ref 处理真正的横向滚动 -->
          <div class="scroll-content" ref="scrollContainer">
            <!-- 中间全景展示大图与交互热点区域 -->
            <div class="panoramic-container">
              <!-- 背景画卷 -->
              <img src="/Group 1@2x.png" alt="霍尔果斯口岸全景图" class="panoramic-bg" />

              <!-- 左上角观光旅游人数统计卡片 -->
              <div class="tourist-card">
                <div class="tourist-header">
                  <span class="eye-icon">👁️</span>
                  <span class="tourist-title">观光旅游人数</span>
                </div>
                <div class="tourist-num">1,121 <span class="unit">人</span></div>
                <div class="tourist-compare">
                  <span>环比</span>
                  <span class="trend-up">▲ 12.5%</span>
                </div>
              </div>

              <!-- 地标与功能区热点标注标签 -->
              <div 
                v-for="marker in markers" 
                :key="marker.id"
                class="map-marker"
                :style="{ left: marker.x + '%', top: marker.y + '%' }"
                @click="activeMarker = marker"
              >
                <div class="marker-img-container">
                  <img :src="marker.bgImg" class="marker-bg-img" alt="" />
                  <span class="marker-overlay-title"></span>
                </div>
              </div>

              <!-- 弹窗展示选中地标/板块的详细信息 -->
              <div v-if="activeMarker" class="marker-modal-backdrop" @click.self="activeMarker = null">
                <div class="marker-modal">
                  <button class="modal-close" @click="activeMarker = null">✕</button>
                  <h3>{{ activeMarker.title }}</h3>
                  <div class="modal-divider"></div>
                  <p>{{ activeMarker.desc }}</p>
                  <div class="modal-stats">
                    <div class="stat-item" v-for="(stat, idx) in activeMarker.stats" :key="idx">
                      <span class="stat-value">{{ stat.value }}</span>
                      <span class="stat-label">{{ stat.label }}</span>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      
      <!-- 底部 Footer (固定在 scroll-container) -->
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
  </div>
</template>


<script setup>
import { ref, onMounted, onUnmounted } from 'vue'


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
const lastUpdated = ref('2027/07/03 14:32')
const currentTime = ref('2027/07/03 14:32')
const activeMarker = ref(null)

// 卷轴动画状态
const isOpening = ref(true)
const isOpened = ref(false)

const currentNavIndex = ref(0)
const footerNavs = ref([
  '驿站溯源',
  '口岸脉动',
  '货通四海',
  '产业新城',
  '智慧未来'
])

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
    currentTime.value = `${year}/${month}/${day} ${hours}:${minutes}`
  }, 1000)
})

onUnmounted(() => {
  if (timer) clearInterval(timer)
})

// 地标数据定义 - 100%使用 public/ 中的 Group 92@2x 包含光柱及图文贴图的精美背景图片 (坐标已校准: x - 1, y + 3)
const markers = ref([
  { id: 1, x: 4.8, y: 59.5, title: '古驿站遗址', bgImg: '/Frame 417@2x.png', desc: '古代丝绸之路重要的商埠与通关驿站，见证千年丝路文明与商业贸易繁荣。', stats: [{ label: '建驿历史', value: '1000+年' }, { label: '遗址面积', value: '15.6公顷' }] },
  { id: 2, x: 16.5, y: 57.0, title: '六代国门', bgImg: '/Frame 422@2x.png', desc: '霍尔果斯历经六代国门的建设与演变，展现了中国边境口岸的沧桑巨变与辉煌发展。', stats: [{ label: '演进历程', value: '6代迭代' }, { label: '通关能力', value: '提升100倍' }] },
  // { id: 3, x: 25.2, y: 52.5, title: '口岸建成', bgImg: '/Group 92@2x(2).png', desc: '口岸城市现代化建设核心示范区，具备完善的公共服务与高品质生活配套设施。', stats: [{ label: '建成区面积', value: '38.5k㎡' }, { label: '常住人口', value: '10.2万' }] },
  { id: 4, x: 24.5, y: 80.0, title: '公路口岸通关区', bgImg: '/Frame 418@2x.png', desc: '高效智能的现代公路物流通关区，集查验、通关、物流于一体，实现快速高效通关。', stats: [{ label: '日均通关车次', value: '2500+辆' }, { label: '平均通关时间', value: '15分钟' }] },
  { id: 5, x: 34.0, y: 61.5, title: '中欧班列', bgImg: '/Frame 425@2x.png', desc: '亚欧陆路交通干线核心枢纽节点，累计开行中欧班列数万列，辐射欧亚多个国家。', stats: [{ label: '开行线路', value: '75条' }, { label: '通达国家', value: '18个' }] },
  // { id: 6, x: 40.5, y: 48.0, title: '综合保税区大门', bgImg: '/Group 92@2x(1).png', desc: '霍尔果斯综合保税区核心进出枢纽，享受免税、保税、退税等多重国家级优惠政策。', stats: [{ label: '入驻企业', value: '450+家' }, { label: '年贸易额', value: '320亿' }] },
  { id: 8, x: 49.8, y: 41.0, title: '霍尔果斯经济开发区', bgImg: '/Frame 426@2x.png', desc: '国家级经济开发区，推动跨境产业与新兴工业全产业链高质量发展。', stats: [{ label: '开发区面积', value: '73k㎡' }, { label: '投产项目', value: '210个' }] },
  { id: 9, x: 58.5, y: 48.5, title: '自贸区', bgImg: '/Frame 429@2x.png', desc: '中国（新疆）自由贸易试验区霍尔果斯片区。', stats: [{ label: '企业注册', value: '1200+' }, { label: '政策扶持', value: '全方位' }] },
  // { id: 10, x: 57.5, y: 70.0, title: '跨境电商综试区', bgImg: '/Group 92@2x(4).png', desc: '集仓储、展示、交易、跨境配送为一体的综合性跨境电商产业孵化园区。', stats: [{ label: '单日包裹', value: '50万+' }, { label: '园区企业', value: '120家' }] },
  { id: 11, x: 68.5, y: 54.5, title: '中哈合作中心', bgImg: '/Frame 430@2x.png', desc: '全球首个跨国边境自由贸易合作区，实现中哈两国人员、车辆与货物的自由流动。', stats: [{ label: '免税额度', value: '8000元/人' }, { label: '日均客流', value: '2.5万人' }] },
  { id: 12, x: 77.2, y: 36.0, title: '城市天际线', bgImg: '/Frame 419@2x.png', desc: '展现现代化口岸新城向现代化高科技城市迈进的雄伟城市轮廓。', stats: [{ label: '建筑地标', value: '12座' }, { label: '绿化覆盖率', value: '42%' }] },
  { id: 13, x: 88.0, y: 66.5, title: '智慧治理指挥中心', bgImg: '/Frame 420@2x.png', desc: '依托大屏监控与全域感知系统，实现口岸人流、物流、车流及城市的精细化全天候运营管理。', stats: [{ label: '全域感知设备', value: '12000+' }, { label: '事件处置率', value: '99.8%' }] },
  { id: 14, x: 82.0, y: 83.0, title: '产业园区', bgImg: '/Frame 427@2x.png', desc: '涵盖先进制造、农产品深加工、高端装备制造的跨境优势产业集群。', stats: [{ label: '产值规模', value: '180亿元' }, { label: '科技企业', value: '68家' }] },
  { id: 15, x: 88.5, y: 93.0, title: '未来规划蓝图', bgImg: '/Frame 428@2x.png', desc: '立足亚欧黄金通道，规划打造全球顶级的绿色、智能、人文、包容的国际一流智慧口岸。', stats: [{ label: '规划面积', value: '120k㎡' }, { label: '远期贸易额', value: '1000亿' }] }
])
</script>

<style scoped>
/* 整个页面与背景 */
.app-shell {
  width: 100vw;
  height: 100vh;
  padding: 0.5rem;
  box-sizing: border-box;
  position: relative;
  overflow: hidden;
}

.scroll-container {
  width: 100%;
  height: 100%;
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
  font-size: 0.3rem;
  color: #5c4015;
}

.icon-refresh{
  font-size: 0px;
}
.icon-clock{
  font-size: 0px;
}
.icon-refresh img{
  width: 0.4rem;
}
.icon-clock img{
  width: 0.4rem;
}
.icon-weather img{
  width: 0.7rem;
}
.icon-weather{
  font-size: 0px;
}

.update-time{
  font-size: 0.3rem;
  color: #5c4015;
}

/* 32:9 比例适配外框 */
.ratio-box {
  height: 100%;
  width: 100%;
  position: relative;
}

/* 卷轴主体包裹器 */
.scroll-wrapper {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 100%;
  position: relative;
  padding:0.3rem 0.45rem;
  box-sizing: border-box;
}

/* 卷轴内部展布画布区域（居中展开） */
.scroll-content {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  background: #fbf6ec;
  position: relative;
  overflow-x: auto;
  overflow-y: hidden;
  overscroll-behavior-x: none;
  box-shadow: inset 0 0 40px rgba(100, 60, 20, 0.15);
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

.ratio-box.is-opening .panoramic-container,

.scroll-footer.is-opening {
  height: 0.68rem;
  background: linear-gradient(180deg, #3d2b15 0%, #1e1308 100%);
  border-top: 0.02rem solid #d49c25;
  display: flex;
  align-items: center;
  justify-content: space-around;
  padding: 0 0.2rem;
  z-index: 100;
  position: absolute;
  left: 0;
  bottom: .3rem;
  width: 100%;
  box-sizing: border-box;
}
.header.is-opening{
  height: 0.68rem;
  background: linear-gradient(180deg, #3d2b15 0%, #1e1308 100%);
  border-top: 0.02rem solid #d49c25;
  display: flex;
  align-items: center;
  justify-content: space-around;
  padding: 0 0.2rem;
  z-index: 100;
  position: absolute;
  left: .3rem;
  bottom: 0;
  width: 100%;
  box-sizing: border-box;
}

/* 纯物理宽度展开关键帧 */
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
  padding:0px 1rem;
  z-index: 100;
  width: 100%;
  position: absolute;
  left: 0;
  top: .3rem;
  box-sizing: border-box;
}

.header-left, .header-right {
  display: flex;
  align-items: center;
  gap: 0.15rem;
  font-size: 0.14rem;
  color: #5c4015;
  font-weight: 500;
}

.header-center {
  width:50%;
  font-size:0px
}

.header-title-img {
  width: 100%;
  object-fit: contain;
}

/* 中间全景展示大图区域 */
.panoramic-container {
  height: 100%;
  position: relative;
  overflow: hidden;
  width: max-content;
}

.panoramic-bg {
  height: 100%;
  width: auto;
  object-position: center;
  display: block;
}

/* 左上角观光旅游人数统计卡片 */
.tourist-card {
  position: absolute;
  top: 2rem;
  left: 0.7rem;
  z-index: 8;
  background: rgba(30, 24, 15, 0.75);
  border: 1px solid rgba(212, 175, 55, 0.6);
  border-radius: 0.08rem;
  padding: 0.1rem 0.16rem;
  color: #fff;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.4);
  backdrop-filter: blur(4px);
  min-width: 1.4rem;
}

.tourist-header {
  display: flex;
  align-items: center;
  gap: 0.06rem;
  font-size: 0.12rem;
  color: #e0c896;
}

.tourist-num {
  font-size: 0.24rem;
  font-weight: bold;
  color: #ffffff;
  margin: 0.04rem 0;
  font-family: "Arial", sans-serif;
}

.tourist-num .unit {
  font-size: 0.12rem;
  font-weight: normal;
  color: #d0c0a0;
}

.tourist-compare {
  display: flex;
  justify-content: space-between;
  font-size: 0.11rem;
  color: #b0a080;
}

.trend-up {
  color: #52c41a;
  font-weight: bold;
}

/* 地标标注样式 - 使用 public 中的图片做为基底光柱和气泡框 */
.map-marker {
  position: absolute;
  transform: translate(-50%, -100%);
  cursor: pointer;
  z-index: 4;
  transition: transform 0.3s ease;
}

.map-marker:hover {
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
  height: 1.45rem;
  width: auto;
  display: block;
  filter: drop-shadow(0 8px 16px rgba(0, 0, 0, 0.6));
}

.marker-overlay-title {
  position: absolute;
  top: 0.2rem;
  font-size: 0.24rem;
  font-weight: bold;
  color: #ffffff;
  white-space: nowrap;
  letter-spacing: 0.02rem;
  text-shadow: 0 0.02rem 0.06rem rgba(0, 0, 0, 0.95), 0 0 0.08rem rgba(0, 0, 0, 0.85);
  pointer-events: none;
}

/* 详情弹窗 Modal */
.marker-modal-backdrop {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.4);
  backdrop-filter: blur(4px);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 20;
}

.marker-modal {
  width: 4.2rem;
  background: linear-gradient(135deg, #fffcf7 0%, #f7eedb 100%);
  border: 0.02rem solid #d4af37;
  border-radius: 0.16rem;
  padding: 0.24rem;
  box-shadow: 0 0.12rem 0.32rem rgba(0, 0, 0, 0.3);
  position: relative;
  animation: modalFadeIn 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}

@keyframes modalFadeIn {
  from { opacity: 0; transform: scale(0.8) translateY(0.2rem); }
  to { opacity: 1; transform: scale(1) translateY(0); }
}

.modal-close {
  position: absolute;
  top: 0.14rem;
  right: 0.16rem;
  background: none;
  border: none;
  font-size: 0.2rem;
  color: #8c6a38;
  cursor: pointer;
}

.marker-modal h3 {
  font-size: 0.22rem;
  color: #4a2f07;
  margin-bottom: 0.1rem;
  font-family: "STKaiti", "KaiTi", serif;
}

.modal-divider {
  height: 0.02rem;
  background: linear-gradient(90deg, #e65c00 0%, #ff9d1e 50%, transparent 100%);
  margin-bottom: 0.14rem;
}

.marker-modal p {
  font-size: 0.14rem;
  line-height: 1.6;
  color: #554433;
  margin-bottom: 0.2rem;
}

.modal-stats {
  display: flex;
  gap: 0.16rem;
  background: rgba(230, 92, 0, 0.06);
  border-radius: 0.1rem;
  padding: 0.12rem;
}

.stat-item {
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.stat-value {
  font-size: 0.18rem;
  font-weight: bold;
  color: #e65c00;
}

.stat-label {
  font-size: 0.12rem;
  color: #776655;
  margin-top: 0.04rem;
}

/* 底部 Golden 卷轴五大板块栏 */
.scroll-footer {
  height: 0.68rem;
  border-top: 0.02rem solid #d49c25;
  display: flex;
  align-items: center;
  justify-content: space-around;
  padding: 0 0.2rem;
  z-index: 100;
  position: absolute;
  bottom: .3rem;
  left: 0;
  width: 100%;
  box-sizing: border-box;
}

.footer-nav-cell {
  flex: 1;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  position: relative;
  background: linear-gradient(180deg, #6e4e20 0%, #3d280d 100%);
  border-right: 1px solid rgba(212, 175, 55, 0.4);
  transition: all 0.3s ease;
}

.footer-nav-cell:last-child {
  border-right: none;
}

.footer-nav-cell.active,
.footer-nav-cell:hover {
  background: linear-gradient(180deg, #c49438 0%, #855f19 100%);
}

.nav-text {
  font-family: "STKaiti", "KaiTi", serif;
  font-size: 0.24rem;
  font-weight: bold;
  color: #f7eedb;
  letter-spacing: 0.04rem;
  text-shadow: 0 0.02rem 0.04rem rgba(0, 0, 0, 0.6);
}
</style>
