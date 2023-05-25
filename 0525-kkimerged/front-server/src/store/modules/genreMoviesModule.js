import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

const genreMoviesModule = {
  state: {
    thriller_movies: [],
  },
  getters: {
    thrillerMovies: (state) => state.thriller_movies,
  },
  mutations: {
    GET_THRILLER_MOVIES(state, movies) {
      state.thriller_movies = movies
    },
  },
  actions: {
    getThrillerMovies(context) {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/movies/thriller/`,
        headers: {
          Authorization: `Token ${context.rootState.token}`
        }
      })
      .then((res) => {
        context.commit('GET_THRILLER_MOVIES', res.data)
      })
      .catch((err) => {
        console.log(err)
      })
    },
  }
}

export default genreMoviesModule