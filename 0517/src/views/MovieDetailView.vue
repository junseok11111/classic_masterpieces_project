<template>
  <div>
    <h1>MovieDetailView</h1>
    <p v-if="movie">{{movie}}</p>
    <p>================================</p>
    <p>{{casts}}</p>
  </div>
</template>

<script>

export default {
  name: 'MovieDetailView',
  computed: {
    movie() {
      // const movies = this.$store.state.upcoming_movies
      // const movieId = this.$route.params.id
      
      // const movieDetail = movies?.find(function (movie) {
      //   return movie.id === movieId})
      // return movieDetail

      return this.$store.state.movie_detail
    },
    casts() {
      return this.$store.state.casts
    },
  },
  methods: {
    getMovieCasts() {
      const movieId = this.$route.params.id
      this.$store.dispatch('getMovieCasts', movieId)
    },
    getMovieDetail() {
      const movieId = this.$route.params.id
      this.$store.dispatch('getMovieDetail', movieId)
    }
  },
  created() {
    this.getMovieCasts()
    this.getMovieDetail()
  }
}
</script>

<style>

</style>