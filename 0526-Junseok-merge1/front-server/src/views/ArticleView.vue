<template>
  <div class="ArticleView-container" @click="closeArticleForm">
    <div class="articleimg"></div>
    <br />
    <br />
    <br />

    <div class="article_table">
      <div class="scaredtitle">공포게시판</div>

      <div class="writebutton" @click.stop>
        <button @click.prevent="openArticleForm">글쓰기</button>
      </div>

      <div @click.stop>
        <form v-if="article_form" @submit="createArticle" >
          <input id="title" type="text" placeholder="제목을 입력하세요." v-model.trim="title" class="article-title-input">
          <textarea id="content" cols="70" rows="10" placeholder="내용을 입력하세요." v-model.trim="content" class="article-content-input"></textarea>
          <input type="submit" value="제출" class="article-submit-button">
        </form>
      </div>

      <tr class="article_list">
        <td class="article_title">글 제목</td>
        <td class="article_writer">작성자</td>
        <td class="article_time">작성시간</td>
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
  data() {
    return {
      article_form: false,
      title: null,
      content: null,
    }
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
    openArticleForm() {
      this.article_form = true
    },
    closeArticleForm() {
      this.article_form = false
    },
    createArticle() {
      const title = this.title
      const content = this.content

      if (title && content) {
        const payload = {title, content}
        this.$store.dispatch('createArticle', payload)
        this.title = null
        this.content = null
      } else {
        alert('잘못된 입력입니다')
      }
    },
  },
  created() {
    this.getArticles();
  },
};
</script>

<style>
.ArticleView-container {
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

.article_list {
  max-width: 1300px;
  width: auto;
  background-color: rgba(0, 0, 0, 0.9);
  border: 1px solid #ddd;
  border-radius: 5px;
  padding: 20px;
  text-align: center;
  color: #ffffff;
}

.article_title {
  border-top: 3px solid #ddd;
  border-bottom: 1px solid #ddd;
  color: #ffffff;
  width: 700px;
}

.article_writer {
  border-top: 3px solid #ddd;
  border-bottom: 1px solid #ddd;
  width: 300px;
  color: #ffffff;
}

.article_time {
  border-top: 3px solid #ddd;
  border-bottom: 1px solid #ddd;
  width: 300px;
  color: #ffffff;
}
.article_table {
  margin-left: 300px;
  margin-right: 300px;
}
.writebutton {
  /* width: 1300px; */
  width: fit-content;
  text-align: right;
  /* margin-right: 10px; */
  margin-bottom: 10px;
}
.scaredtitle {
  width: 1300px;
  text-align: left;
  margin-bottom: 10px;
  color: red;
  font-size: 2em;
  font-weight: 900;
}
@media (max-width: 1300px) {
  .article_table {
    margin-left: 200px;
    margin-right: 200px;
  }
}

@media (max-width: 768px) {
  .article_table {
    margin-left: 200px;
    margin-right: 200px;
  }
}

.article-title-input, .article-content-input {
  width: 700px;
  display: block;
}


.article-submit-button {
  /* display: block; */
  width: 100px;
  margin-bottom: 5%;

  /* padding: 10px; */
  font-size: 15px;
  background-color: #007bff;
  border: none;
  border-radius: 3px;
  color: #fff;
  cursor: pointer;
}

.article-submit-button:hover {
  background-color: #0069d9;
}
</style>
