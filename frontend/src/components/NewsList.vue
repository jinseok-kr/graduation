<template>
  <v-container>
    <v-data-table
      :headers="headers"
      :items="newss"
      sort-by="create_date"
      sort-desc="true"
      class="elevation-1"
      :items-per-page="5"
      @click:row="serverPage"
    >
      <template v-slot:top>
        <v-toolbar flat>
          <v-toolbar-title
            >News List
            <span v-if="keyname" class="body-1 font-italic ml-3"
              >(with {{ keyname }} tagged)</span
            >
          </v-toolbar-title>
        </v-toolbar>
      </template>
      
      <template v-slot:[`item.actions`]="{ item }">
        <v-icon small class="mr-2" @click.stop="addScrap(item)">mdi-plus</v-icon>
      </template>
      <template v-slot:no-data>
        <v-btn color="primary" @click="fetchNewsList"> Reset </v-btn>
      </template>
    </v-data-table>
  </v-container>
</template>

<script>
import axios from "axios";
import EventBus from './event_bus';
export default {
  data: () => ({
    headers: [
      {
        text: "ID",
        align: "start",
        sortable: false,
        value: "id",
      },
      { text: "제 목", value: "title" },
      { text: "분 야", value: "category" },
      { text: "작성일", value: "create_date" },
      { text: "언론사", value: "press" },
      { text: "Actions", value: "actions", sortable: false },
    ],
    newss: [],
    keyname: "",
    me: {user:'Anonymous'},
  }),
  created() {
    const params = new URL(location).searchParams;
    this.keyname = params.get("keyname");
    this.fetchNewsList();
    EventBus.$on('me_change', (val)=>{
      this.me = val;
    });
  },
  methods: {
    fetchNewsList() {
      console.log("fetchNewsList()...", this.keyname);

      let getUrl = "";
      if (this.keyname) getUrl = `/api/news/list/?keyname=${this.keyname}`;
      else getUrl = "/api/news/list";

      axios
        .get(getUrl)
        .then((res) => {
          console.log("NEWS LIST GET RES!!", res);
          this.newss = res.data;
        })
        .catch((err) => {
          console.log("NEWS LIST ERR RES!!", err.response);
          alert(err.response.status + "" + err.response.statusText);
        });
    },
    serverPage(item) {
      console.log("serverPage()...", item);
      location.href = `/blog/news/${item.id}`;
    },
    addScrap(item){
      console.log("addScrap()...", item);
      if(this.me.username ==='Anonymous'){
        alert("Please login first!");
        return;
      }
      axios.get(`/api/news/${item.id}/scrap/add/`)
      .then(res =>{
        console.log("NEWS SCRAP ADD GET RES",res.data);
        if(res.data.successmsg){
          alert(res.data.successmsg);
        }
        else if(res.data.errmsg){
          alert(res.data.errmsg);
        }
      })
      .catch(err =>{
        console.log("NEWS SCRAP ADD ERR.RESPONSE", err.response);
        alert(err.response.status + '' + err.response.statusText);
      });
    },
  },
};
</script>

<style scoped>
.v-data-table >>> tbody > tr {
  cursor: pointer;
}
</style>