<template>
  <div>
    <h1>TopRated</h1>
    <TopRatedCard
      v-for="movie in topRated"
      :key = movie.id
      :movie="movie"  
    />
  </div>
</template>

<script>
import TopRatedCard from '@/components/TopRatedCard'
import {mapGetters} from 'vuex'

export default {
  name: 'TopRatedView',
  components: {
    TopRatedCard,
  },
  computed: {
    ...mapGetters(['topRated']),
  }
}
</script>

<style>

</style>