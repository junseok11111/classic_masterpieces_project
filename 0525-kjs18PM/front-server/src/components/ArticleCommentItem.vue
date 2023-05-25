<template>
  <div>
    <p>{{comment.content}} / 작성자: {{comment.user_name}}</p>
  </div>
</template>

<script>
export default {
  name: 'ArticleCommentItem',
  props: {
    comment: Object,
  }
}
</script>

<style>

</style>