<template>
  <div>
    <!-- <v-navigation-drawer v-model="drawer" app clipped>
      <v-list dense>
        <v-list-item link>
          <v-list-item-action>
            <v-icon>mdi-view-dashboard</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>dashboard</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-list-item link>
          <v-list-item-action>
            <v-icon>mdi-cog</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>Settings</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer> -->

    <v-app-bar app clipped-left color="teal lighten-2" dark>
      <v-toolbar-title>뉴스와 친해지기</v-toolbar-title>
      <v-spacer></v-spacer>

      <v-btn text href="/">HOME</v-btn>
      <v-btn text href="/blog/news/list/">Article</v-btn>
      <v-btn text href="/blog/post/list/">POST</v-btn>
      <v-btn text href="/admin/">Admin</v-btn>
      <v-spacer></v-spacer>

      <v-menu offset-y left bottom>
        <template v-slot:activator="{ on, attrs }">
          <v-btn text v-bind="attrs" v-on="on">
            <v-icon>mdi-account</v-icon>
            {{ me.username }}
            <v-icon>mdi-dots-vertical</v-icon>
          </v-btn>
        </template>
        <v-list>
          <template v-if="me.username === 'Anonymous'">
            <v-list-item @click="dialogOpen('login')">
              <v-list-item-title>Login</v-list-item-title>
            </v-list-item>
            <v-list-item>
              <v-list-item-title @click="dialogOpen('register')"
                >Register</v-list-item-title
              >
            </v-list-item>
          </template>
          <template v-else>
            <v-list-item @click="logout">
              <v-list-item-title>Logout</v-list-item-title>
            </v-list-item>
            <v-list-item>
              <v-list-item-title @click="dialogOpen('pwdchg')">Password change</v-list-item-title>
            </v-list-item>
            <v-list-item>
              <v-list-item-title @click="moveNewsScrap()">Article Scrap</v-list-item-title>
            </v-list-item>
            <v-list-item>
              <v-list-item-title @click="movePostScrap()">Post Scrap</v-list-item-title>
            </v-list-item>
          </template>
        </v-list>
      </v-menu>
    </v-app-bar>

    <!-- v-dialog 로그인을 위한 팝업창 -->
    <v-dialog v-model="dialog.login" max-width="600">
      <v-card class="elevation-12">
        <v-toolbar dark color="primary">
          <v-toolbar-title>Login form</v-toolbar-title>
          <v-spacer></v-spacer>
        </v-toolbar>
        <v-card-text>
          <v-form id="login-form" ref="loginForm">
            <v-text-field
              prepend-icon="person"
              name="username"
              label="Username"
              type="text"
            ></v-text-field>
            <v-text-field
              prepend-icon="lock"
              name="password"
              label="Password"
              type="password"
            ></v-text-field>
          </v-form>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn text color="grey" @click="cancel('login')">Cancel</v-btn>
          <v-btn color="primary" class="mr-5" @click="save('login')"
            >Login</v-btn
          >
        </v-card-actions>
      </v-card>
    </v-dialog>

    <!-- v-dialog 회원가입을 위한 팝업창 -->
    <v-dialog v-model="dialog.register" max-width="600">
      <v-card class="elevation-12">
        <v-toolbar dark color="success">
          <v-toolbar-title>Resgister form</v-toolbar-title>
          <v-spacer></v-spacer>
        </v-toolbar>
        <v-card-text>
          <v-form id="register-form" ref="registerForm">
            <v-text-field
              prepend-icon="person"
              name="username"
              label="Username"
              type="text"
            ></v-text-field>
            <v-text-field
              prepend-icon="lock"
              name="password1"
              label="Password"
              type="password"
            ></v-text-field>
            <v-text-field
              prepend-icon="lock"
              name="password2"
              label="Password again"
              type="password"
            ></v-text-field>
          </v-form>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn text color="grey" @click="cancel('register')">Cancel</v-btn>
          <v-btn color="success" class="mr-5" @click="save('register')"
            >Register</v-btn
          >
        </v-card-actions>
      </v-card>
    </v-dialog>

    <!-- v-dialog 비번변경을 위한 팝업창 -->
    <v-dialog v-model="dialog.pwdchg" max-width="600">
      <v-card class="elevation-12">
        <v-toolbar dark color="warning">
          <v-toolbar-title>Password change form</v-toolbar-title>
          <v-spacer></v-spacer>
        </v-toolbar>
        <v-card-text>
          <v-form id="pwdchg-form" ref="pwdchgForm">
            <v-text-field
              id="password"
              prepend-icon="lock"
              name="old_password"
              label="Old password"
              type="password"
            ></v-text-field>
            <v-text-field
              id="password"
              prepend-icon="lock"
              name="new_password1"
              label="New password"
              type="password"
            ></v-text-field>
            <v-text-field
              id="password"
              prepend-icon="lock"
              name="new_password2"
              label="New password again"
              type="password"
            ></v-text-field>
          </v-form>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn text color="grey" @click="cancel('pwdchg')">Cancel</v-btn>
          <v-btn color="warning" class="mr-5" @click="save('pwdchg')"
            >Password change</v-btn
          >
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
import axios from "axios";
import EventBus from './event_bus';

axios.defaults.xsrfCookieName = "csrftoken";
axios.defaults.xsrfHeaderName = "X-CSRFToken";

export default {
  data: () => ({
    drawer: null,
    dialog: {
      login: false,
      register: false,
      pwdchg: false,
    },
    me: { username: "Anonymous" },
  }),
  created() {
    this.getUserInfo();
  },

  watch: {
    me(newVal, oldVal){
      console.log("watch.me()...", newVal, oldVal);
      EventBus.$emit('me_change', newVal);
    }
  },
  methods: {
    dialogOpen(kind) {
      console.log("diallogOpen()...", kind);
      if (kind === "login") {
        this.dialog.login = true;
      } else if (kind === "register") {
        this.dialog.register = true;
      } else if (kind === "pwdchg") {
        this.dialog.pwdchg = true;
      }
    },

    cancel(kind) {
      console.log("cancel()...", kind);
      if (kind === "login") {
        this.dialog.login = false;
        this.$refs.loginForm.reset();
      } else if (kind === "register") {
        this.dialog.register = false;
        this.$refs.registerForm.reset();
      } else if (kind === "pwdchg") {
        this.dialog.pwdchg = false;
        this.$refs.pwdchgForm.reset();
      }
    },

    save(kind) {
      console.log("save()...", kind);
      if (kind === "login") {
        this.login();
        this.dialog.login = false;
        this.$refs.loginForm.reset();
      } else if (kind === "register") {
        this.register();
        this.dialog.register = false;
        this.$refs.registerForm.reset();
      } else if (kind === "pwdchg") {
        this.pwdchg();
        this.dialog.pwdchg = false;
        this.$refs.pwdchgForm.reset();
      }
    },

    login() {
      console.log("login()...");
      const postData = new FormData(document.getElementById("login-form"));
      axios
        .post("/api/login/", postData)
        .then((res) => {
          console.log("LOGIN POST RES", res);
          // alert(`user: ${res.data.username} login OK`);
          this.me = res.data;
        })
        .catch((err) => {
          console.log("LOGIN POST ERR.RESPONSE", err.response);
          alert("login NOK");
        });
    },
    register() {
      console.log("register()...");
      const postData = new FormData(document.getElementById("register-form"));
      axios
        .post("/api/register/", postData)
        .then((res) => {
          console.log("REGISTER POST RES", res);
          alert(`user: ${res.data.username} created OK`);
        })
        .catch((err) => {
          console.log("REGISTER POST ERR.RESPONSE", err.response);
          alert("register NOK");
        });
    },
    logout() {
      console.log("logout()...");
      axios
        .get("/api/logout/")
        .then((res) => {
          console.log("LOGOUT GET RES", res);
          alert(`user: ${this.me.username} logout OK`);
          this.me = { username: "Anonymous" };
        })
        .catch((err) => {
          console.log("LOGOUT GETT ERR.RESPONSE", err.response);
          alert("LOGOUT NOK");
        });
    },
    pwdchg() {
      console.log("pwdchg()...");
      const postData = new FormData(document.getElementById("pwdchg-form"));
      axios
        .post("/api/pwdchg/", postData)
        .then((res) => {
          console.log("PWDCHG GET RES", res);
          alert(`user: ${this.me.username} password change OK`);
        })
        .catch((err) => {
          console.log("PWDCHG GET ERR.RESPONSE", err.response);
          alert("PASSWORD CHANGE NOK");
        });
    },
    getUserInfo() {
      console.log("getUserInfo()...");
      axios
        .get("/api/me/")
        .then((res) => {
          console.log("GET USER INFO GET", res);
          this.me = res.data;
        })
        .catch((err) => {
          console.log("GET USER INFO GET ERR.RESPONSE", err.response);
          alert(err.response.status + "" + err.response.statusText);
        });
    },
    moveNewsScrap(){
      console.log("moveNewsScrap()...");
      location.href = `/blog/news/scrap/`;
    },
    movePostScrap(){
      console.log("movePostScrap()...");
      location.href = `/blog/post/scrap/`;
    },
  },
};
</script>

<style>
</style>