<template>
  <div>
    <nav class="navbar">
      <router-link :to="{name: 'home'}">Home</router-link>  | 
      <router-link :to="{name: 'home'}">Home</router-link>  |
    </nav>
    <h1>MovieDetailView</h1>
    <div v-if="movie" class="container">


      <div v-if="movie" class="container1">
        <div class="youtube">
          <iframe :src="`https://www.youtube.com/embed/${movie?.youtube_key}`" frameborder="0"></iframe>
        </div>
      </div>



      
      <div v-if="movie" class="container2">

        <div class="movie-details1">

          <div class="poster">
            <img :src="`http://image.tmdb.org/t/p/w154${movie?.poster_path}`" alt="...">
          </div>

          <div class="info">
            <h2 class="title">{{ movie?.title }}</h2>
            <p>평점: {{ movie?.vote_average }}</p>
          </div>
        </div>
        <hr>
        <div class="movie-details2">
          <div class="overview">
            <p>{{ movie?.overview }}</p>
          </div>
        </div>

      </div>


    </div>
    <hr>

    <div class="actor">

    <ActorCard
      v-for="actor in actors"
      :key="actor.id"
      :actor="actor"
    />

    </div>
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
.actor {
 display: flex;
 margin-left : 400px
}
.container {
  width: 70%;
  display: flex;
  margin-left : 400px ;
  margin-right : 100px ;
}
iframe {
  width: 100%;
  height: 500px;
} 

.container1 {
  width: 70%;
}
.container2 {
  width: 30%;
  background-color: rgb(29, 29, 29);
  padding: 30px;
  margin-left: 30px;
  margin-right: 30px;
}
.poster img {
  width: 150px;
  height: auto;
  object-fit: cover;
}


.info {
  display: flex;
  flex-direction: column;
  color: white;
}

.movie-details1 {
  display: flex;
  justify-content: space-between;
  margin-left: 20px;
  flex: 1;
  order:1;
}

.overview {

  color: white;
  display: -webkit-box;
  word-wrap: break-word;
  -webkit-line-clamp: 4;
  -webkit-box-orient: vertical;
  text-overflow: ellipsis;
  overflow: hidden;
}
/* .container {
  display: flex;
  align-items: flex-start;
  
}

.youtube {
  flex: 0 0 40%;
}

.youtube iframe {
  width: 100%;
  height: 300px;
}


.movie-details2 {
  display: flex;
  align-items: flex-start;
  margin-left: 20px;
  flex: 1;
  order:2;
}

.poster {
  flex: 0 0 200px;
  margin-right: 20px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  
}





.title {
  display: inline;
}



*/

</style>