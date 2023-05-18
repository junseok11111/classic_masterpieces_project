<template>
  <div>
    <h1>MovieDetailView</h1>
    <div v-if="movie">
      <img :src="`http://image.tmdb.org/t/p/w154${movie?.poster_path}`" alt="...">
      <iframe :src="`https://www.youtube.com/embed/${movie?.youtube_key}`" frameborder="0"></iframe>
      <p>제목: {{movie?.title}}</p>
      <p>개봉일: {{movie?.release_date}}</p>
      <p>평점: {{movie?.vote_average}}</p>
      <p>장르: {{movie?.genres}}</p>
      <p>{{movie?.overview}}</p>
    </div>

    <!-- <p v-if="movie">{{movie}}</p> -->
    <p>================================</p>
    <!-- <p>{{actors}}</p> -->
    <ActorCard 
    v-for="actor in actors"
    :key="actor.id"
    :actor="actor"/>

  
    
  </div>
</template>

<script>
import ActorCard from '@/components/ActorCard.vue'
import {mapState} from 'vuex'

export default {
  name: 'MovieDetailView',
  components:{
    ActorCard,
  },
  data() {
    return {
      videos: []
    };
  },
  mounted() {
    this.getVideos();
  },
  computed: {
    ...mapState({
      movie: state => state.movieDetailModule.movie_detail
    }),
    // 모듈 분리 시 데이터를 불러오지 못함, 위의 코드로 수정
    // movie() {
    //   // const movies = this.$store.state.upcoming_movies
    //   // const movieId = this.$route.params.id
      
    //   // const movieDetail = movies?.find(function (movie) {
    //   //   return movie.id === movieId})
    //   // return movieDetail
    //   console.log(this.$store.state.movie_detail)
    //   return this.$store.state.movie_detail
    // },
    
    ...mapState({
      actors: state => state.movieDetailModule.actors
    }),
    // casts() {
    //   return this.$store.state.casts
    // },
  },
  methods: {
    getMovieDetail() {
      const movieId = this.$route.params.id
      this.$store.dispatch('getMovieDetail', movieId)
    },
    getMovieActors() {
      const movieId = this.$route.params.id
      this.$store.dispatch('getMovieActors', movieId)
    },
  },
  created() {
    this.getMovieDetail()
    this.getMovieActors()
  }
}
</script>

<style>

</style>