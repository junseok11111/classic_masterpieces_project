<template>
  <div>
    <GenreThrillerCard
      v-for="movie in thrillerMovies"
      :key="movie.id"
      :movie="movie"
    />
  </div>
</template>

<script>
import GenreThrillerCard from '@/components/GenreThrillerCard'
import {mapGetters} from 'vuex'

export default {
  name: 'GenreThrillerView',
  components: {
    GenreThrillerCard,
  },
  computed: {
    ...mapGetters(["thrillerMovies"])
    // ...mapState({
    //   thrillerMovies: state => state.genreMoviesModule.thriller_movies
    // }),
  },
  methods: {
    getThrillerMovies() {
      this.$store.dispatch('getThrillerMovies')
    },
  },
  created() {
    this.getThrillerMovies()
  },
  // beforeMount() {
  // this.getThrillerMovies();
  // }
}
</script>

<style>

</style>