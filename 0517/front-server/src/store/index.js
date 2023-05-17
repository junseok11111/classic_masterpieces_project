import Vue from 'vue'
import Vuex from 'vuex'

import axios from 'axios'

Vue.use(Vuex)
const API_KEY = process.env.VUE_APP_TMDB_API_KEY
const TMDB_TOP_RATED_URL = `https://api.themoviedb.org/3/movie/top_rated/?api_key=${API_KEY}&language=ko-KR&page=1`
const TMDB_UPCOMING_URL = `https://api.themoviedb.org/3/movie/upcoming/?api_key=${API_KEY}&language=ko-KR&page=1`

export default new Vuex.Store({
  state: {
    top_rated_movies: null,
    upcoming_movies: null,
    casts: [],
    movie_detail: null,
  },
  getters: {
    upComing1(state) {return state.upcoming_movies?.slice(0, 6)},
    upComing2(state) {return state.upcoming_movies?.slice(6, 12)},
    upComing3(state) {return state.upcoming_movies?.slice(12, 18)},
  },
  mutations: {
    GET_TOP_RATED_MOVIES(state, movies) {
      state.top_rated_movies = movies
    },
    GET_UPCOMING_MOVIES(state, movies) {
      state.upcoming_movies = movies
    },
    GET_MOVIE_CASTS(state, casts) {
      state.casts.push(casts)
    },
    GET_MOVIE_DETAIL(state, movie) {
      state.movie_detail = movie
    }
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
        url: TMDB_UPCOMING_URL
      })
      .then((res) => {
        context.commit('GET_UPCOMING_MOVIES', res.data.results)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    getMovieCasts(context, movieId) {
      axios({
        url: `https://api.themoviedb.org/3/movie/${movieId}/credits?api_key=${API_KEY}`
      })
      .then((res) => {
        context.commit('GET_MOVIE_CASTS', res.data.cast)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    getMovieDetail(context, movieId) {
      axios({
        method: 'get',
        url: `
        https://api.themoviedb.org/3/movie/${movieId}?api_key=${API_KEY}&language=ko-KR`
      })
      .then((res) => {
        console.log(movieId)
        context.commit('GET_MOVIE_DETAIL', res)
      })
    }
  },
  modules: {
  }
})
