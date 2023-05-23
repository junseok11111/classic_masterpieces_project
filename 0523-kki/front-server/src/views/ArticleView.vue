<template>
  <div class="ArticleView">
    
    
    <div class="articleimg"></div>


    
    <button @click.prevent="createArticle">글쓰기</button>


    <div class="articletable">
    <tr class="mockrock">
      <td class="title">글 제목</td>
      <td class="writer">작성자</td>
    </tr>
    <ArticleItem
      v-for="article in articles"
      :key="article.id"
      :article="article"
    />
    </div>
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
.ArticleView{
  background-color: rgba(0, 0, 0, 0.9);
  height: 100vw;
}
.articleimg{
  display: flex;
  justify-content: center;
  align-items: center;
  height: 250px;
  background-image: url("@/assets/gonziam.jpg");
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
}

.mockrock{
  max-width: 1000px;
  width: auto;
  background-color: rgba(0, 0, 0, 0.9);
  border: 1px solid #ddd;
  border-radius: 5px;
  padding: 20px;
  text-align: center; 
  color: #ffffff;
}


.title{
  border: 1px solid #ddd;
  color: #ffffff;
  width: 700px;
}

.writer{
  border: 1px solid #ddd;
  width: 300px;
  color: #ffffff;

}

.articletable{
  margin-left: 300px;
  margin-right: 300px;

}
</style>