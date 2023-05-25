<template>
  <div>
    <GenreMysteryCard
      v-for="movie in MysteryMovies"
      :key="movie.id"
      :movie="movie"
    />
  </div>
</template>

<script>
import GenreMysteryCard from '@/components/GenreMysteryCard'
import {mapGetters} from 'vuex'

export default {
  name: 'GenreMysteryView',
  components: {
    GenreMysteryCard,
  },
  computed: {
    ...mapGetters(["MysteryMovies"])
  },
  methods: {
    getMysteryMovies() {
      this.$store.dispatch('getMysteryMovies')
    },
  },
  created() {
    this.getMysteryMovies()
  },
}
</script>

<style>

</style>