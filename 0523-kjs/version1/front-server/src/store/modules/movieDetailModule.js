// movie_detail에 대한 모듈

import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

const movieDetailModule = {
  state: {
    movie_detail: null,
    actors: [],
  },
  getters: {},
  mutations: {
    GET_MOVIE_DETAIL(state, movie) {
      state.movie_detail = movie
    },
    GET_MOVIE_ACTORS(state, actors) {
      state.actors = [...actors]
      // state.actors.push(actors) <- 잘못된 코드
    },
  },
  actions: {
    getMovieDetail(context, movieId) {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/movies/${movieId}/`
      })
      .then((res) => {
        context.commit('GET_MOVIE_DETAIL', res.data)
      })
    },
    getMovieActors(context, movieId) {
      axios({
        url: `${API_URL}/api/v1/movies/${movieId}/actors/`
      })
      .then((res) => {
        console.log(res)
        context.commit('GET_MOVIE_ACTORS', res.data)
      })
      .catch((err) => {
        console.log(err)
      })
    },
  }
}

export default movieDetailModule