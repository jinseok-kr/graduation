<template>
  <v-app id="inspire">
    <main-menu />
    <v-main>
      <NewsList />
    </v-main>

    <v-footer app>
      <span>&copy; 2021</span>
    </v-footer>
  </v-app>
</template>

<script>
import MainMenu from "../components/MainMenu.vue";
import NewsList from "../components/NewsList.vue";
export default {
  components: { NewsList, MainMenu },
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