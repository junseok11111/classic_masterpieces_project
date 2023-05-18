// top_rated에 대한 모듈
// const TMDB_TOP_RATED_URL = `https://api.themoviedb.org/3/movie/top_rated/?api_key=${API_KEY}&language=ko-KR&page=1`

import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

const topRatedModule = {
  namespased: true,
  state: {
    top_rated_movies: null,
  },
  getters: {
    topRated1(state) {return state.top_rated_movies?.slice(0, 6)},
    topRated2(state) {return state.top_rated_movies?.slice(6, 12)},
    topRated3(state) {return state.top_rated_movies?.slice(12, 18)},
  },
  mutations: {
    GET_TOP_RATED_MOVIES(state, movies) {
      state.top_rated_movies = movies
    },
  },
  actions: {
    getTopRatedMovies(context) {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/movies/top_rated/`
      })
      .then((res) => {
        context.commit('GET_TOP_RATED_MOVIES', res.data)
      })
      .catch((err) => {
        console.log(err)
      })
    },
  }
}

export default topRatedModule