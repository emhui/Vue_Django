<template>
  <div class="label-content">
    <a-button id="btn" class="box-left margin-bottom-small" type="primary" size="small" @click="onClick">按钮</a-button>
    <a-list itemLayout="horizontal" :dataSource="data" bordered size="small">
      <a-list-item slot="renderItem" slot-scope="item, index">
        <a-list-item-meta>
          <a slot="title">{{ item.title }}</a>
        </a-list-item-meta>
        <a slot="actions">edit</a>
        <a slot="actions">del</a>
      </a-list-item>
    </a-list>
  </div>
</template>
<script>
const data = [
  {
    title: "Ant Design Title 1"
  },
  {
    title: "Ant Design Title 2"
  },
  {
    title: "Ant Design Title 3"
  },
  {
    title: "Ant Design Title 4"
  }
];
export default {
  data() {
    return {
      data
    };
  },
  methods: {
      onClick(){
          var btn = document.getElementById("btn")
          if (btn.classList.contains("active")){
              btn.classList.remove("active")
          }else{
              btn.classList.add("active")
          }
      }
  }
};
</script>
<style>
.label-content {
  margin: 10px 0 0 10px;
  width: 250px;
  background: #ff00ff;
}

.margin-bottom-small {
  margin-bottom: 10px;
}

.box-left {
}

.active {
  color: #fff;
  background-color: #096dd9;
  border-color: #096dd9;
}
</style>
