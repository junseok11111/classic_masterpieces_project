<template>
  <div>
    <div>
      <span>작성자 : {{movieComment.user_name}}</span> |
      <span>평점 : [넣어야됨] </span> | 
    </div>
    <div>
      <span>{{ movieComment.content }}</span> |
      <span>{{ movieComment.created_at}}</span>
    </div>
    <hr>
    <!-- 삭제는 프로필에서 -->
    <!-- 영화 한줄평 수정 back-server에서 삭제 -->
  </div>
</template>

<script>

export default {
  name: 'MovieCommentsList',
  props:{
    movieComment: Object,
    movieId: String,
  },
  methods: {
    DeleteMovieComment() {

    }
  },
}
</script>

<style>

</style>