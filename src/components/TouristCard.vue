<template>
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
</template>

<style scoped>
.tourist-card {
  position: absolute;
  z-index: 100;
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
</style>
