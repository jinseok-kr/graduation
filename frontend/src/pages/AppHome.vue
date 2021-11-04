<template>
  <v-app id="inspire">
    <MainMenu></MainMenu>
    <v-main>
      <hello-world />
    </v-main>

    <v-footer app>
      <span>&copy; 2021</span>
    </v-footer>
  </v-app>
</template>

<script>
import MainMenu from "../components/MainMenu.vue";
import HelloWorld from "../components/HelloWorld.vue";
export default {
  components: { HelloWorld, MainMenu },
  props: {
    // source: String,
  },

  data: () => ({
    // drawer: null,
  }),

  created: () => {
    // this.$vuetify.theme.dark = true
  },
};
</script>