<template>
  <div>
    <GenreSFCard
      v-for="movie in SFMovies"
      :key="movie.id"
      :movie="movie"
    />
  </div>
</template>

<script>
import GenreSFCard from '@/components/GenreSFCard'
import {mapGetters} from 'vuex'

export default {
  name: 'GenreSFView',
  components: {
    GenreSFCard,
  },
  computed: {
    ...mapGetters(["SFMovies"])
  },
  methods: {
    getSFMovies() {
      this.$store.dispatch('getSFMovies')
    },
  },
  created() {
    this.getSFMovies()
  },
}
</script>

<style>

</style>