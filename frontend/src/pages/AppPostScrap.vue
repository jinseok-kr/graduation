<template>
  <v-app id="inspire">
    <main-menu />
    <v-main>
      <post-scrap></post-scrap>
    </v-main>

    <v-footer app>
      <span>&copy; 2021</span>
    </v-footer>
  </v-app>
</template>

<script>
import MainMenu from "../components/MainMenu.vue";
import PostScrap from "../components/PostScrap.vue";
export default {
  components: { PostScrap, MainMenu },
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