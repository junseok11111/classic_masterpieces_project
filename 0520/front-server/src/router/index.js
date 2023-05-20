import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import TopRatedView from '@/views/TopRatedView.vue'
import MovieDetailView from '@/views/MovieDetailView.vue'
import DoorView from '@/views/DoorView.vue'

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
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
