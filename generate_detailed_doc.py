# -*- coding: utf-8 -*-

content = """**霍尔果斯市“数字名片”系统**

**详细设计说明书**

V1.0

|     |     |     |     |
| --- | --- | --- | --- |
| 文档编号： | HG-CSDM-2026-02 | 项目名称： | 霍尔果斯市“数字名片”系统 |
| 编 写： | 系统架构组 | 编写日期： | 2026-09-18 |
| 审 核： |     | 审核日期： |     |
| 批 准： |     | 批准日期： |     |

新疆坤智讯科云科技有限公司

**修订状况**

|     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- |
| 序号  | 修订内容简述 | 修订日期 | 修订前版本号 | 修订人 | 批准人 |
| 1   | 根据概要设计说明书及当前项目（Vue 3 + Vite）具体代码实现，编写详细设计说明书 | 2026-09-18 | V1.0 | 系统架构组 | 项目主管 |

**1. 引言**

**1.1 编写目的**

本文档旨在对霍尔果斯市“数字名片”系统进行详细设计说明。基于《霍尔果斯数字名片-概要设计说明书.md》中确定的“插画长卷叙事 + 6大分类指标分析”架构，结合项目实际代码实现（前端框架基于 Vue 3 + Vite 搭建），详细描述系统的组件划分、状态管理、核心交互逻辑、动画实现方案及数据渲染机制。本说明书是前端开发、代码维护及后续迭代的直接参考依据。

**1.2 项目背景**

本项目旨在构建“一中枢、一门户”的城市级数字底座，数字城市名片作为一期项目的对外展示窗口，以可横向滚动的“数字城市长卷”为核心展现形式。由于需求调整，已取消原三维CIM方案，采用纯前端 H5 Canvas 及 CSS Transform 技术实现流畅的长卷展示与热点数据交互。

**1.3 术语与定义**

*   **Vue 3 Composition API**：Vue 3 的核心 API，采用 `<script setup>` 语法进行逻辑组织。
*   **长卷容器 (Scroll Container)**：通过 CSS `overflow-x: auto` 与自定义拖拽逻辑实现的横向插画展示区。
*   **动态组件 (Dynamic Component)**：使用 `<component :is="...">` 根据状态动态渲染的面板模块。

**1.4 参考资料**

*   《霍尔果斯“数字链计划”一期项目__需求规格说明书_20260831》
*   《霍尔果斯数字名片-概要设计说明书》

**2. 系统前端架构设计**

**2.1 项目目录与技术栈**

本项目位于 `/data/data/com.termux/files/home/porject/silu`，采用现代前端工程化工具 Vite 构建：
*   **核心框架**：Vue 3 (`^3.4.0`)，全部采用 `<script setup>` 组合式 API。
*   **构建工具**：Vite (`^5.0.0`)，提供极速的模块热更新（HMR）。
*   **组件结构**：`src/App.vue` 作为根容器组件，按功能拆分为业务组件存放在 `src/components/` 目录下（如 `DataBox.vue`, `Panel0.vue` 等）。独立图文 HTML 内容存放在 `src/html/` 中，通过 `?raw` 方式导入。

**2.2 组件树结构**

```text
App.vue (根容器)
 ├─ Header (顶部状态栏，包含时间与天气)
 ├─ ScrollHandle (左右滚动控制轴柄)
 ├─ ScrollContent (长卷核心区域)
 │   └─ PanoramicContainer
 │       ├─ panoramic-bg (长卷底层背景图)
 │       ├─ DataBox / DataBoxIndustry / DataBoxGovernance (悬浮数据小面板)
 │       └─ MapMarker (建筑热点标注组件，列表渲染)
 ├─ MarkerModal (热点详情弹窗)
 ├─ RightPopup (右侧指标浮层)
 │   └─ Dynamic Component -> Panel0 ~ Panel4 (六大分类指标数据图表)
 └─ Footer (底部分类导航栏)
```

**3. 核心功能详细设计**

**3.1 长卷物理滚动与拖拽实现**

长卷的横向浏览是系统的核心交互。
*   **轴柄悬停滚动**：通过 `startScroll` 和 `stopScroll` 方法，利用 `requestAnimationFrame` 以 `15px/帧` 的速度动态修改 `scrollContainer.value.scrollLeft`。
*   **鼠标拖拽**：在 `scroll-content` 容器上绑定 `@mousedown="startDrag"`，结合全局的 `mousemove` 和 `mouseup` 事件，计算水平偏移量（`(e.pageX - startX) * 1.5` 的摩擦系数），更新滚动条位置。拖拽时添加 `.is-dragging` 类，禁用内部元素的指针事件（`pointer-events: none`）以防止误触热点。

**3.2 热点交互与数据模型 (MapMarker)**

热点数据在 `App.vue` 中通过 `const markers = ref([...])` 静态定义或初始化赋值。
*   **数据结构**：
    ```javascript
    { 
      id: 1, 
      x: 5.8, y: 50.5, // 相对长卷的百分比坐标
      title: '驿站溯源', 
      subTitle: '', 
      bgImg: './laby1.png', // 背景底图
      desc: '...', 
      stats: [{ label: '建驿历史', value: '1000+年' }], 
      htmlContent: marker1Html // 通过 ?raw 导入的静态富文本
    }
    ```
*   **交互逻辑**：热点采用绝对定位 `left: marker.x + '%'`, `top: marker.y + '%'`。点击热点后，将 `activeMarker` 置为当前对象，界面渲染 `<div class="marker-modal">`，若存在 `htmlContent` 则通过 `v-html` 渲染富文本内容，否则渲染 `desc` 与 `stats` 列表。
*   **微光浮动动画**：为 `.map-marker` 添加 `@keyframes floatUpDown` 实现 2.5s 周期的平滑上下浮动，`hover` 时停止浮动并放大 `scale(1.18)`，提升 `z-index`。

**3.3 右侧分类指标浮层 (Right Popup)**

底部分类导航（数字党建、数字政务等）点击后唤起右侧指标面板。
*   **状态控制**：通过 `currentNavIndex` (ref) 记录当前激活的分类索引（0-4对应驿站溯源、口岸脉动等5个主题场景，与需求侧分类存在映射关联）。
*   **动态渲染**：使用 `<component :is="panels[currentNavIndex]">`，根据 `panels = [Panel0, Panel1, Panel2, Panel3, Panel4]` 数组动态加载具体的 ECharts 图表组件。
*   **出场动画**：外层包裹 `<transition name="slide-right">`，在 CSS 中定义 `.slide-right-enter-active` 等过渡类，实现 300ms 平滑滑出效果。

**3.4 开场进场动画序列**

系统启动时，具有强烈的视觉仪式感：
*   通过 `triggerScrollAnimation` 方法，控制 `isOpening` 和 `isOpened` 状态变量。
*   **轴柄展开**：`@keyframes handleLeftExpand` 与 `handleRightExpand`，在 3.6s 内使用 `cubic-bezier(0.25, 0.1, 0.25, 1)` 缓动曲线将轴柄从屏幕中央向两侧推开。
*   **长卷物理伸展**：`@keyframes scrollPhysicalExpand` 控制 `.scroll-content` 的宽度从 `0.1vw` 伸展至 `100%`，结合 `scrollContentFadeIn` 实现模糊变清晰的渐显效果。

**4. 接口数据联调设计**

*   **实时时间与天气**：`App.vue` 的 `onMounted` 钩子中初始化 `setInterval`，每 1000ms 计算一次格式化日期，更新 `currentTime` 以驱动 Header 时间跳动。
*   **指标数据对接规划**：当前 `PanelX.vue` 中的图表数据主要以组件内部状态呈现，未来将通过引入 `axios` 在组件的 `onMounted` 生命周期内调用后端协同中枢提供的 RESTful API（如 `/api/v1/indicators/{categoryId}`）。为避免过度请求，在 Vue 组件内部引入 `setInterval`，默认设置为 `300000` 毫秒（5分钟），定时重载 ECharts 实例的 `setOption` 方法以刷新数据视图。

**5. 响应式与全屏适配机制**

*   系统提供了**全屏模式**切换按钮。通过监听 `isFullScreen` 状态，动态为 `document.documentElement` 添加或移除 `is-fullscreen-mode` 类，并调用全局的 `window.updateRem()` 方法，基于视口宽度动态重新计算 `REM` 基准值，确保大屏展示下的图文尺寸、绝对定位比例及 ECharts 图表尺寸能够完美缩放适配。
*   为了防止在不同分辨率下图片被拉伸，所有的 Marker 热点及 UI 面板背景大多采用百分比 (`%`) 和 `rem` 混合布局，背景图统一设置 `object-fit: contain;` 或 `background-size: 100% 100%`。
"""

with open('/data/data/com.termux/files/home/porject/silu/doc/霍尔果斯数字名片-详细设计说明书.md', 'w', encoding='utf-8') as f:
    f.write(content)

print("Detailed design document generated successfully.")
