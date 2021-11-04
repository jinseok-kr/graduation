<template>
  <v-app id="inspire">
    <main-menu />
    <v-main>
      <news-scrap></news-scrap>
    </v-main>

    <v-footer app>
      <span>&copy; 2021</span>
    </v-footer>
  </v-app>
</template>

<script>
import MainMenu from "../components/MainMenu.vue";
import NewsScrap from "../components/NewsScrap.vue";
export default {
  components: { NewsScrap, MainMenu },
  props: {
    //source: String,
  },

  data: () => ({
    //drawer: null,
  }),

  created: () => {
    // this.$vuetify.theme.dark = true
  },
};
</script>