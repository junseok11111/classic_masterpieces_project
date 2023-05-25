<template>
  <div class="ArticleDetailView">
    <div class="articleimg"></div>
    <br />
    <br />
    <br />
    <br />
    <div class="articledetailcontainer">
      <div class="titledetail">{{ article.title }}</div>

      <br />
      <br />
      <p>{{ article.content }}</p>
      <p>작성시간: {{ article.created_at }}</p>

      <br />
      <br />
      <br />
      <br />
      <br />

      <div>
        <h3>댓글</h3>
        <div>
          <form @submit.prevent="createArticleComment">
            <input type="text" id="content" v-model="input_comment" placeholder="한 줄평을 등록하세요"> 
            <input type="submit" value="등록">
          </form>
          <hr>

          <ArticleCommentItem
            v-for="comment in articleComment"
            :key="comment.id"
            :comment="comment"
          />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import ArticleCommentItem from "@/components/ArticleCommentItem";
import { mapState } from "vuex";

export default {
  name: "ArticleDetailView",
  components: {
    ArticleCommentItem,
  },
  data() {
    return {
      input_comment: null,
    }
  },
  computed: {
    ...mapState({
      article: (state) => state.articleModule.article,
    }),
    articleComment() {
      return this.article.articlecomment_set;
    },
  },
  methods: {
    getArticleDetail() {
      const articleId = this.$route.params.id;
      this.$store.dispatch("getArticleDetail", articleId);
    },

    // 게시판 댓글 생성
    createArticleComment() {
      const inputComment = this.input_comment
      const articleId = this.$route.params.id

      if (!inputComment) {
        alert('내용을 입력해 주세요!')
        return
      } else if (inputComment.length > 100) {
        alert('100자 이하로 작성해 주세요!')
        this.input_comment = null
        return
      }
      const payload = {inputComment, articleId}
      console.log(payload)
      this.$store.dispatch('createArticleComment', payload)
      this.input_comment = null
    }
  },
  created() {
    this.getArticleDetail();
  },
};
</script>

<style>
.ArticleDetailView {
  background-color: rgba(0, 0, 0, 0.9);
  height: 100%;
}

.titledetail {
  display: flex;
  align-items: center;
  border-top: solid;
  border-bottom: solid;
  height: 50px;
  font-weight: bolder;
  font-size: 24px;
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

.articledetailcontainer {
  max-width: 1300px;
  width: 90%;
  padding: 20px;
  color: #ffffff;
  margin: 0 auto;
  text-align: left;
}

@media (max-width: 768px) {
  .articledetailcontainer {
    margin: 0 20px;
  }
}
</style>
