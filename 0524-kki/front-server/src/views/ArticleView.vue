<template>
  <div class="ArticleView">
    <div class="articleimg"></div>
    <br>
    <br>
    <br>
    

    <div class="articletable">
    <div class="scaredtitle">공포게시판 </div>
    
    <div class ="writebutton"><button @click.prevent="createArticle">글쓰기</button></div>
      <tr class="mockrock">
        <td class="title">글 제목</td>
        <td class="writer">작성자</td>
        <td class="time">작성시간</td>
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
import ArticleItem from "@/components/ArticleItem.vue";

import { mapState } from "vuex";

export default {
  name: "ArticleView",
  components: {
    ArticleItem,
  },
  computed: {
    ...mapState({
      articles: (state) => state.articleModule.articles,
    }),
  },
  methods: {
    getArticles() {
      this.$store.dispatch("getArticles");
    },
    createArticle() {},
  },
  created() {
    this.getArticles();
  },
};
</script>

<style>
.ArticleView {
  background-color: rgba(0, 0, 0, 0.9);
  height: 100vw;
}
.articleimg {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 250px;
  background-image: url("@/assets/gonziam.jpg");
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
}

.mockrock {
  max-width: 1300px;
  width: auto;
  background-color: rgba(0, 0, 0, 0.9);
  border: 1px solid #ddd;
  border-radius: 5px;
  padding: 20px;
  text-align: center;
  color: #ffffff;
}

.title {
  border-top: 3px solid #ddd;
  border-bottom: 1px solid #ddd;
  color: #ffffff;
  width: 700px;
}

.writer {
  border-top: 3px solid #ddd;
  border-bottom: 1px solid #ddd;
  width: 300px;
  color: #ffffff;
}

.time {
  border-top: 3px solid #ddd;
  border-bottom: 1px solid #ddd;
  width: 300px;
  color: #ffffff;
}
.articletable {
  margin-left: 300px;
  margin-right: 300px;
}
.writebutton{
  width: 1300px;
  text-align: right;
  margin-bottom: 10px;
}
.scaredtitle{
  width: 1300px;
  text-align: left;
  margin-bottom: 10px;
  color: red;
  font-size: 2em;
  font-weight: 900;
}
</style>
