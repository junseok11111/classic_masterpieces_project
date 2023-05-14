<template>
  <div class="home">
    <h3>
      <router-link :to="{name: 'UpComingView'}">Upcoming</router-link>
    </h3>
    <UpComingHCard
      v-for="movie in upComing"
      :key = movie.id
      :movie="movie"
    />
  </div>
</template>

<script>
import UpComingHCard from '@/components/UpComingHCard'

export default {
  name: 'HomeView',
  components: {
    UpComingHCard,
  },
  computed: {
    upComing() {
      return this.$store.state.upcoming_movies
    },
    // topRate() {
    //   return this.$store.state.top_rated_movies
    // },
  }
}
</script>
