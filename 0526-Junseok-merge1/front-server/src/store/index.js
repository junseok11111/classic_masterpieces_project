import Vue from 'vue'
import Vuex from 'vuex'
import topRatedModule from './modules/topRatedModule'
import genreMoviesModule from './modules/genreMoviesModule'
import movieDetailModule from './modules/movieDetailModule'
import movieCommentModule from './modules/movieCommentModule'
import articleModule from './modules/articleModule'
import movieLikeModule from './modules/movieLikeModule'
import searchModule from './modules/searchModule'
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
      if (token) {
        router.push({name : 'home'}) 
      } else {
        router.push({name : 'LogOutView'}) 
      }
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
        context.commit('SAVE_TOKEN', res.data.key)
      })
      .catch((err) => {        
        if (err.response.status === 400) {
          const errData = err.response.data
          if (errData) {
            if ('username' in errData) {
              if (errData.username[0] === "This field may not be null." || 
              errData.username[0] === 'This field may not be blank.'
              ) {
                alert('아이디를 입력해주세요')
              } else if (errData.username[0] === "A user with that username already exists.") {
                alert('중복된 아이디 입니다.')
              }
            } else {
              alert('비밀번호를 다시 입력해주세요')
            }
          }
        }
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
      .catch((err) => {     
        if (err.response.status === 400) {
          const errData = err.response.data
          if (errData) {
            if ('username' in errData) {
              alert('아이디를 입력해주세요')
            } else if ('password' in errData) {
              alert('비밀번호를 다시 입력해주세요')
            } else {
              alert('아이디와 비밀번호를 다시 확인해주세요')
            }
          }
        }
      })
    },
    logout(context) {
      axios({
        method: 'post',
        url: `${API_URL}/accounts/logout/`,
      })
      .then(() => {
        context.commit('SAVE_TOKEN', null)
      })
      .catch((err) => console.log(err))
    },

  },
  modules: {
    topRatedModule,
    genreMoviesModule,
    movieDetailModule,
    movieCommentModule,
    articleModule,
    movieLikeModule,
    searchModule,
  }
})
