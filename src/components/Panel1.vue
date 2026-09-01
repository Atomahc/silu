<template>
  <div class="grid-container">
    <div class="grid-item" v-for="item in zhibiao" :key="item.title">
      <div class="item-title">
        <img src="./Frame 119@2x.png" class="title-bg" alt="" draggable="false" />
        <span class="title-text">{{ item.title }}</span>
      </div>
      <div class="item-content">
        <div class="content-wrapper">
          <div class="drlj">
            <div>当日累计</div>
            <img src="./Slice 3@2x.png" class="content-img" alt="" draggable="false" />
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
  { title: '地区生产总值', content: '/Slice 3@2x.png' },
  { title: '规上工业增加值增速', content: '/Slice 3@2x.png' },
  { title: '固定资产投资额', content: '/Slice 3@2x.png' },
  { title: '社会消费品零售额', content: '/Slice 3@2x.png' },
  { title: '家庭农场数量', content: '/Slice 3@2x.png' },
  { title: '农业龙头企业数', content: '/Slice 3@2x.png' },
  { title: 'A级景区游客接待量', content: '/Slice 3@2x.png' },
  { title: '有效发明专利数', content: '/Slice 3@2x.png' },
  { title: '建筑工程施工许可证量', content: '/Slice 3@2x.png' }
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
