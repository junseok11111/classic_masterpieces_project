// upComing에 대한 모듈
import axios from 'axios'

const API_KEY = process.env.VUE_APP_TMDB_API_KEY
const TMDB_UPCOMING_URL = `https://api.themoviedb.org/3/movie/upcoming/?api_key=${API_KEY}&language=ko-KR&page=1`

const upComingModule = {
  namespased: true,
  state: {
    upcoming_movies: null,
  },
  getters: {
    upComing1(state) {return state.upcoming_movies?.slice(0, 6)},
    upComing2(state) {return state.upcoming_movies?.slice(6, 12)},
    upComing3(state) {return state.upcoming_movies?.slice(12, 18)},
  },
  mutations: {
    GET_UPCOMING_MOVIES(state, movies) {
      state.upcoming_movies = movies
    },
  },
  actions: {
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
  }
}

export default upComingModule