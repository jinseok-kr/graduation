<template>
  <v-app id="inspire">
    <main-menu/>
    <v-main>
      <news-detail></news-detail>
    </v-main>

    <v-footer app>
      <span>&copy; 2021</span>
    </v-footer>
  </v-app>
</template>

<script>
import MainMenu from '../components/MainMenu.vue';
import NewsDetail from "../components/NewsDetail.vue";
export default {
  components: { NewsDetail, MainMenu },
  props: {
    source: String,
  },

  data: () => ({
    drawer: null,
  }),

  created: () => {
    // this.$vuetify.theme.dark = true
  },
};
</script>