import Vue from 'vue'
import VueRouter from 'vue-router'
import DoorView from '@/views/DoorView.vue'
import HomeView from '@/views/HomeView.vue'
import TopRatedView from '@/views/TopRatedView.vue'
import MovieDetailView from '@/views/MovieDetailView.vue'
import ArticleView from '@/views/ArticleView.vue'
import ArticleDetailView from '@/views/ArticleDetailView.vue'

import GenreThrillerView from '@/views/GenreThrillerView.vue'
import GenreSFView from '@/views/GenreSFView.vue'
import GenreActionView from '@/views/GenreActionView.vue'
import GenreMysteryView from '@/views/GenreMysteryView.vue'


import SignUpView from '@/views/SignUpView'
import LogInView from '@/views/LogInView'
import LogOutView from '@/views/LogOutView'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'DoorView',
    component: DoorView,
  },
  {
    path: '/home',
    name: 'home',
    component: HomeView
  },
  {
    path: '/TopRatedView',
    name: 'TopRatedView',
    component: TopRatedView
  },
  {
    path: '/movie/:id',
    name: 'MovieDetailView',
    component: MovieDetailView
  },
  {
    path: '/articles/',
    name: 'ArticleView',
    component: ArticleView
  },
  {
    path: '/articles/:id',
    name: 'ArticleDetailView',
    component: ArticleDetailView
  },

  // Genre
  {
    path: 'movies/thriller',
    name: 'GenreThrillerView',
    component: GenreThrillerView
  },
  {
    path: 'movies/science_fiction',
    name: 'GenreSFView',
    component: GenreSFView
  },
  {
    path: 'movies/action',
    name: 'GenreActionView',
    component: GenreActionView
  },
  {
    path: 'movies/mystery',
    name: 'GenreMysteryView',
    component: GenreMysteryView
  },
  


  // Auth
  {
    path: '/signup',
    name: 'SignUpView',
    component: SignUpView
  },

  {
    path: '/login',
    name: 'LogInView',
    component: LogInView
  },

  {
    path: '/logout',
    name: 'LogOutView',
    component: LogOutView
  },


]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
