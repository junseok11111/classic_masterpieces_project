<template>
  <div>
    <h1>UpComing</h1>
    <UpComingCard
      v-for="movie in upComing"
      :key = movie.id
      :movie="movie"  
    />
  </div>
</template>

<script>
import UpComingCard from '@/components/UpComingCard'

export default {
  name: 'UpComingView',
  components: {
    UpComingCard,
  },
  computed: {
    upComing() {
      return this.$store.state.upcoming_movies
    },
  }
}
</script>

<style>

</style>