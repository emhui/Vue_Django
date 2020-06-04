<template>
  <!--   <div v-bind:id="id" v-if="dialogVisible">
    <header>
        dsaf
      <div @mousedown="mousedown">
        <h2 v-html="title"></h2>
        <div @click.stop="closeDialog()" style="position: absolute;top: 0px; right: 20px;">
          <span>
            <svg class="icon" aria-hidden="false">
              <use xlink:href="#el-icon-ext-close" />
            </svg>
          </span>
        </div>
      </div>
    </header>
    <main>
      <slot>这里是内容</slot>
    </main>
    <footer>
      <span class="dialog-footer">
        <button @click="closeDialog">取 消</button>
        <button type="primary" @click="closeDialog">确 定</button>
      </span>
    </footer>
  </div>-->

  <div>
    <a-button type="primary" @click="open">点击</a-button>
    <a-card
      id="card"
      style="width: 300px"
      v-show="show"
      :style="{left: divXY.x, top: divXY.y}"
      size="small"
    >
      <!--     <a-card id="card" title="1#闸门" style="width: 300px" @click="clickCard" v-show="show"> -->
      <a slot="extra" @click="hide">x</a>
      <h2 slot="title" @mousedown="mousedown">1#闸门</h2>

      <p>实际闸高： 84m</p>
      <p>外河水位： 79.3m</p>
      <p>闸门状态： 停止</p>
      <template class="ant-card-actions">
      控制模式： 自动
        <a-divider type="vertical" />
        <a-switch defaultChecked size="small" />
      </template>
      <template class="ant-card-actions" slot="actions">
        <a-button>提升</a-button>
        <a-button>降落</a-button>
        <a-button>停止</a-button>
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
      show: false,
      divXY: {
        x: "20px",
        y: "20px"
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
      this.selectElement = document.getElementById("card");
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

#card {
  box-shadow: 1px 1px 5px rgba(0, 0, 0, 0.5);
  text-align: left;
}

.layout-header {
  height: 30px;
  background: blue;
}
</style>