<template>
  <div class="governance-box">
    <!-- Row 1 -->
    <div class="gov-item">
      <div class="gov-title">当月案件处置率</div>
      <div class="gov-content">
        <div class="gov-value">98.5<span class="unit">%</span> <span class="trend up">▲</span></div>
        <div class="gov-chart circle-chart" style="--percent: 98.5%;"></div>
      </div>
    </div>
    <div class="gov-item">
      <div class="gov-title">平均办结时长</div>
      <div class="gov-content">
        <div class="gov-value">4.2<span class="unit">小时</span> <span class="trend down">▼</span></div>
        <div class="gov-chart">
          <svg viewBox="0 0 100 30" class="spark-line"><polyline points="0,25 20,20 40,28 60,15 80,10 100,5" /></svg>
        </div>
      </div>
    </div>
    <div class="gov-item">
      <div class="gov-title">政务服务办结率</div>
      <div class="gov-content">
        <div class="gov-value">99.1<span class="unit">%</span> <span class="trend up">▲</span></div>
        <div class="gov-chart circle-chart" style="--percent: 99.1%;"></div>
      </div>
    </div>
    <div class="gov-item">
      <div class="gov-title">群众满意度</div>
      <div class="gov-content">
        <div class="gov-value">99.5<span class="unit">%</span> <span class="trend up">▲</span></div>
        <div class="gov-chart">
          <svg viewBox="0 0 100 30" class="spark-line"><polyline points="0,20 20,22 40,15 60,10 80,8 100,2" /></svg>
        </div>
      </div>
    </div>
    
    <!-- Row 2 -->
    <div class="gov-item">
      <div class="gov-title">在校学生数</div>
      <div class="gov-content">
        <div class="gov-value">1.5<span class="unit">万</span> <span class="trend up">▲</span></div>
        <div class="gov-chart pie-chart" style="background: conic-gradient(#4ade80 0% 40%, #fbbf24 40% 70%, #60a5fa 70% 100%);"></div>
      </div>
    </div>
    <div class="gov-item">
      <div class="gov-title">医疗床位总数</div>
      <div class="gov-content" style="flex-direction: column; align-items: flex-start; justify-content: center;">
        <div class="gov-value">3,200<span class="unit">张</span> <span class="trend up">▲</span></div>
        <div class="gov-sub">医院 15家 | 每千人 8.5张</div>
      </div>
    </div>
    <div class="gov-item">
      <div class="gov-title">空气质量优良率</div>
      <div class="gov-content">
        <div class="gov-value">95.0<span class="unit">%</span> <span class="trend up">▲</span></div>
        <div class="gov-chart circle-chart" style="--percent: 95%;"></div>
      </div>
    </div>
    <div class="gov-item">
      <div class="gov-title">气象灾害预警</div>
      <div class="gov-content">
        <div class="gov-value">12<span class="unit">次</span></div>
        <div class="gov-chart pie-chart" style="background: conic-gradient(#60a5fa 0% 25%, #fbbf24 25% 50%, #f97316 50% 75%, #ef4444 75% 100%); margin-left: 5px;"></div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.governance-box {
  background: rgba(30, 24, 15, 0.75);
  border: 1px solid rgba(212, 175, 55, 0.6);
  border-radius: 0.08rem;
  padding: 0.16rem;
  width: 7rem;
  backdrop-filter: blur(4px);
  position: absolute;
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  grid-template-rows: repeat(2, 1fr);
  gap: 0.16rem;
}

.governance-box::before, .governance-box::after {
  content: '';
  position: absolute;
  width: 0.1rem;
  height: 0.1rem;
  border: 2px solid rgba(212, 175, 55, 0.6);
}
.governance-box::before {
  top: -1px; left: -1px;
  border-right: none; border-bottom: none;
}
.governance-box::after {
  bottom: -1px; right: -1px;
  border-left: none; border-top: none;
}

.gov-item {
  background: rgba(212, 175, 55, 0.05);
  border-radius: 0.08rem;
  padding: 0.12rem;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.gov-title {
  color: #e0c896;
  font-size: 0.15rem;
  margin-bottom: 0.08rem;
}

.gov-content {
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 0.4rem;
}

.gov-value {
  color: #ffffff;
  font-size: 0.2rem;
  font-weight: bold;
  display: flex;
  align-items: baseline;
  white-space: nowrap;
}

.unit {
  font-size: 0.15rem;
  color: #94a3b8;
  font-weight: normal;
  margin-left: 0.02rem;
}

.trend {
  font-size: 0.12rem;
  margin-left: 0.06rem;
}
.trend.up { color: #4ade80; }
.trend.down { color: #4ade80; } /* green means good (duration goes down) */

.gov-sub {
  color: #e0c896;
  font-size: 0.12rem;
  margin-top: 0.04rem;
  white-space: nowrap;
}

.gov-chart {
  width: 0.4rem;
  height: 0.4rem;
  display: flex;
  align-items: center;
  justify-content: center;
}

.circle-chart {
  border-radius: 50%;
  background: conic-gradient(#eab308 var(--percent), rgba(212, 175, 55, 0.2) 0);
  position: relative;
}
.circle-chart::after {
  content: '';
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 0.3rem;
  height: 0.3rem;
  background: #1f1b14;
  border-radius: 50%;
}

.pie-chart {
  border-radius: 50%;
}

.spark-line {
  width: 100%;
  height: 100%;
  overflow: visible;
}
.spark-line polyline {
  fill: none;
  stroke: #eab308;
  stroke-width: 2;
  stroke-linecap: round;
  stroke-linejoin: round;
}
</style>
