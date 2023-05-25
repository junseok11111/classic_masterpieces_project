<template>
  <div>
    <h1>뽑히나?</h1>
    <p>{{movieTitle}}</p>
  </div>
</template>

<script>
export default {
  name: 'GenreThrillerCard',
  props: {
    movie: Object,
  },
  computed: {
    movieTitle() {
      return this.movie?.title
    },
  }
}
</script>

<style>

</style>