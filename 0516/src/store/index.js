import Vue from 'vue'
import Vuex from 'vuex'

import axios from 'axios'

Vue.use(Vuex)
const API_KEY = process.env.VUE_APP_TMDB_API_KEY
const TMDB_TOP_RATED_URL = `https://api.themoviedb.org/3/movie/top_rated/?api_key=${API_KEY}&language=ko-KR&page=1`
const TMOD_UPCOMING_URL = `https://api.themoviedb.org/3/movie/upcoming/?api_key=${API_KEY}&language=ko-KR&page=1`
export default new Vuex.Store({
  state: {
    top_rated_movies: null,
    upcoming_movies: null,
  },
  getters: {
  },
  mutations: {
    GET_TOP_RATED_MOVIES(state, movies) {
      state.top_rated_movies = movies
    },
    GET_UPCOMING_MOVIES(state, movies) {
      state.upcoming_movies = movies
    },
  },
  actions: {
    getTopRatedMovies(context) {
      axios({
        url: TMDB_TOP_RATED_URL
      })
      .then((res) => {
        context.commit('GET_TOP_RATED_MOVIES', res.data.results)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    getUpComingMovies(context) {
      axios({
        url: TMOD_UPCOMING_URL
      })
      .then((res) => {
        context.commit('GET_UPCOMING_MOVIES', res.data.results)
      })
      .catch((err) => {
        console.log(err)
      })
    },
  },
  modules: {
  }
})
