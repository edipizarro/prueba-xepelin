<template>
  <div>
    <div v-if="loading">
      <h2>Loading...</h2>
    </div>
    <div v-else>
      <div v-if="!loggedIn">
        <h2>Sign In</h2>
        <form @submit.prevent="onLoginSubmit">
          <div class="form-group">
            <label for="username">Username</label>
            <input
              v-model="username"
              type="text"
              name="username"
              class="form-control"
            />
          </div>
          <div class="form-group">
            <label htmlFor="password">Password</label>
            <input
              v-model="password"
              type="password"
              name="password"
              class="form-control"
            />
          </div>
          <div class="form-group">
            <button :disabled="loading">
              <span
                class="spinner-border spinner-border-sm"
                v-show="loading"
              ></span>
              <span>Login</span>
            </button>
          </div>
        </form>
      </div>
      <div v-else>
        <h2>Hello {{ this.$cookies.get("user") }}</h2>
        <button @click="logout()">
          <span
            class="spinner-border spinner-border-sm"
            v-show="loading"
          ></span>
          <span>Logout</span>
        </button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      username: "",
      password: "",
      loading: false,
      loggedIn: false,
    };
  },
  beforeMount() {
    this.checkJWT();
  },
  methods: {
    async onLoginSubmit() {
      // fetch Login Token
      this.loading = true;
      if (this.username.length < 6 || this.password.length < 6) {
        this.loading = false;
        alert("Username and password must be at least 6 characters long");
        return;
      }
      await this.fakeLoginFetch(this.username, this.password).then((JWT) => {
        this.$cookies.set("JWT", JWT);
        this.$cookies.set("user", "fakeUser");
        this.loggedIn = true;
        this.$router.push("/rates");
      });
      this.loading = false;
    },
    async fakeLoginFetch(username, password) {
      username;
      password;
      await new Promise((r) => setTimeout(r, 2000));
      const JWT = "fakeJWT";
      return JWT;
    },
    logout() {
      this.$cookies.remove("JWT");
      this.$cookies.remove("user");
      this.loggedIn = false;
      this.$router.push("/");
    },
    checkJWT() {
      try {
        if (this.$cookies.get("JWT")) {
          this.loggedIn = true;
        } else {
          this.loggedIn = false;
        }
        console.log("END TRY");
      } catch (e) {
        console.log(e);
      }
    },
  },
};
</script>

<style scoped>
button {
  height: 100%;
  width: 100%;
  background: #606060;
  color: #ffffff;
  text-align: center;
  font-weight: bold;
  font-size: 150%;
  line-height: 100%;
  font-family: Arial;
  border-radius: 20px;
  text-decoration: none;
}

button :hover {
  background: #404040;
}
</style>
