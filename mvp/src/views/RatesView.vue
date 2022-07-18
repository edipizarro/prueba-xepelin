<template>
  <main>
    <iframe
      v-if="loggedIn"
      style="width: 100%; height: 150%; border: none"
      src="https://docs.google.com/spreadsheets/d/e/2PACX-1vRQyka1NJcCDCzIISTm9GRF_YWcX91p1cCOPaBVmpoUJXrjP_4YJWh0DOBxioxab9dZRDbtY_Lo6Q-h/pubhtml?gid=0&amp;single=true&amp;widget=true&amp;headers=false"
    ></iframe>
    <div v-else>
      <h1>Please login</h1>
    </div>
  </main>
</template>

<script>
export default {
  data() {
    return {
      loggedIn: false,
    };
  },
  beforeMount() {
    this.checkJWT();
  },
  methods: {
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
