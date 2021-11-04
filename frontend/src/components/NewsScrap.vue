<template>
  <v-container>
    <v-data-table
      :headers="headers"
      :items="newss"
      sort-by="name"
      class="elevation-1"
      :items-per-page="5"
      @click:row="serverPage"
    >
      <template v-slot:top>
        <v-toolbar flat>
          <v-toolbar-title>ScrapList</v-toolbar-title>
          <v-divider class="mx-4" inset vertical></v-divider>
          <v-spacer></v-spacer>
        </v-toolbar>
      </template>
      <template v-slot:[`item.actions`]="{ item }">
        <v-icon small @click.stop="deleteNews(item)"> mdi-minus </v-icon>
      </template>

      <template v-slot:no-data>
        <v-btn color="primary" @click="fetchNewsList"> Reset </v-btn>
      </template>
    </v-data-table>
  </v-container>
</template>

<script>
import axios from "axios";
import EventBus from "./event_bus";
export default {
  data: () => ({
    headers: [
      {
        text: "ID",
        align: "start",
        sortable: false,
        value: "id",
      },
      { text: "제 목", value: "title", sortable: false },
      { text: "분 야", value: "category", sortable: false },
      { text: "작성일", value: "create_date", sortable: false },
      { text: "언론사", value: "press", sortable: false },
      { text: "Actions", value: "actions", sortable: false },
    ],
    newss: [],
    me: { user: "Anonymous" },
  }),
  created() {
      EventBus.$on("me_change", (val) => {
      this.me = val;
      console.log("EventBus()...", this.me.username);
    });
    this.fetchNewsList();
  },

  methods: {
    fetchNewsList() {
      console.log("fetchNewsList()...");
      axios
        .get(`/api/news/scrap/`)
        .then((res) => {
          console.log("NEWS SCRAPLIST GET RES!!", res);
          this.newss = res.data;
        })
        .catch((err) => {
          console.log("NEWS SCRAPLIST ERR RES!!", err.response);
          alert(err.response.status + "" + err.response.statusText);
        });
    },

    serverPage(item) {
      console.log("serverPage()...", item);
      location.href = `/blog/news/${item.id}`;
    },

    deleteNews(item) {
      console.log("deleteNews()...", item);
      if (this.me.username === "Anonymous") {
        alert("Please login first!");
        return;
      }
      if (!confirm("Are you sure to delete ?")) return;
      axios
        .get(`/api/news/${item.id}/scrap/delete`)
        .then((res) => {
          console.log("NEWS SCRAP DEL GET RES!!", res);
          const index = this.newss.indexOf(item);
          this.newss.splice(index, 1);
          alert("Scrap is canceled!");
        })
        .catch((err) => {
          console.log("NEWS SCRAP DEL GET ERR.RESPONSE", err.response);
          alert(err.response.status + "" + err.response.statusText);
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