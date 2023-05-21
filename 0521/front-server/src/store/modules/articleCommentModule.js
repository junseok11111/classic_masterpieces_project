import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

const articleCommentModule = {
  state: {
    movie_comments: null,
  },
  getters: {
    movieComments: (state) => state.movie_comments,
  },
  mutations: {
    GET_MOVIE_COMMENTS_LIST(state, movie_comments) {
      state.movie_comments = movie_comments
    },
  },
  actions: {
    getMovieCommentsList(context, movie_id) {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/movies/${movie_id}/comments/`,
      })
      .then((res) => {
        console.log(res)
        context.commit('GET_MOVIE_COMMENTS_LIST', res.data)
      })
      .catch((err) => {
        console.log(err)
      })
    },
  }
}

export default articleCommentModule