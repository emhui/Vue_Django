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
      <h2 slot="title" @mousedown="mousedown">#实时水位</h2>

      <template class="ant-card-actions ">
        <a-row :gutter="[24,8]" style="text-align: center">
          <a-col :span="12">
            <a-card title="内河" size="small">
              <h4>3.11m</h4>
            </a-card>
          </a-col>
          <a-col :span="12">
            <a-card title="外河" size="small">
              <h4>3.11m</h4>
            </a-card>
          </a-col>
        </a-row>
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
        top: "4em",
        width: "180px"
      },
      headStyle: {},
      bodyStyle: {
        textAlgin: "center"
      }
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
.card {
  box-shadow: 1px 1px 5px rgba(0, 0, 0, 0.5);
  text-align: left;
}

p {
  line-height: 1;
}
</style>