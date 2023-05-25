import Vue from "vue";
import VueRouter from "vue-router";
import DoorView from "@/views/DoorView.vue";
import HomeView from "@/views/HomeView.vue";
import TopRatedView from "@/views/TopRatedView.vue";
import MovieDetailView from "@/views/MovieDetailView.vue";
import ArticleView from "@/views/ArticleView.vue";
import ArticleDetailView from "@/views/ArticleDetailView.vue";
import GameView from "@/views/GameView.vue";

import NotFound from "@/views/NotFound.vue";
import SignUpView from "@/views/SignUpView";
import LogInView from "@/views/LogInView";
import ProfileView from "@/views/ProfileView";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "DoorView",
    component: DoorView,
  },
  {
    path: "/home",
    name: "home",
    component: HomeView,
  },
  {
    path: "/TopRatedView",
    name: "TopRatedView",
    component: TopRatedView,
  },
  {
    path: "/movie/:id",
    name: "MovieDetailView",
    component: MovieDetailView,
  },
  {
    path: "/articles/",
    name: "ArticleView",
    component: ArticleView,
  },
  {
    path: "/articles/:id",
    name: "ArticleDetailView",
    component: ArticleDetailView,
  },

  // Auth
  {
    path: "/signup",
    name: "SignUpView",
    component: SignUpView,
  },

  {
    path: "/login",
    name: "LogInView",
    component: LogInView,
  },
  {
    path: "/GameView",
    name: "GameView",
    component: GameView,
  },
  {
    path: "/ProfileView",
    name: "ProfileView",
    component: ProfileView,
  },

  // 404 페이지
  {
    path: "/404",
    name: "NotFound",
    component: NotFound,
  },
  {
    path: "*",
    redirect: "/404",
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
