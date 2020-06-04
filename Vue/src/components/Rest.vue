<template>
  <div class="box">
    <h1>{{title}}</h1>
    <ul>
      <li v-for="(column, index) in columns" :key="index" @click="getInfo(column.id)">
        {{index}} - {{column.name}} - {{column.slug}} -
        <button @click="deleteColumn(column.id)">x</button>
      </li>
    </ul>
    <form action>
      name：
      <input type="text" placeholder="book name" v-model="columnEntity.name" />
      <br />slug：
      <input type="text" placeholder="book author" v-model="columnEntity.slug" />
      <br />intro：
      <input type="text" placeholder="book author" v-model="columnEntity.intro" />
      <br />nav_display：
      <input
        type="checkbox"
        placeholder="book author"
        v-model="columnEntity.nav_display"
      />
      <br />home_display：
      <input
        type="checkbox"
        placeholder="book author"
        v-model="columnEntity.home_display"
      />
      <br />
    </form>
    <button type="submit" @click="submit()">submit</button>
    <button @click="rediect">重定向</button>
    <button @click="updateInfo">更新</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      title: "Vue+Django 前后端分离，实现增删改查",
      columns: null,
      columnEntity: {
        name: "",
        slug: "",
        intro: "",
        nav_display: false,
        home_display: false
      },
      currentId: 0
    };
  },
  mounted() {
    this.getData();
  },
  methods: {
    submit() {
      console.log(this.columnEntity);
      this.$http
        .post("http://127.0.0.1:8000/api/column/", {
          name: this.columnEntity.name,
          slug: this.columnEntity.slug,
          intro: this.columnEntity.intro,
          nav_display:
            this.columnEntity.nav_display === null
              ? false
              : this.columnEntity.nav_display,
          home_display:
            this.columnEntity.home_display === null
              ? false
              : this.columnEntity.home_display
        })
        .then(res => {
          console.log(res);
          this.getData();
          // 成功的话，重定向到这个页面
          // this.rediect();
        });
    },
    rediect() {
      // 该方法定向无法定向到当前路由
      // this.$router.push("Rest");
      window.location.reload();
    },
    getData() {
      this.$http.get("http://127.0.0.1:8000/api/column/").then(res => {
        console.log(res);
        this.columns = res.data;
      });
    },
    deleteColumn(id) {
      this.$http.delete(`http://127.0.0.1:8000/api/column/${id}/`).then(res => {
        console.log(res);
        this.getData();
      });
    },
    getInfo(id) {
      this.$http.get(`http://127.0.0.1:8000/api/column/${id}/`).then(res => {
        this.columnEntity = res.data;
        this.currentId = id;
      });
    },
    updateInfo() {
      console.log("更新信息", this.currentId);
      this.$http
        .put(`http://127.0.0.1:8000/api/column/${this.currentId}/`, {
          name: this.columnEntity.name,
          slug: this.columnEntity.slug,
          intro: this.columnEntity.intro,
          nav_display:
            this.columnEntity.nav_display === null
              ? false
              : this.columnEntity.nav_display,
          home_display:
            this.columnEntity.home_display === null
              ? false
              : this.columnEntity.home_display
        })
        .then(res => {
          console.log(res);
          this.getData();
          // 成功的话，重定向到这个页面
          // this.rediect();
        });
    }
  }
};
</script>

<style>
</style>