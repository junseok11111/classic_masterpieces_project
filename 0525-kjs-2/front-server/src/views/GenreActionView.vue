<template>
  <div>
    <GenreActionCard
      v-for="movie in ActionMovies"
      :key="movie.id"
      :movie="movie"
    />
  </div>
</template>

<script>
import GenreActionCard from '@/components/GenreActionCard'
import {mapGetters} from 'vuex'

export default {
  name: 'GenreActionView',
  components: {
    GenreActionCard,
  },
  computed: {
    ...mapGetters(["ActionMovies"])
  },
  methods: {
    getActionMovies() {
      this.$store.dispatch('getActionMovies')
    },
  },
  created() {
    this.getActionMovies()
  },
}
</script>

<style>

</style>