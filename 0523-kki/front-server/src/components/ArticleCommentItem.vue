<template>
  <div>
    <p>{{comment.content}}</p> 
    
    <p>{{comment.user_name}}</p>
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