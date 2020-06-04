<template>
  <div>
    <a-collapse class="collapse" v-model="activeKey" expandIconPosition="right" accordion>
      <a-collapse-panel header="阀门" key="1">
        <a-list :grid="{ gutter: 16,  column: 4}" :dataSource="data" size="small">
          <a-list-item slot="renderItem" slot-scope="item, index">
            <a-card :title="item.title" size="small">
              <a-switch checkedChildren="开" unCheckedChildren="关" defaultChecked size="small" />
            </a-card>
          </a-list-item>
        </a-list>
      </a-collapse-panel>

      <a-collapse-panel header="河流" key="2" :disabled="false">
        <a-list itemLayout="horizontal" :dataSource="data_river">
          <a-list-item slot="renderItem" slot-scope="item, index">
            <a-list-item-meta>
              <a slot="title">{{ item.title }}</a>
              <!--               <a-avatar slot="avatar" src="http://127.0.0.1:9090/public/image/river.png" /> -->
              <a-avatar slot="avatar" :src="riverIcon" />
            </a-list-item-meta>
            <a-switch
              slot="actions"
              checkedChildren="升"
              unCheckedChildren="降"
              defaultChecked
              size="small"
            />

            <a-input-number
              slot="actions"
              id="inputNumber"
              :min="0"
              :value="5"
              :max="10"
              size="small"
            />
          </a-list-item>
        </a-list>
      </a-collapse-panel>

      <a-collapse-panel header="监控" key="3">
        <a-checkbox size="small">显示</a-checkbox>
         <a-button shape="primary" :icon="videoIcon" @click="play"/>
      </a-collapse-panel>

      <a-collapse-panel header="其他" key="4">
        <a-list itemLayout="horizontal">
          <a-list-item>
            <a-checkbox slot="actions" size="small">下雨</a-checkbox>
          </a-list-item>
          <a-list-item>
            <a-dropdown slot="actions">
              <a-menu slot="overlay" @click="handleMenuClick">
                <a-menu-item key="1">路线1</a-menu-item>
                <a-menu-item key="2">路线2</a-menu-item>
                <a-menu-item key="3">路线3</a-menu-item>
              </a-menu>
              <a-button>
                开始漫游
                <a-icon type="down" />
              </a-button>
            </a-dropdown>
            <a-switch checkedChildren="继续" unCheckedChildren="暂停" slot="actions" />
            <a-icon type="close-circle" slot="actions" @click="closeWander" />
          </a-list-item>
        </a-list>
      </a-collapse-panel>
    </a-collapse>
    <a-input-search
      class="inputDiv"
      placeholder="input search text"
      @search="onSearch"
      size="small"
    >
      <a-button slot="enterButton">确认</a-button>
    </a-input-search>
    <div>
      <a-radio-group defaultValue buttonStyle="solid" size="small">
        <a-radio-button value="a">Hangzhou</a-radio-button>
      </a-radio-group>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      text: `A dog is a type of domesticated animal.Known for its loyalty and faithfulness,it can be found as a welcome guest in many households across the world.`,
      activeKey: ["3"],
      data: [
        {
          title: "阀2"
        },
        {
          title: "阀2"
        },
        {
          title: "阀3"
        },
        {
          title: "阀4"
        },
        {
          title: "阀5"
        },
        {
          title: "阀6"
        }
      ],
      data_river: [
        {
          title: "上游"
        },
        {
          title: "下游"
        }
      ],
      data_surroundings: [
        {
          title: "下雨"
        },
        {
          title: "漫游"
        }
      ],
      riverIcon: require("../assets/river.png"),
      videoIcon: "play-circle"
    };
  },
  methods: {
    handleMenuClick(e) {
      console.log("click", e);
      this.$message.success(`路线${e.key}开始漫游`);
    },
    closeWander() {
      this.$message.error("结束漫游");
    },
    play(){
      if(this.videoIcon === "play-circle"){
        this.videoIcon = "pause-circle"
      }else{
        this.videoIcon = "play-circle"
      }
    }
  },
  watch: {
    activeKey(key) {
      console.log(key);
    }
  }
};
</script>

<style lang="scss" scoped>
.collapse {
  width: 300px;
  /* top | right | bottom | left */
  margin: 10px 0px 0px 10px;
}

.small-margin-left {
  margin-right: 10px;
}

.inputDiv {
  width: 200px;
}
</style>