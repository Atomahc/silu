import re

html_content = """<div class="custom-timeline">
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
"""

# Read the file
with open('/data/data/com.termux/files/home/Desktop/项目/silu/src/App.vue', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the marker line
pattern = r"(\{ id: 2, x: 14\.5, y: 57\.0, title: '六代国门'[^}]*\})"
replacement = r"{ id: 2, x: 14.5, y: 57.0, title: '六代国门', bgImg: '/Frame 422@2x.png', desc: '霍尔果斯历经六代国门的建设与演变，展现了中国边境口岸的沧桑巨变与辉煌发展。', stats: [{ label: '演进历程', value: '6代迭代' }, { label: '通关能力', value: '提升100倍' }], htmlContent: `" + html_content + r"` }"

new_content = re.sub(pattern, replacement, content)

css_styles = """
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
"""

# Append CSS to the end of the file if not already present
if ".custom-timeline" not in new_content:
    new_content += css_styles

with open('/data/data/com.termux/files/home/Desktop/项目/silu/src/App.vue', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Updated successfully")
