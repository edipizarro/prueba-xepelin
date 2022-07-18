import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import RatesView from "../views/RatesView.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "login",
      component: HomeView,
    },
    {
      path: "/rates",
      name: "rates",
      component: RatesView,
    },
  ],
});

export default router;
