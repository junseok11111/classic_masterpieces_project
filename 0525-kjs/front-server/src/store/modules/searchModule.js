import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

const searchModule = {
  state: {
    searchMovieList: null,
  },
  getters: {
    searchMovieList: (state) => state.searchMovieList,
  },
  mutations: {
    GET_SEARCH_MOVIE_LIST(state, searchMovieList) {
      state.searchMovieList = searchMovieList
    },
    CLOSE_SEARCH_MODAL(state) {
      state.searchMovieList = null
    }
  },
  actions: {
    getSearchMovieList(context, search) {
      axios({
        method: 'post',
        url: `${API_URL}/api/v1/movies/search/`,
        data: {search,},
        headers: {
          Authorization: `Token ${context.rootState.token}`
        }
      })
      .then((res) => {
        context.commit('GET_SEARCH_MOVIE_LIST', res.data)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    closeSearchModal(context) {
      context.commit('CLOSE_SEARCH_MODAL')
    }
  }
}

export default searchModule