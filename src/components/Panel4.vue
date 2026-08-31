<template>
  <div class="grid-container">
    <div class="grid-item" v-for="item in zhibiao" :key="item.title">
      <div class="item-title">
        <img src="/Frame 119@2x.png" class="title-bg" alt="" draggable="false" />
        <span class="title-text">{{ item.title }}</span>
      </div>
      <div class="item-content">
        <div class="content-wrapper">
          <div class="drlj">
            <div>当日累计</div>
            <img src="/Slice 3@2x.png" class="content-img" alt="" draggable="false" />
            <div style="font-size: .2rem; color:#fff;font-weight: bold;">51.7</div>
          </div>
          <div style="color: #0DC923;">
            <span>上涨</span>
            <span> 3.2%</span>
          </div>
        </div>

      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
const zhibiao = ref([
  { title: '建设用地供应面积', content: '/Slice 3@2x.png' },
  { title: '不动产登记宗数', content: '/Slice 3@2x.png' },
  { title: '已开工土地项目数', content: '/Slice 3@2x.png' },
  { title: '基本农田保护面积', content: '/Slice 3@2x.png' },
  { title: '文物保护单位数', content: '/Slice 3@2x.png' },
  { title: '文化事业季报数据', content: '/Slice 3@2x.png' },
  { title: '体育场地总数', content: '/Slice 3@2x.png' },
  { title: '建设用地供应面积', content: '/Slice 3@2x.png' },
  { title: '城市建成区不动产活跃度', content: '/Slice 3@2x.png' }
])
</script>

<style scoped>
.grid-container {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-template-rows: repeat(3, 1fr);
  gap: 0.15rem;
  width: 100%;
  height: 100%;
}

.grid-item {
  display: flex;
  flex-direction: column;
  position: relative;
  overflow: hidden;
  border: 1px solid;
  border-image: linear-gradient(to bottom, #ffdd8ea5, #ffdd8e32) 1;
}

.item-title {
  position: relative;
  height: 0.3rem;
  display: flex;
  align-items: center;
  justify-content: center;
}

.title-bg {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: fill;
  z-index: 1;
}

.content-wrapper {
  position: relative;
  font-size: 0.1rem;
  display: flex;
  justify-content: space-around;
  align-items: flex-end;
  
}

.content-wrapper img {
  position: absolute;
  top: 0rem;
  left: 0rem;
  width: 1.4rem;

}

.title-text {
  position: relative;
  z-index: 2;
  color: #FFDE8D;
  font-size: 0.12rem;
  font-weight: bold;


}

.item-content {
  flex: 1;
  display: flex;
  align-items: center;

  padding: 0.1rem;
  color: #FFDE8D;
}
.drlj{
  width: 1.5rem;
  text-align: center;
  padding-left: .3rem;
}

</style>
