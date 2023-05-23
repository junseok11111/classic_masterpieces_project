import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

const movieLikeModule = {
  state: {
  },
  getters: {
  },
  mutations: {
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
      .then((res) => {
        console.log(res)
        context
      })
    },
  }
}

export default movieLikeModule