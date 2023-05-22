<template>
  <div>
    <h1>Article Page</h1>
    <button @click.prevent="createArticle">글쓰기</button>
    <ArticleItem
      v-for="article in articles"
      :key="article.id"
      :article="article"
    />
  </div>
</template>

<script>
import ArticleItem from '@/components/ArticleItem.vue'

import {mapState} from 'vuex'

export default {
  name: 'ArticleView',
  components: {
    ArticleItem,
  },
  computed: {
    ...mapState({
      articles: state => state.articleModule.articles
    }),
  },
  methods: {
    getArticles() {
      this.$store.dispatch('getArticles')
    },
    createArticle() {
      
    }
  },
  created() {
    this.getArticles()
  }

}
</script>

<style>

</style>