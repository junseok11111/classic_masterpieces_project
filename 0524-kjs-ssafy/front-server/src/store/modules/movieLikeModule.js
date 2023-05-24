import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

const movieLikeModule = {
  state: {
    movieLikeCount: null,
  },
  getters: {
  },
  mutations: {
    GET_MOVIE_LIKE_COUNT(state, count) {
      state.movieLikeCount = count
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
        context.commit('GET_MOVIE_LIKE_COUNT', res.data.movie_like_count)
      })
    }
  }
}

export default movieLikeModule