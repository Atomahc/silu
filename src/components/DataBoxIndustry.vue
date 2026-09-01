<template>
  <div class="data-box-container">
    <div class="data-grid">
      <div class="data-item">
        <div class="icon-wrap">
          <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M12 22C17.5228 22 22 17.5228 22 12C22 6.47715 17.5228 2 12 2C6.47715 2 2 6.47715 2 12C2 17.5228 6.47715 22 12 22Z" stroke="#4ade80" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M12 6V12L16 14" stroke="#4ade80" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
        </div>
        <div class="text-content">
          <div class="label">新签投资项目</div>
          <div class="value">24 <span class="unit">个</span></div>
        </div>
      </div>
      <div class="data-item">
        <div class="icon-wrap">
          <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M12 22C17.5228 22 22 17.5228 22 12C22 6.47715 17.5228 2 12 2C6.47715 2 2 6.47715 2 12C2 17.5228 6.47715 22 12 22Z" stroke="#4ade80" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M12 6V12L16 14" stroke="#4ade80" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
        </div>
        <div class="text-content">
          <div class="label">同比增长</div>
          <div class="value">71.42 <span class="unit">%</span></div>
        </div>
      </div>
      <div class="data-item">
        <div class="icon-wrap">
          <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M12 22C17.5228 22 22 17.5228 22 12C22 6.47715 17.5228 2 12 2C6.47715 2 2 6.47715 2 12C2 17.5228 6.47715 22 12 22Z" stroke="#eab308" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M12 6V12L16 14" stroke="#eab308" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
        </div>
        <div class="text-content">
          <div class="label">协议总投资</div>
          <div class="value">46.2 <span class="unit">亿元</span></div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.data-box-container {
  background: rgba(30, 24, 15, 0.75);
  border:  1px solid rgba(212, 175, 55, 0.6);
  border-radius: 0.08rem;
  padding: 0.1rem;
  width: auto;
  min-width: 2rem;
  backdrop-filter: blur(4px);
  position: absolute;
}
.data-box-container::before, .data-box-container::after {
  content: '';
  position: absolute;
  width: 0.1rem;
  height: 0.1rem;
  border: 2px solid rgba(212, 175, 55, 0.6);
}
.data-box-container::before {
  top: -1px; left: -1px;
  border-right: none; border-bottom: none;
}
.data-box-container::after {
  bottom: -1px; right: -1px;
  border-left: none; border-top: none;
}

.data-grid {
  display: flex;
  flex-direction: column;
  gap: 0.12rem;
  position: relative;
}

.data-item {
  display: flex;
  align-items: center;
  padding: 0.05rem;
}

.icon-wrap {
  width: 0.3rem;
  height: 0.3rem;
  margin-right: 0.1rem;
  flex-shrink: 0;
  display: flex;
  align-items: center;
  justify-content: center;
}
.icon-wrap svg {
  width: 100%;
  height: 100%;
  display: block;
}

.label {
  color: #e0c896;
  font-size: 0.15rem;
  margin-bottom: 4px;
}

.value {
  color: #ffffff;
  font-size: 0.2rem;
  font-weight: bold;
  line-height: 1;
}

.unit {
  font-size: 0.15rem;
  color: #94a3b8;
  font-weight: normal;
}
</style>
