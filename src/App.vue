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

              <!-- 数据面板 -->
              <DataBox style="top: 3.1rem; left: 11.5rem;" />
              <DataBoxIndustry style="top: 3.1rem; left: 34rem;" />

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

            </div>
          </div>
        </div>
      </div>
              <!-- 弹窗展示选中地标/板块的详细信息 -->
              <div v-if="activeMarker" class="marker-modal-backdrop" @click.self="activeMarker = null">
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
  { id: 1, x: 5.8, y: 61.5, title: '古驿站遗址', bgImg: '/Frame 417@2x.png', desc: '古代丝绸之路重要的商埠与通关驿站，见证千年丝路文明与商业贸易繁荣。', stats: [{ label: '建驿历史', value: '1000+年' }, { label: '遗址面积', value: '15.6公顷' }], htmlContent: `<section data-role="outer" class="article135" label="edit by 135editor">
	<section data-role="paragraph" class="_135editor">
		<p style="margin-top:0;margin-right:0;margin-bottom:0;margin-left:0;padding:0 0 0 0;text-align:center;" align="center">
			<strong><span style=";color:#aa0000;font-family:Calibri;"><span style="font-family:Calibri;">“</span><span style="font-family:宋体;">千年驿站，百年口岸</span><span style="font-family:Calibri;">”</span></span></strong>
		</p>
		<p style="margin-top:0;margin-right:0;margin-bottom:0;margin-left:0;padding:0 0 0 0;text-align:center;" align="center">
			<span style=";font-size:16px;font-family:Calibri;"><span style="font-family:宋体;">霍尔果斯口岸位于新疆伊犁哈萨克自治州</span></span>
		</p>
		<p style="margin-top:0;margin-right:0;margin-bottom:0;margin-left:0;padding:0 0 0 0;text-align:center;" align="center">
			<span style=";font-size:16px;font-family:Calibri;"><span style="font-family:宋体;">与哈萨克斯坦隔河相望</span></span>
		</p>
		<p style="margin-top:0;margin-right:0;margin-bottom:0;margin-left:0;padding:0 0 0 0;text-align:center;" align="center">
			<span style=";font-size:16px;font-family:Calibri;"><span style="font-family:宋体;">在历史的更迭中</span></span>
		</p>
		<p style="margin-top:0;margin-right:0;margin-bottom:0;margin-left:0;padding:0 0 0 0;text-align:center;" align="center">
			<span style=";font-size:16px;font-family:Calibri;"><span style="font-family:宋体;">作为</span><span style="font-family:Calibri;">“</span><span style="font-family:宋体;">西北国际大通道</span><span style="font-family:Calibri;">”</span><span style="font-family:宋体;">的起点</span></span>
		</p>
		<p style="margin-top:0;margin-right:0;margin-bottom:0;margin-left:0;padding:0 0 0 0;text-align:center;" align="center">
			<span style=";font-size:16px;font-family:Calibri;"><span style="font-family:宋体;">担负着重要的外贸运输职责</span></span>
		</p>
		<p style="margin-top:0;margin-right:0;margin-bottom:0;margin-left:0;padding:0 0 0 0;text-align:center;" align="center">
			<span style=";font-size:16px;font-family:Calibri;"><span style="font-family:宋体;">抗战时期</span></span>
		</p>
		<p style="margin-top:0;margin-right:0;margin-bottom:0;margin-left:0;padding:0 0 0 0;text-align:center;" align="center">
			<span style=";font-size:16px;font-family:Calibri;"><span style="font-family:宋体;">曾被誉为</span><span style="font-family:Calibri;">“</span><span style="font-family:宋体;">红色口岸</span><span style="font-family:Calibri;">”“</span><span style="font-family:宋体;">生命通道</span><span style="font-family:Calibri;">”</span></span>
		</p>
		<p style="margin-top:0;margin-right:0;margin-bottom:0;margin-left:0;text-indent:28px;padding:0 0 0 0">
			<span style=";font-size:16px;font-family:Calibri;"><span style="font-family:宋体;">新疆伊犁</span><span style="font-family:Calibri;">“</span><span style="font-family:宋体;">百年口岸</span><span style="font-family:Calibri;">”</span><span style="font-family:宋体;">霍尔果斯是西北大通道的一个重要驿站，这里是丝绸之路经济带上的重要枢纽。而在</span><span style="font-family:Calibri;">70</span><span style="font-family:宋体;">多年前的抗日战争中，这里曾是苏联援华物资运输大通道</span><span style="font-family:Calibri;">——“</span><span style="font-family:宋体;">西北国际大通道</span><span style="font-family:Calibri;">”</span><span style="font-family:宋体;">陆路通道的起点，被誉为</span><span style="font-family:Calibri;">“</span><span style="font-family:宋体;">红色口岸</span><span style="font-family:Calibri;">”“</span><span style="font-family:宋体;">生命通道</span><span style="font-family:Calibri;">”</span><span style="font-family:宋体;">。</span></span>
		</p>
		<p style="margin-top:0;margin-right:0;margin-bottom:0;margin-left:0;text-indent:28px;padding:0 0 0 0;text-align:left;" align="left">
			<span style=";font-size:16px;font-family:Calibri;"><span style="font-family:宋体;">抗日战争时期，</span></span><strong><span style=";color:#aa0000;font-family:Calibri;"><span style="font-family:宋体;">中国</span>80%<span style="font-family:宋体;">以上的外国援助物资来自苏联，而其中的</span><span style="font-family:Calibri;">90%</span><span style="font-family:宋体;">又都是通过霍尔果斯口岸运送入境。</span></span></strong><img src="https://bexp.135editor.com/files/users/1497/14974597/202608/QXTDbeJF_LnbA.png?auth_key=1788105599-0-0-fbecf62ccc4a81fdf967fb4899f30aef" alt="图片1.png" style="text-align: center; caret-color: red; vertical-align: baseline; width: 100%;box-sizing:border-box;max-width:100% !important;" draggable="false" data-ratio="0.6152450090744102" data-w="551"/>
		</p>
		<p style=";text-align:center;" align="center">
			<span style=";font-size:16px;font-family:宋体;"><span style="font-family:宋体;">图为抗战时期途经霍尔果斯运输而来的物资。</span></span>
		</p>
		<p style="margin-top:0;margin-right:0;margin-bottom:0;margin-left:0;text-indent:28px;padding:0 0 0 0">
			<span style=";font-size:16px;font-family:Calibri;"><span style="font-family:Calibri;">“</span><span style="font-family:宋体;">西北国际大通道</span><span style="font-family:Calibri;">”</span><span style="font-family:宋体;">的开通，凝聚着中国共产党人的心血。当时人口不足</span><span style="font-family:Calibri;">500</span><span style="font-family:宋体;">万的新疆在极其艰苦的条件下投入了</span><span style="font-family:Calibri;">50</span><span style="font-family:宋体;">多万人力，</span><span style="font-family:Calibri;">35</span><span style="font-family:宋体;">天内修通了从霍尔果斯到星星峡</span><span style="font-family:Calibri;">1500</span><span style="font-family:宋体;">多公里的公路，为保证国际援华物资运输的畅通作出了重要贡献。</span></span>
		</p>
		<p style="margin-top:0;margin-right:0;margin-bottom:0;margin-left:0;text-indent:28px;padding:0 0 0 0">
			<span style=";font-size:16px;font-family:Calibri;">1937<span style="font-family:宋体;">年</span><span style="font-family:Calibri;">10</span><span style="font-family:宋体;">月，八路军驻新疆办事处成立，其重要任务之一就是维护国际交通线的畅通。</span><span style="font-family:Calibri;">1938</span><span style="font-family:宋体;">年</span><span style="font-family:Calibri;">2</span><span style="font-family:宋体;">月，应新疆军阀盛世才要求，党中央从</span><span style="font-family:Calibri;">“</span><span style="font-family:宋体;">新兵营</span><span style="font-family:Calibri;">”</span><span style="font-family:宋体;">抽调一批干部，组织民众修路、护路，确保国际援华抗日物资运输交通线的畅通。中共中央驻新疆代表陈潭秋在向党中央报告工作时也说：</span><span style="font-family:Calibri;">“</span><span style="font-family:宋体;">保证这条交通线的畅通是我党在新疆工作的重要任务。</span><span style="font-family:Calibri;">”</span></span>
		</p>
		<p style="margin-top:0;margin-right:0;margin-bottom:0;margin-left:0;text-indent:28px;padding:0 0 0 0">
			<span style=";font-size:16px;font-family:Calibri;">1500<span style="font-family:宋体;">多公里即使在今天也是一条漫长的道路。在国家危亡之际，在中国共产党人的带领下，新疆各族民众肩扛手提，在崇山峻岭间、深沟险壑中打通了从霍尔果斯到星星峡的通道。</span></span>
		</p>
		<p style="margin-top:0;margin-right:0;margin-bottom:0;margin-left:0;text-indent:28px;padding:0 0 0 0">
			<span style=";font-size:16px;font-family:Calibri;"><span style="font-family:Calibri;">“</span><span style="font-family:宋体;">不怕山高，不怕无边的戈壁，不怕风霜雨雪，我们为了新疆的建设，大家一起用力。</span><span style="font-family:Calibri;">”1939</span><span style="font-family:宋体;">年</span><span style="font-family:Calibri;">5</span><span style="font-family:宋体;">月出版的《新疆日报》上刊登着这样一首《筑路歌》。作者是共产党员沈雁冰，也就是茅盾先生。读着这些歌词，眼前仿佛浮现出当时新疆各族民众唱着歌儿鼓着劲儿，一起建设、守护这条红色交通线的场景。</span></span>
		</p>
		<p style=";text-align:center;" align="center">
			<img src="https://bexp.135editor.com/files/users/1497/14974597/202608/uXgavCDp_75rJ.png?auth_key=1788105599-0-0-7a3d692f8cc04f639b45ea74c6efd5dd" style="vertical-align: baseline; width: 100%;box-sizing:border-box;max-width:100% !important;" alt="图片2.png" draggable="false" data-ratio="0.6737804878048781" data-w="656"/>
		</p>
		<p style=";text-align:center;" align="center">
			<span style=";font-size:16px;font-family:宋体;"><span style="font-family:宋体;">图为抗战时期中苏在霍尔果斯的货物进出通道。</span></span>
		</p>
		<p style="text-align:center;" align="center">
			<img src="https://bexp.135editor.com/files/users/1497/14974597/202608/x7Pf5Zrf_jJa7.png?auth_key=1788105599-0-0-319f8bf5491eca62b97cf546215701d2" style="vertical-align: baseline; width: 100%;box-sizing:border-box;max-width:100% !important;" alt="图片3.png" draggable="false" data-ratio="0.496" data-w="500"/>
		</p>
		<p style=";text-align:center;" align="center">
			<span style=";font-size:16px;font-family:宋体;"><span style="font-family:宋体;">西起霍尔果斯，东到哈密星星峡的</span>1500多公里运输线。</span>
		</p>
		<p style=";text-align:left;" align="left">
			<span style=";font-size:16px;font-family:宋体;">1940年12月，苏联300辆载重汽车满载飞机配件、大炮、轻重机枪、汽油等抗战物资从霍尔果斯入境，返回时运回中国做抵偿的茶叶、羊毛等物资。</span>
		</p>
		<p style=";text-align:left;" align="left">
			<img src="https://bexp.135editor.com/files/users/1497/14974597/202608/uu2ODgaZ_6B3L.png?auth_key=1788105599-0-0-120902da418adb2c67167f7fff332c60" style="vertical-align: baseline; width: 100%;box-sizing:border-box;max-width:100% !important;" alt="图片4.png" draggable="false" data-ratio="0.6659242761692651" data-w="898"/><span style=";font-size:16px;font-family:宋体;"></span>
		</p>
		<p style=";text-align:center;" align="center">
			<span style=";font-size:16px;font-family:宋体;"><span style="font-family:宋体;">图为支援抗战一线的飞机经霍尔果斯运输入境。</span></span>
		</p>
		<p style="margin-top:0;margin-right:0;margin-bottom:0;margin-left:0;text-indent:28px;padding:0 0 0 0">
			<span style=";font-size:16px;font-family:Calibri;"><span style="font-family:宋体;">抗战期间，这条国际交通线保持高效运转，源源不断地将援华抗战物资输送到前线。</span></span>
		</p>
		<p style="margin-top:0;margin-right:0;margin-bottom:0;margin-left:0;text-indent:28px;padding:0 0 0 0">
			<span style=";font-size:16px;font-family:Calibri;"><span style="font-family:宋体;">根据新疆伊犁档案馆资料，抗日战争全面爆发后不到</span>1<span style="font-family:宋体;">年时间里，就有</span><span style="font-family:Calibri;">6000</span><span style="font-family:宋体;">多吨苏联援华军事物资经过霍尔果斯口岸从苏联进入中国并转运到内地抗战前线。</span></span>
		</p>
	</section>
</section>` },
  { id: 2, x: 14.5, y: 57.0, title: '六代国门', bgImg: '/Frame 422@2x.png', desc: '霍尔果斯历经六代国门的建设与演变，展现了中国边境口岸的沧桑巨变与辉煌发展。', stats: [{ label: '演进历程', value: '6代迭代' }, { label: '通关能力', value: '提升100倍' }], htmlContent: `<div class="custom-timeline">
  <div class="timeline-item">
    <div class="timeline-left">
      <img src="https://bexp.135editor.com/files/users/1497/14974597/202608/FUbVs4OF_F88Y.png?auth_key=1788105599-0-0-ca76b0c8cc8e88c13b3fc9ec437d00d4" />
    </div>
    <div class="timeline-divider">
      <div class="dot"></div><div class="line"></div>
    </div>
    <div class="timeline-right">
      <div class="timeline-title">第一代国门</div>
      <div class="timeline-desc">
        1978年，中国共产党第十一届三中全会在北京胜利召开，提出了把党和国家的工作重点转移到社会主义现代化建设和实行改革开放的重大战略决策上来，标志着我国进入了社会主义现代化建设的新时期。<br><br>
        <strong>改革开放的春风从首都吹到了我国西北边境地区，霍尔果斯口岸迎来了新的发展。</strong>20世纪60年代，第一代霍尔果斯国门建成投入使用。
      </div>
    </div>
  </div>

  <div class="timeline-item">
    <div class="timeline-left">
      <img src="https://bexp.135editor.com/files/users/1497/14974597/202608/pnUOVw5Q_XHOR.png?auth_key=1788105599-0-0-2f7a2618eb26b87e6945bcf50dbf0c97" />
    </div>
    <div class="timeline-divider">
      <div class="dot"></div><div class="line"></div>
    </div>
    <div class="timeline-right">
      <div class="timeline-title">第二代国门</div>
      <div class="timeline-desc">
        1992年7月，国务院批准建立霍尔果斯口岸边民互市市场，同年8月15日，市场正式开业，是当时全国最大的内陆边民贸易市场。<br><br>
        20世纪90年代初，<strong><span style="color: rgb(170, 0, 0);">霍尔果斯被誉为“西部口岸第一市”</span>。</strong>这一时期，国门迎来了第二次改造扩建。
      </div>
    </div>
  </div>

  <div class="timeline-item">
    <div class="timeline-left">
      <img src="https://bexp.135editor.com/files/users/1497/14974597/202608/fG83jj43_h2t6.png?auth_key=1788105599-0-0-6c221eeee2606d7bbf0aace4fe558dcc" />
    </div>
    <div class="timeline-divider">
      <div class="dot"></div><div class="line"></div>
    </div>
    <div class="timeline-right">
      <div class="timeline-title">第三代国门</div>
      <div class="timeline-desc">
        始建于1990年，首次加入国旗、国徽等元素，象征意义增强。1992-1998年，霍尔果斯边民互市贸易经济效益每年成倍增长，从1992年<strong>2750万元</strong>，增长到1998年的<strong>5.1112亿元</strong>，<strong>累计交易额高达19.708亿元</strong>。
      </div>
    </div>
  </div>

  <div class="timeline-item">
    <div class="timeline-left">
      <img src="https://bexp.135editor.com/files/users/1497/14974597/202608/HAtBDRGV_XCPv.png?auth_key=1788105599-0-0-cc7146423a39e665bef8b06948c647a5" />
    </div>
    <div class="timeline-divider">
      <div class="dot"></div><div class="line"></div>
    </div>
    <div class="timeline-right">
      <div class="timeline-title">第四代国门</div>
      <div class="timeline-desc">
        伴随霍尔果斯口岸对外贸易进入快速增长期，1996年，第四代国门应运而生，始建于1993年，1996年正式启用，随着口岸贸易量增长，国门规模进一步扩大，基础设施更加完善。第四代国门也是真正具有大通道意义的国门。
      </div>
    </div>
  </div>

  <div class="timeline-item">
    <div class="timeline-left">
      <img src="https://bexp.135editor.com/files/users/1497/14974597/202608/IUewvT9I_SbvA.png?auth_key=1788105599-0-0-ac96a45d3fb21eb17e544107fd411869" />
    </div>
    <div class="timeline-divider">
      <div class="dot"></div><div class="line"></div>
    </div>
    <div class="timeline-right">
      <div class="timeline-title">第五代国门</div>
      <div class="timeline-desc">
        2000年以来，贸易运输从边境互市向大宗物资进出口转变，霍尔果斯进入了新的发展时期，国门也进行了再一次的升级改造，过货通道在原有基础上进行了拓宽加高。
      </div>
    </div>
  </div>

  <div class="timeline-item">
    <div class="timeline-left">
      <img src="https://bexp.135editor.com/files/users/1497/14974597/202608/ASO5kr8y_qVMm.png?auth_key=1788105599-0-0-ed684369cdf6cfd86e327fe6b4876af7" />
    </div>
    <div class="timeline-divider">
      <div class="dot"></div><div class="line"></div>
    </div>
    <div class="timeline-right">
      <div class="timeline-title">第六代国门</div>
      <div class="timeline-desc">
        2018年9月27日，霍尔果斯（中国）-努尔饶尔（哈萨克斯坦）口岸正式开通，<strong>新口岸占地面积800余亩</strong>，分为客运、货运查验区，设计<strong>人员年通关量500万人次</strong>，<strong>货物年通关量300万吨。</strong>第六代国门随即投入使用，在“一带一路”倡议下焕发着新活力。成为“六位一体”的现代化崭新口岸。
      </div>
    </div>
  </div>

  <div class="timeline-item">
    <div class="timeline-left">
    </div>
    <div class="timeline-divider">
      <div class="dot"></div>
    </div>
    <div class="timeline-right">
      <div class="timeline-title">结语</div>
      <div class="timeline-desc">
        从2014年9月霍尔果斯市的设立，短短的20年，一座祖国西部边境的新城迅速崛起，折射出新疆的欣欣向荣，巨大发展。
      </div>
    </div>
  </div>
</div>
` },
  // { id: 3, x: 25.2, y: 52.5, title: '口岸建成', bgImg: '/Group 92@2x(2).png', desc: '口岸城市现代化建设核心示范区，具备完善的公共服务与高品质生活配套设施。', stats: [{ label: '建成区面积', value: '38.5k㎡' }, { label: '常住人口', value: '10.2万' }] },
  { id: 4, x: 29.5, y: 80.0, title: '公路口岸通关区', bgImg: '/Frame 418@2x.png', desc: '高效智能的现代公路物流通关区，集查验、通关、物流于一体，实现快速高效通关。', stats: [{ label: '日均通关车次', value: '2500+辆' }, { label: '平均通关时间', value: '15分钟' }] },
  { id: 5, x: 20.0, y: 76.5, title: '中欧班列', bgImg: '/Frame 425@2x.png', desc: '亚欧陆路交通干线核心枢纽节点，累计开行中欧班列数万列，辐射欧亚多个国家。', stats: [{ label: '开行线路', value: '75条' }, { label: '通达国家', value: '18个' }], htmlContent: `<video src="/c836787fa55544c0824c49e9091a8541_spd.mp4" controls autoplay muted style="width: 100%; margin-bottom: 10px;"></video>
<p style="font-size: 16px; font-family: 宋体; margin-bottom: 10px; line-height: 1.6; color: #333;">2013年，国家主席习近平提出了“一带一路”倡议。作为“一带一路”的重要支点，霍尔果斯的发展势头愈发迅猛。</p>
<p style="font-size: 16px; font-family: 宋体; margin-bottom: 10px; line-height: 1.6; color: #333;">2016年，霍尔果斯口岸开行中欧班列，将中国制造带向世界。自开行以来，经霍尔果斯口岸出入境中欧班列从2016年600余列次上涨到2020年的4727列，2020年过货量662万吨。</p>` },
  // { id: 6, x: 40.5, y: 48.0, title: '综合保税区大门', bgImg: '/Group 92@2x(1).png', desc: '霍尔果斯综合保税区核心进出枢纽，享受免税、保税、退税等多重国家级优惠政策。', stats: [{ label: '入驻企业', value: '450+家' }, { label: '年贸易额', value: '320亿' }] },
  { id: 8, x: 44.8, y: 41.0, title: '经济开发区', bgImg: '/Frame 426@2x.png', desc: '国家级经济开发区，推动跨境产业与新兴工业全产业链高质量发展。', stats: [{ label: '开发区面积', value: '73k㎡' }, { label: '投产项目', value: '210个' }] },
  { id: 9, x: 52.5, y: 70.5, title: '自贸区', bgImg: '/Frame 429@2x.png', desc: '中国（新疆）自由贸易试验区霍尔果斯片区。', stats: [{ label: '企业注册', value: '1200+' }, { label: '政策扶持', value: '全方位' }], htmlContent: `<section data-role="outer" class="article135" label="edit by 135editor">
	<section data-role="paragraph" class="_135editor">
		<p>
			<strong><strong>自贸区</strong></strong>
		</p>
		<p>
			2023年11月1日，中国（新疆）自由贸易试验区揭牌，霍尔果斯片区是新疆自贸试验区重要组成部分，霍尔果斯片区总面积16.58平方公里（含新疆生产建设兵团第四师1.95平方公里；含合作中心中方区2.34平方公里及霍尔果斯综合保税区3.61平方公里），四至范围东起兵团大道，西至纵一路，南起环南路北侧，北至横二路南侧。根据功能定位和产业形态，霍尔果斯片区划分为综合保税区、合作中心、铁路口岸、公路口岸和兵团四师五个功能区域。
		</p>
		<p>
			<img src="https://bexp.135editor.com/files/users/1497/14974597/202608/PZ6cwADa_wwtr.png?auth_key=1788105599-0-0-1324d1a9e3edb162dc556ba5a705fe6d" style="vertical-align: baseline; width: 100%;box-sizing:border-box;max-width:100% !important;" alt="image.png" draggable="false" data-ratio="0.5614457831325301" data-w="830"/>
		</p>
		<p>
			<img src="https://bexp.135editor.com/files/users/1497/14974597/202608/G3LkXMxy_kGnJ.png?auth_key=1788105599-0-0-8843e5f5f9f1d52ea9b14d04830d0be8" style="vertical-align: baseline; width: 100%;box-sizing:border-box;max-width:100% !important;" alt="image.png" draggable="false" data-ratio="1.121875" data-w="640"/>
		</p>
		<p>
			01区位优势显著
		</p>
		<p>
			霍尔果斯向东拥有国内14亿人口大市场，向西辐射中亚、西亚、欧洲及非洲20余亿人口。中欧班列联通“一带一路"共建国家，开行线路达80条，是我国对外开放最安全、最经济、最便捷的通道。
		</p>
		<p>
			02开放优势独特
		</p>
		<p>
			国家赋予了霍尔果斯多个开放平台，拥有国家级经济开发区、综合保税区、跨境电商综合试验区、自由贸易试验区、中哈霍尔果斯国际边境合作中心、边民互市、对外文化贸易基地等一系列开放平台。
		</p>
		<p>
			03政策优势巨大
		</p>
		<p>
			霍尔果斯片区是多区叠加的“政策洼地+制度创新高地”，如合作中心享受8000元每人每日免税政策；国家级经济开发区企业所得税“五免五减半”；自贸试验区先行先试、制度创新；综保区保税加工、保税物流、保税仓储等一系列政策优势。
		</p>
		<p>
			04口岸优势突出
		</p>
		<p>
			霍尔果斯片区是集公路、铁路、管道、航空、光缆、邮政“六位一体”的综合交通枢纽，口岸具备十大进出口资质，如水果、植物种苗、活畜、中药材、药品、整车/二手车等，数量居全国首位。
		</p>
		<p>
			<br/>
		</p>
	</section>
</section>` },
  // { id: 10, x: 57.5, y: 70.0, title: '跨境电商综试区', bgImg: '/Group 92@2x(4).png', desc: '集仓储、展示、交易、跨境配送为一体的综合性跨境电商产业孵化园区。', stats: [{ label: '单日包裹', value: '50万+' }, { label: '园区企业', value: '120家' }] },
  { id: 11, x: 65.5, y: 54.5, title: '中哈合作中心', bgImg: '/Frame 430@2x.png', desc: '全球首个跨国边境自由贸易合作区，实现中哈两国人员、车辆与货物的自由流动。', stats: [{ label: '免税额度', value: '8000元/人' }, { label: '日均客流', value: '2.5万人' }], htmlContent: `<section data-role="outer" class="article135" label="edit by 135editor">
	<section data-role="paragraph" class="_135editor">
		<p>
			<strong><span style=";font-size:16px;font-family:宋体;"><span style="font-family:宋体;"><strong>中哈合作中心</strong></span></span></strong>
		</p>
		<p >
			中哈霍尔果斯国际边境合作中心是中哈两国领导人2003年达成的国家级合作项目，是我国与其他国家建立的首个跨境经济合作区。合作区总面积5.6平方公里，其中中方区3.43平方公里，哈方区2.17平方公里，中哈两国公民和第三国公民，无需办理签证，可持护照或出入境通行证等有效证件，即可出入，实现面对面的商贸洽谈和商品交易。这里汇聚了来自世界各地的上万种商品，涉及服装配饰、鞋帽箱包、建材家居、美容护肤、食品百货等品类，汇集深圳免税、欧洲免税、意大利免税等200余家免税店，销售来自欧美、日韩、俄哈等40余个国家的免税商品，是新疆著名的跨境旅游胜地和购物天堂。
		</p>
		<p>
			<img src="https://bexp.135editor.com/files/users/1497/14974597/202608/RWHBIVjI_GzCp.png?auth_key=1788105599-0-0-a3b4edd7e0778cf1b080479c9b742832" style="vertical-align: baseline; width: 100%;box-sizing:border-box;max-width:100% !important;" alt="image.png" draggable="false" data-ratio="0.6377858002406739" data-w="831"/>
		</p>
		<p>
			<img src="https://bexp.135editor.com/files/users/1497/14974597/202608/hOedknZV_KhRs.png?auth_key=1788105599-0-0-70975f1565e5cb6e1e145c3155d8044b" style="vertical-align: baseline; width: 100%;box-sizing:border-box;max-width:100% !important;" alt="image.png" draggable="false" data-ratio="0.6630565583634176" data-w="831"/>
		</p>
		<p>
			<img src="https://bexp.135editor.com/files/users/1497/14974597/202608/aGGnrbgm_jtOO.png?auth_key=1788105599-0-0-26de7cb529c76a9e344e6ec60ee18715" style="vertical-align: baseline; width: 100%;box-sizing:border-box;max-width:100% !important;" alt="image.png" draggable="false" data-ratio="0.6650602409638554" data-w="830"/>
		</p>
		<p>
			<img src="https://bexp.135editor.com/files/users/1497/14974597/202608/K8cmNpKZ_fYOO.png?auth_key=1788105599-0-0-af0774ff5d13e3e1e38ad91b17a9d773" style="vertical-align: baseline; width: 100%;box-sizing:border-box;max-width:100% !important;" alt="image.png" draggable="false" data-ratio="0.6586248492159228" data-w="829"/>
		</p>
	</section>
</section>` },
  { id: 12, x: 73.2, y: 36.0, title: '城市天际线', bgImg: '/Frame 419@2x.png', desc: '展现现代化口岸新城向现代化高科技城市迈进的雄伟城市轮廓。', stats: [{ label: '建筑地标', value: '12座' }, { label: '绿化覆盖率', value: '42%' }], htmlContent: `<section data-role="outer" class="article135" label="edit by 135editor">
	<section data-role="paragraph" class="_135editor">
		<p>
			<strong><strong>城市天际线</strong></strong>
		</p>
		<p >
			城市是一本书翻开是故事
		</p>
		<p>
			合上是情怀
		</p>
		<p>
			十载光阴弹指过
		</p>
		<p>
			未应磨染是初心
		</p>
		<p>
			因为敢于弄潮&nbsp;所以逐浪高飞
		</p>
		<p>
			用天空视角看世界
		</p>
		<p>
			霍尔果斯美不胜收
		</p>
		<p>
			<img src="https://bexp.135editor.com/files/users/1497/14974597/202608/ppyKBYGS_Yrvb.png?auth_key=1788105599-0-0-4c41147255eadc9ae47e23abb34ae17e" style="vertical-align: baseline; width: 100%;box-sizing:border-box;max-width:100% !important;" alt="image.png" draggable="false" data-ratio="0.5625" data-w="800"/>
		</p>
		<p>
			每一盏灯
		</p>
		<p>
			都在点亮千家万户的幸福
		</p>
		<p>
			<img src="https://bexp.135editor.com/files/users/1497/14974597/202608/C9GO3DDS_Ty9A.png?auth_key=1788105599-0-0-8846cf872067b4987bfe62e5a1149007" style="vertical-align:baseline;" alt="image.png" draggable="false" data-ratio="0.5631067961165048" data-w="824"/>
		</p>
		<p style="margin-top:0;margin-right:0;margin-bottom:0;padding:0 0 0 0">
			<span style=";font-size:16px;font-family:宋体;"><span style="font-family:宋体;">人来人往</span></span>
		</p>
		<p style="margin-top:0;margin-right:0;margin-bottom:0;padding:0 0 0 0">
			<span style=";font-size:16px;font-family:宋体;"><span style="font-family:宋体;">承载着奔赴远方的希冀</span></span>
		</p>
		<p style="margin-top:0;margin-right:0;margin-bottom:0;padding:0 0 0 0">
			<span style=";font-size:16px;font-family:宋体;"><span style="font-family:宋体;">以及归家的喜悦</span></span>
		</p>
		<p>
			<img src="https://bexp.135editor.com/files/users/1497/14974597/202608/NHhs5zwZ_vb2A.png?auth_key=1788105599-0-0-f3f44ae95941cda7dfe2af4216858d01" style="vertical-align: baseline; width: 100%;box-sizing:border-box;max-width:100% !important;" alt="image.png" draggable="false" data-ratio="0.75" data-w="760"/>
		</p>
		<p style="margin-top:0;margin-right:0;margin-bottom:0;padding:0 0 0 0">
			<span style=";font-size:16px;font-family:宋体;"><span style="font-family:宋体;">每一个普通的日子</span></span>
		</p>
		<p style="margin-top:0;margin-right:0;margin-bottom:0;padding:0 0 0 0">
			<span style=";font-size:16px;font-family:宋体;"><span style="font-family:宋体;">都在美好中奔赴美好</span></span>
		</p>
		<p>
			<img src="https://bexp.135editor.com/files/users/1497/14974597/202608/XFcQTcs8_kUFc.png?auth_key=1788105599-0-0-912ed22102e93802646ee466f47656d7" style="vertical-align:baseline;" alt="image.png" draggable="false" data-ratio="0.5626506024096386" data-w="830"/>
		</p>
	</section>
	<section class="_135editor" data-role="paragraph">
		<p style="margin-top:0;margin-right:0;margin-bottom:0;padding:0 0 0 0;text-align:left;" align="left">
			<span style=";font-size:16px;font-family:宋体;"><span style="font-family:宋体;">每个人内心都有一场久违的约定</span></span>
		</p>
		<p style="margin-top:0;margin-right:0;margin-bottom:0;padding:0 0 0 0;text-align:left;" align="left">
			<span style=";font-size:16px;font-family:宋体;"><span style="font-family:宋体;">不问西东</span> <span style="font-family:宋体;">感受真意</span></span>
		</p>
		<p>
			<img src="https://bexp.135editor.com/files/users/1497/14974597/202608/rDpr99ss_dJNq.png?auth_key=1788105599-0-0-6191dd2f320211ef640fdc5274015b9e" style="vertical-align:baseline;" alt="image.png" draggable="false" data-ratio="0.5631067961165048" data-w="824"/>
		</p>
		<p style="margin-top:0;margin-right:0;margin-bottom:0;padding:0 0 0 0;text-align:left;" align="left">
			<span style=";font-size:16px;font-family:宋体;"><span style="font-family:宋体;">总有一条路</span></span>
		</p>
		<p style="margin-top:0;margin-right:0;margin-bottom:0;padding:0 0 0 0;text-align:left;" align="left">
			<span style=";font-size:16px;font-family:宋体;"><span style="font-family:宋体;">见证着城市的发展记录着城市的繁荣</span></span>
		</p>
		<p>
			<img src="https://bexp.135editor.com/files/users/1497/14974597/202608/WZ2pbXXU_EK2Y.png?auth_key=1788105599-0-0-18fcde29f35c87be78000158b148a1e1" style="vertical-align:baseline;" alt="image.png" draggable="false" data-ratio="0.5631768953068592" data-w="831"/>
		</p>
		<p style="margin-top:0;margin-right:0;margin-bottom:0;padding:0 0 0 0;text-align:left;" align="left">
			<span style=";font-size:16px;font-family:宋体;"><span style="font-family:宋体;">山水交织</span> <span style="font-family:宋体;">刚柔冲撞</span></span>
		</p>
		<p style="margin-top:0;margin-right:0;margin-bottom:0;padding:0 0 0 0;text-align:left;" align="left">
			<span style=";font-size:16px;font-family:宋体;"><span style="font-family:宋体;">五味调和</span> <span style="font-family:宋体;">甘之如饴</span></span>
		</p>
		<p>
			<img src="https://bexp.135editor.com/files/users/1497/14974597/202608/RamVh6tO_WsqK.png?auth_key=1788105599-0-0-73651144ec239bb4236628c1f0a434b9" style="vertical-align: baseline; width: 100%;box-sizing:border-box;max-width:100% !important;" alt="image.png" draggable="false" data-ratio="0.75" data-w="824"/>
		</p>
		<p style="margin-top:0;margin-right:0;margin-bottom:0;padding:0 0 0 0;text-align:left;" align="left">
			<span style=";font-size:16px;font-family:宋体;"><span style="font-family:宋体;">生活在这里</span></span>
		</p>
		<p style="margin-top:0;margin-right:0;margin-bottom:0;padding:0 0 0 0;text-align:left;" align="left">
			<span style=";font-size:16px;font-family:宋体;"><span style="font-family:宋体;">每个人都是见证者</span><span style="font-family:宋体;">&nbsp;也是受益者</span></span>
		</p>
		<p style="margin-top:0;margin-right:0;margin-bottom:0;padding:0 0 0 0;text-align:left;" align="left">
			<span style=";font-size:16px;font-family:宋体;"><span style="font-family:宋体;">在霍尔果斯</span></span>
		</p>
		<p style="margin-top:0;margin-right:0;margin-bottom:0;padding:0 0 0 0;text-align:left;" align="left">
			<span style=";font-size:16px;font-family:宋体;"><span style="font-family:宋体;">你能听到城市生长拔节的声音</span></span>
		</p>
	</section>
</section>` },
  { id: 13, x: 90.0, y: 67.5, title: '智慧治理指挥中心', bgImg: '/Frame 420@2x.png', desc: '依托大屏监控与全域感知系统，实现口岸人流、物流、车流及城市的精细化全天候运营管理。', stats: [{ label: '全域感知设备', value: '12000+' }, { label: '事件处置率', value: '99.8%' }], htmlContent: `<section data-role="outer" class="article135" label="edit by 135editor"><section data-role="paragraph" class="_135editor"><p>智慧治理指挥中心</p></section><p>“智慧治理指挥中心”是霍尔果斯统筹城市治理各条战线的数字化集合体。它不是一个独立的实体机构，而是汇聚城市管理、政务服务、基层治理、社会治安、应急安全等多部门力量，各司其职、协同联动、数据互通，共同构成城市治理的“神经中枢”。</p><p>城市管理部门依托智慧城管平台，构建“信息收集、案件立案、任务派遣、处理处置、结果反馈、核查结案、综合评价”七环节闭环处置体系，城市管理问题一网统管、全程可溯。平台上线以来，累计受理处置城市各类问题4183件，办结案件3858件，结案率达99.38%，实现城市问题精准发现、快速处置、常态管控。</p><p style="text-align:center;"><img src="https://bexp.135editor.com/files/users/1497/14974597/202608/t5xCV4xj_gyrU.png?auth_key=1788710399-0-0-aa5af941601a51b1b9fe14a3b4cb116a" style="vertical-align: baseline; width: 100%;box-sizing:border-box;" alt="微信图片_2026-08-29_193614_878.png" _src="https://bexp.135editor.com/files/users/1497/14974597/202608/t5xCV4xj_gyrU.png?auth_key=1788710399-0-0-aa5af941601a51b1b9fe14a3b4cb116a"/></p><p style="text-align:center;"><img src="https://bexp.135editor.com/files/users/1497/14974597/202608/eqtdCjNj_OELV.jpg?auth_key=1788710399-0-0-eceab862f189f4c671b6c439d6e3a0be" style="vertical-align: baseline; width: 100%;box-sizing:border-box;" alt="城市小管家业务流程闭环图（可编辑源文件） (1).jpg" _src="https://bexp.135editor.com/files/users/1497/14974597/202608/eqtdCjNj_OELV.jpg?auth_key=1788710399-0-0-eceab862f189f4c671b6c439d6e3a0be"/></p><p>政务服务部门推进“一网通办”，持续压缩办事时限、提升服务效能；政法综治部门坚持和发展新时代“枫桥经验”，依托网格化体系推动矛盾纠纷源头化解；公安部门构建立体化治安防控网络，织密口岸与城市安全防线；应急管理部门强化安全生产监管和应急指挥调度，提升突发事件处置能力。</p><p>各条线业务汇聚于统一的数字底座，形成“城市运行一网统管、政务服务一网通办、基层治理一张网、城市安全一盘棋”的现代化治理体系，为精致口岸城市建设提供坚实支撑。</p><p><br/></p></section>` },
  { id: 14, x: 77.0, y: 89.0, title: '产业园区', bgImg: '/Frame 427@2x.png', desc: '涵盖先进制造、农产品深加工、高端装备制造的跨境优势产业集群。', stats: [{ label: '产值规模', value: '180亿元' }, { label: '科技企业', value: '68家' }] },
  { id: 15, x: 95.5, y: 82.0, title: '未来规划蓝图', bgImg: '/Frame 428@2x.png', desc: '立足亚欧黄金通道，规划打造全球顶级的绿色、智能、人文、包容的国际一流智慧口岸。', stats: [{ label: '规划面积', value: '120k㎡' }, { label: '远期贸易额', value: '1000亿' }], htmlContent: `<section data-role="outer" class="article135" label="edit by 135editor"><section data-role="paragraph" class="_135editor"><p>未来规划蓝图</p></section><p>未来规划蓝图描绘霍尔果斯从“数字化”迈向“智慧化”的演进路径。霍尔果斯将深入推进智慧城市建设，持续完善智慧城管系统平台，构建全要素“数字孪生城市”一网通管体系，推动城市治理向“感知全域、智能研判、精准施策”升级。</p><p><img src="https://bexp.135editor.com/files/users/1497/14974597/202608/mRbZBKKx_ydzX.png?auth_key=1788710399-0-0-1eeec417fc43b356e9482481e9eb3fb8" style="vertical-align:baseline;" alt="未来规划蓝图_远景规划图1.png" _src="https://bexp.135editor.com/files/users/1497/14974597/202608/mRbZBKKx_ydzX.png?auth_key=1788710399-0-0-1eeec417fc43b356e9482481e9eb3fb8"/><img src="https://bexp.135editor.com/files/users/1497/14974597/202608/mySVNN3L_fdVB.png?auth_key=1788710399-0-0-ea700912e132ab93392864e6830b2ecd" style="vertical-align:baseline;" alt="未来规划蓝图_分期路线图1.png" _src="https://bexp.135editor.com/files/users/1497/14974597/202608/mySVNN3L_fdVB.png?auth_key=1788710399-0-0-ea700912e132ab93392864e6830b2ecd"/></p><p>以“云港·霍数通”智慧口岸综合服务平台为支撑，整合政务办理、口岸监管等核心业务，实现“一点接入、数据共享、一站服务”，打造智慧通关、智慧物流、智慧文旅、智慧社区协同发展的现代化城市。</p><p>聚焦城市运行重点领域，加快智慧井盖、智慧路灯、智慧环卫、智慧管网、智慧燃气、智慧水务和城市运行监测等应用落地，推动城市管理全要素数字化、全流程智能化。未来，霍尔果斯将全面融入数字新疆“1652”总体架构，以数据要素驱动城市治理现代化，为打造市场化、法治化、国际化一流营商环境提供坚实数字底座。</p></section>` }
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
  padding:0.23rem 0.3rem ;
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
  top: 2.2rem;
  left: 1.9rem;
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
  height: 1.2rem;
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
  background: rgba(0, 0, 0, 0.1);
  z-index: 99999999;
}

.marker-modal {
  width: 8rem;
  background: rgba(255, 252, 247, 0.75);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border: 0.02rem solid rgba(212, 175, 55, 0.6);
  border-radius: 0.16rem;
  padding: 0.24rem;
  box-shadow: 0 0.12rem 0.32rem rgba(0, 0, 0, 0.15);
  position: absolute;
  top: 50%;
  left: 0.5rem;
  height:calc(100% - .6rem);
  z-index: 9999;
  transform: translateY(-50%);
  animation: slideInLeft 0.4s cubic-bezier(0.25, 0.8, 0.25, 1);
}

@keyframes slideInLeft {
  from { opacity: 0; transform: translate(-2rem, -50%); }
  to { opacity: 1; transform: translate(0, -50%); }
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

.modal-html-content {
  overflow-y: auto;
  max-height: calc(100% - 0.8rem);
  font-size: 0.14rem;
  color: #333;
  line-height: 1.6;
}

.modal-html-content p {
  margin-bottom: 0.1rem;
}

.modal-html-content img {
  max-width: 100%;
  height: auto;
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
  height: 0.6rem;
  display: flex;
  align-items: center;
  justify-content: space-around;
  padding: 0 0.2rem;
  box-sizing: border-box;
  z-index: 100;
  position: absolute;
  
  background: radial-gradient( 277.74% 169.73% at 190.57% -18.33%, rgba(0,0,0,0.8) 0%, rgba(102,102,102,0) 100%), rgba(0,0,0,0.12);
  bottom: .23rem;
  left: 50%;
  transform: translateX(-50%);
  width: 100%;
  overflow: hidden;
  white-space: nowrap;
}

.footer-nav-cell {
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  width: 6rem;
  position: relative;
  transition: all 0.3s ease;
}

.footer-nav-cell:last-child {
  border-right: none;
}

.footer-nav-cell.active,
.footer-nav-cell:hover {
  background: linear-gradient(180deg, #c49438 0%, #855f19 100%);
}
.flexdvv{
  display: flex;
  width: 10rem;
  height: 100%;

}
.nav-text {
  font-family: "STKaiti", "KaiTi", serif;
  font-size: 0.2rem;
  font-weight: bold;
  color: #f7eedb;
  letter-spacing: 0.04rem;
  text-shadow: 0 0.02rem 0.04rem rgba(0, 0, 0, 0.6);
}

.right-popup {
  position: absolute;
  top: 0.8rem;
  right: 0.6rem;
  bottom: 0.8rem;
  width: 8rem; /* 大约占比 */
  z-index: 200000;
  display: flex;
  justify-content: flex-end;
  pointer-events: none;
}

.right-popup-inner {
  position: relative;
  width: 100%;
  height: 100%;
  pointer-events: auto;
}

.popup-bg {
  width: 100%;
  height: 100%;
  position: absolute;
  top: 0;
  left: 0;
  z-index: 1;
  opacity: .8;
}

.popup-close {
  position: absolute;
  top: -0rem;
  right: -0.1rem;
  width: 0.3rem;
  height: 0.3rem;
  z-index: 10;
  cursor: pointer;
  transition: transform 0.3s;
}

.popup-close:hover {
  transform: scale(1.1) rotate(90deg);
}

.popup-title {
  position: absolute;
  top: 0.05rem;
  left: 50%;
  transform: translateX(-50%);
  z-index: 5;
  font-size: 0.22rem;
  font-weight: bold;
  color: #FFF5CB;
  letter-spacing: 0.06rem;
  font-family: "STKaiti", "KaiTi", serif;
}

.popup-content {
  position: absolute;
  top: 0.6rem;
  left: 0.3rem;
  right: 0.3rem;
  bottom: 0.3rem;
  z-index: 2;
  /* background: rgba(255, 0, 0, 0.1); 占位测试可取消注释 */
}

/* 弹出框过渡动画 */
.slide-right-enter-active,
.slide-right-leave-active {
  transition: all 0.4s cubic-bezier(0.25, 0.8, 0.25, 1);
}
.slide-right-enter-from,
.slide-right-leave-to {
  opacity: 0;
  transform: translateX(1rem);
}

</style>

<style>
.custom-timeline {
  display: flex;
  flex-direction: column;
  padding: 10px 0;
}
.custom-timeline .timeline-item {
  display: flex;
  align-items: stretch;
  margin-bottom: 0px;
}
.custom-timeline .timeline-left {
  width: 140px;
  flex-shrink: 0;
  display: flex;
  align-items: flex-start;
  justify-content: flex-end;
  padding-top: 2px;
}
.custom-timeline .timeline-left img {
  width: 100%;
  border-radius: 6px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.15);
}
.custom-timeline .timeline-divider {
  width: 36px;
  display: flex;
  flex-direction: column;
  align-items: center;
  position: relative;
  flex-shrink: 0;
}
.custom-timeline .timeline-divider .dot {
  width: 12px;
  height: 12px;
  border-radius: 50%;
  background-color: #fff;
  border: 3px solid #e65c00;
  margin-top: 6px;
  z-index: 2;
  box-shadow: 0 0 0 2px rgba(230, 92, 0, 0.2);
}
.custom-timeline .timeline-divider .line {
  position: absolute;
  top: 22px;
  bottom: -6px;
  width: 2px;
  background-color: #e65c00;
  opacity: 0.4;
  z-index: 1;
}
.custom-timeline .timeline-item:last-child .timeline-divider .line {
  display: none;
}
.custom-timeline .timeline-right {
  flex: 1;
  padding-bottom: 25px;
}
.custom-timeline .timeline-title {
  font-size: 18px;
  font-weight: bold;
  color: #a00;
  margin-bottom: 6px;
  font-family: "STKaiti", "KaiTi", serif;
}
.custom-timeline .timeline-desc {
  font-size: 14px;
  color: #443322;
  line-height: 1.6;
}
.custom-timeline .timeline-desc strong {
  color: #a00;
}
</style>
