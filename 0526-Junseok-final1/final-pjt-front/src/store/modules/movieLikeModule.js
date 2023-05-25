import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

const movieLikeModule = {
  state: {
    movieLikeCount: null,
    movieLiked: false,
  },
  getters: {
  },
  mutations: {
    GET_MOVIE_LIKE_COUNT(state, payload) {
      state.movieLikeCount = payload.movie_like_count
      state.movieLiked = payload.movie_liked
    }
  },
  actions: {
    movieLikes(context, movie_id) {
      axios({
        method: 'post',
        url: `${API_URL}/api/v1/movies/${movie_id}/movie_likes/`,
        headers: {
          Authorization: `Token ${context.rootState.token}`
        }
      })
      .then(() => {
        context.dispatch('getMovieLikeCount', movie_id)
      })
    },
    getMovieLikeCount(context, movie_id) {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/movies/${movie_id}/movie_likes/`,
        headers: {
          Authorization: `Token ${context.rootState.token}`
        }
      })
      .then((res) => {
        context.commit('GET_MOVIE_LIKE_COUNT', res.data)
      })
    }
  }
}

export default movieLikeModule