<template>
  <div>
    <a-button type="primary" @click="open">点击</a-button>
    <a-card
      class="card"
      ref="card"
      v-show="show"
      :style="{left: toolsDiv.left, top: toolsDiv.top, width: toolsDiv.width}"
      size="small"
      :headStyle="headStyle"
      :bodyStyle="bodyStyle"
    >
      <a slot="extra" @click="hide">x</a>
      <h2 slot="title" @mousedown="mousedown">#泵机控制</h2>

      <template class="ant-card-actions">
        <p>
          电源电压
          <br />
        </p>
        <template class="ant-card-actions">
          A箱: 380V
          <a-divider type="vertical" />B箱: 380V
          <a-divider type="vertical" />C箱: 380V
        </template>
      </template>
      <a-divider type="horizontal" :dashed="true" />
      <template class="ant-card-actions">
        系统状态: 正常
        <a-divider type="vertical" :dashed="true" />控制模式: 自带
        <a-divider type="vertical" />
        <a-switch defaultChecked size="small" />
      </template>
      <a-divider type="horizontal" :dashed="true" />

      <template class="ant-card-actions">
        <p>
          1#泵机: 0A
          电流
          <a-divider type="vertical" />
          <a-switch defaultChecked size="small" checkedChildren="开" unCheckedChildren="关" />
        </p>
        <p>
          2#泵机: 0A
          电流
          <a-divider type="vertical" />
          <a-switch defaultChecked size="small" checkedChildren="开" unCheckedChildren="关" />
        </p>
        <p>
          3#泵机: 0A
          电流
          <a-divider type="vertical" />
          <a-switch defaultChecked size="small" checkedChildren="开" unCheckedChildren="关" />
        </p>
        <p>
          4#泵机: 0A
          电流
          <a-divider type="vertical" />
          <a-switch defaultChecked size="small" checkedChildren="开" unCheckedChildren="关" />
        </p>
      </template>
      <a-divider type="horizontal" :dashed="true" />

      <template class="ant-card-actions">
        外河水位: 83m
        <a-divider type="vertical" :dashed="true" />内河水位: 27m
      </template>
    </a-card>
  </div>
</template>

<script>
export default {
  name: "Window",
  props: {
    titlex: String,
    id: [String, Number]
  },
  data() {
    return {
      title: "标题",
      selectElement: "",
      show: true,
      toolsDiv: {
        left: "20px",
        top: "20px",
        width: "280px"
      },
      headStyle: {},
      bodyStyle: {}
    };
  },
  computed: {
    dialogVisible: {
      get: function() {
        return true;
      },
      set: function(newValue) {
        this.$store.commit("newDialogVisible", newValue);
      }
    }
  },
  methods: {
    open() {
      this.show = true;
    },
    hide() {
      this.show = false;
    },
    clickCard(envet) {
      this.$nextTick(() => {
        this.mousedown(event);
      });
    },
    mousedown(event) {
      console.log(event);
      this.selectElement = this.$refs.card.$el;
      var div1 = this.selectElement;
      this.selectElement.style.cursor = "move";
      this.isDowm = true;
      var distanceX = event.clientX - this.selectElement.offsetLeft; // 鼠标相对于
      var distanceY = event.clientY - this.selectElement.offsetTop;
      // alert(distanceX)
      // alert(distanceY)
      console.log(distanceX);
      console.log(distanceY);
      document.onmousemove = function(ev) {
        var oevent = ev || event;
        div1.style.left = oevent.clientX - distanceX + "px";
        div1.style.top = oevent.clientY - distanceY + "px";
      };
      document.onmouseup = function() {
        document.onmousemove = null;
        document.onmouseup = null;
        div1.style.cursor = "default";
      };
    }
  }
};
</script>

<style scoped>
.layout {
  width: 330px;
}

.card {
  box-shadow: 1px 1px 5px rgba(0, 0, 0, 0.5);
  text-align: left;
}

p {
  line-height: 1;
}
</style>