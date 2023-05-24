import Vue from 'vue'
import Vuex from 'vuex'
import topRatedModule from './modules/topRatedModule'
import movieDetailModule from './modules/movieDetailModule'
import movieCommentModule from './modules/movieCommentModule'
import articleModule from './modules/articleModule'
import movieLikeModule from './modules/movieLikeModule'
import router from '../router'
import createPersistedState from 'vuex-persistedstate'

// import axios from 'axios'
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [
    createPersistedState(),
  ],
  state: {
    token: null,
  },
  getters: {
    isLogin(state) {
      return state.token ? true : false
    },
  },
  mutations: {
    SAVE_TOKEN(state, token) {
      state.token = token
      router.push({name : 'home'}) 
      // store/index.js $router 접근 불가 -> import를 해야함
    },

  },
  actions: {
    signUp(context, payload) {
      const username = payload.username
      const password1 = payload.password1
      const password2 = payload.password2

      axios({
        method: 'post',
        url: `${API_URL}/accounts/signup/`,
        data: {
          username, password1, password2
        }
      })
        .then((res) => {
          // console.log(res)
          // context.commit('SIGN_UP', res.data.key)
          context.commit('SAVE_TOKEN', res.data.key)
        })
        .catch((err) => {
        console.log(err)
      })
    },
    login(context, payload) {
      const username = payload.username
      const password = payload.password

      axios({
        method: 'post',
        url: `${API_URL}/accounts/login/`,
        data: {
          username, password
        }
      })
        .then((res) => {
        context.commit('SAVE_TOKEN', res.data.key)
        })
      .catch((err) => console.log(err))
    },

  },
  modules: {
    topRatedModule,
    movieDetailModule,
    movieCommentModule,
    articleModule,
    movieLikeModule,
  }
})
