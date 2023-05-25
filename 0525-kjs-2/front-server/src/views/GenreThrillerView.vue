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
  },
  methods: {
    getThrillerMovies() {
      this.$store.dispatch('getThrillerMovies')
    },
  },
  created() {
    this.getThrillerMovies()
  },
}
</script>

<style>

</style>