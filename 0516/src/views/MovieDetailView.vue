<template>
  <div>
    <h1>MovieDetailView</h1>
    <p>{{movie}}</p>
  </div>
</template>

<script>
export default {
  name: 'MovieDetailView',
  computed: {
    movie() {
      const movies = this.$store.state.upcoming_movies
      const movieId = this.$route.params.id
      console.log(movieId)
      const movieDetail = movies.filter(function (movie) {
        return movie.id === movieId})
      return movieDetail[0]
    }
  },
}
</script>

<style>

</style>