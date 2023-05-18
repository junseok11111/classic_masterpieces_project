import Vue from 'vue'
import Vuex from 'vuex'
import topRatedModule from './modules/topRatedModule'
import upComingModule from './modules/upComingModule'
import movieDetailModule from './modules/movieDetailModule'

// import axios from 'axios'

Vue.use(Vuex)
// const API_URL = 'http://127.0.0.1:8000'
// const API_KEY = process.env.VUE_APP_TMDB_API_KEY

export default new Vuex.Store({
  state: {
    // casts: [],
  },
  getters: {
  },
  mutations: {
    // GET_MOVIE_CASTS(state, casts) {
    //   state.casts.push(casts)
    // },
  },
  actions: {
    // getMovieCasts(context, movieId) {
    //   axios({
    //     url: `https://api.themoviedb.org/3/movie/${movieId}/credits?api_key=${API_KEY}`
    //   })
    //   .then((res) => {
    //     context.commit('GET_MOVIE_CASTS', res.data.cast)
    //   })
    //   .catch((err) => {
    //     console.log(err)
    //   })
    // },
  },
  modules: {
    topRatedModule,
    upComingModule,
    movieDetailModule,
  }
})
