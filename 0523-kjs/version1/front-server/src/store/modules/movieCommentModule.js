import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

const movieCommentModule = {
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

    // 영화 한줄평 생성
    createMovieComment(context, payload) {
      const content = payload.movieComment
      const movieId = payload.movieId
      console.log(context)
      axios({
        method: 'post',
        url: `${API_URL}/api/v1/movies/${movieId}/comments/`,
        data: {content,},
        headers: {
          Authorization: `Token ${context.rootState.token}`
        }
      })
      .then(()=>{
        alert('등록되었습니다!')
        context.dispatch('getMovieCommentsList', movieId)
      })
    }
  }
}

export default movieCommentModule