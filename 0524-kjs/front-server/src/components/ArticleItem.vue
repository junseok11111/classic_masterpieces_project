<template>
  <div>
    <router-link :to="{name: 'ArticleDetailView', params: {id: article.id}}">
      {{article.title}}
    </router-link>
    <span>작성자: {{article.user_name}}</span>
  </div>
</template>

<script>
export default {
  name: 'ArticleItem',
  props: {
    article: Object,
  }
}
</script>

<style>

</style>