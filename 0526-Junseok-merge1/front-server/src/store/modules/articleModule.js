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

    // article 상세 조회
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

    // article 생성
    createArticle(context, payload) {
      const title = payload.title
      const content = payload.content
      axios({
        method: 'post',
        url: `${API_URL}/api/v1/articles/`,
        data: {title, content,},
        headers: {
          Authorization: `Token ${context.rootState.token}`
        }
      })
      .then(() => {
        alert('등록되었습니다.')
        context.dispatch('getArticles')
      })
    },

    // article 댓글 생성
    createArticleComment(context, payload) {
      const content = payload.inputComment
      const articleId = payload.articleId
      console.log(context)
      axios({
        method: 'post',
        url: `${API_URL}/api/v1/articles/${articleId}/comments/`,
        data: {content,},
        headers: {
          Authorization: `Token ${context.rootState.token}`
        }
      })
      .then(()=>{
        alert('등록되었습니다!')
        context.dispatch('getArticleDetail', articleId)
      })
    }
  }
}

export default articleModule