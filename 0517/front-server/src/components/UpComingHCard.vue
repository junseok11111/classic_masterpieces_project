<template>
  <div>
    <router-link :to="{name:'MovieDetailView', params: {id: movie.id}}">
      <img :src="imgSrc" alt="...">
    </router-link>
  </div>
</template>

<script>
export default {
  name: 'UpComingHCard',
  props: {
    movie: Object,
  },
  computed: {
    imgSrc() {
      const imgSrc = `http://image.tmdb.org/t/p/w154${this.movie.poster_path}`
      return imgSrc
    },
  },
}
</script>

<style>

</style>