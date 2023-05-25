import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

const articleModule = {
  state: {
    articles: null,
    article: null,
  },
  getters: {
    articles: (state) => state.articles,
  },
  mutations: {
    GET_ARTICLES(state, articles) {
      state.articles = articles
    },
    GET_ARTICLE_DETAIL(state, article) {
      state.article = article
    }
  },
  actions: {
    getArticles(context) {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/articles/`,
        headers: {
          Authorization: `Token ${context.rootState.token}`
        }
      })
      .then((res) => {
        context.commit('GET_ARTICLES', res.data)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    getArticleDetail(context, articleId) {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/articles/${articleId}/`,
        headers: {
          Authorization: `Token ${context.rootState.token}`
        }
      })
      .then((res) => {
        context.commit('GET_ARTICLE_DETAIL', res.data)
      })
      .catch((err) => {
        console.log(err)
      })
    },
  }
}

export default articleModule