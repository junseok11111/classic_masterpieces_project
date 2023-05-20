import Vue from 'vue'
import Vuex from 'vuex'
import topRatedModule from './modules/topRatedModule'
import movieDetailModule from './modules/movieDetailModule'

// import axios from 'axios'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
  },
  getters: {
  },
  mutations: {
  },
  actions: {
  },
  modules: {
    topRatedModule,
    movieDetailModule,
  }
})
