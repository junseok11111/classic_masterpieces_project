<template>
  <div>
    <p>{{ movieComment.content }}</p>
    <MovieComment />
  </div>
</template>

<script>

export default {
  name: 'MovieCommentsList',
  components: {
  },
  props:{
    movieComment: Object,
  },
}
</script>

<style>

</style>