<template>
  <div>
    <div><img :src="`http://image.tmdb.org/t/p/w500${movie?.poster_path}`" alt="..." class="Detail-Card-img" ></div>
    <div class="Detail-Card-Title"><p>{{movieTitle}}</p></div>
  </div>
</template>

<script>
export default {
  name: 'GenreActionCard',
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
.Detail-Card-Title{
  color: white;
}
.Detail-Card-img{
  width: 200px;
}
</style>