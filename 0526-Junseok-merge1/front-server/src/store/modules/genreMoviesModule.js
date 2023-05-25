import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

const genreMoviesModule = {
  state: {
    thriller_movies: [],
    sf_movies: [],
    mystery_movies: [],
    action_movies: [],
  },
  getters: {
    thrillerMovies: (state) => state.thriller_movies,
    SFMovies: (state) => state.sf_movies,
    MysteryMovies: (state) => state.mystery_movies,
    ActionMovies: (state) => state.action_movies,
  },
  mutations: {
    GET_THRILLER_MOVIES(state, movies) {
      state.thriller_movies = movies
    },
    GET_SF_MOVIES(state, movies) {
      state.sf_movies = movies
    },
    GET_MYSTERY_MOVIES(state, movies) {
      state.mystery_movies = movies
    },
    GET_ACTION_MOVIES(state, movies) {
      state.action_movies = movies
    },
  },
  actions: {
    // Thriller
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

    // SF
    getSFMovies(context) {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/movies/science_fiction/`,
        headers: {
          Authorization: `Token ${context.rootState.token}`
        }
      })
      .then((res) => {
        context.commit('GET_SF_MOVIES', res.data)
      })
      .catch((err) => {
        console.log(err)
      })
    },

    // Mystery
    getMysteryMovies(context) {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/movies/mystery/`,
        headers: {
          Authorization: `Token ${context.rootState.token}`
        }
      })
      .then((res) => {
        context.commit('GET_MYSTERY_MOVIES', res.data)
      })
      .catch((err) => {
        console.log(err)
      })
    },

    // Action
    getActionMovies(context) {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/movies/action/`,
        headers: {
          Authorization: `Token ${context.rootState.token}`
        }
      })
      .then((res) => {
        context.commit('GET_ACTION_MOVIES', res.data)
      })
      .catch((err) => {
        console.log(err)
      })
    },
  }
}

export default genreMoviesModule