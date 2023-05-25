<template>
  <div class="MovieDetailView">

    <div class="movie-detail-container">
      <div class="movie-youtube">
        <iframe :src="`https://www.youtube.com/embed/${movie?.youtube_key}`" frameborder="0"></iframe>
      </div>

      <div class="movie-detail">
        <div class="movie-detail-content">  
          <div class="movie-detail-poster">
            <img :src="`http://image.tmdb.org/t/p/w154${movie?.poster_path}`" alt="...">
          </div>
          <div class="movie-info">
            <h2 class="title">{{ movie?.title }}</h2>
            <p>평점: {{ movie?.vote_average }}</p>
            <button @click.prevent="movieLikes">좋아요
              <i class="fa-sharp fa-solid fa-thumbs-up" style="color: #707070;"></i>
            </button>
            <p>{{movieLikeCount}} 명이 좋아합니다.</p>
          </div>
        </div>
        <p class="line"></p>
        <div class="overview">
          <p>{{ movie?.overview }}</p>
        </div>
      </div>
    </div>
    <br>
    <!-- <div v-if="movie" class="container">

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
            <button @click.prevent="movieLikes">좋아요/좋아요취소</button>
          </div>
        </div>
        <hr>
        <div class="movie-details2">
          <div class="overview">
            <p>{{ movie?.overview }}</p>
          </div>
        </div>
      </div>

    </div> -->

    <div class="movie-detail-container">
      <div class="actor-detail">
        <h1>영화 배우 정보</h1>
        <div class="actors">
          <ActorCard v-for="actor in actors" :key="actor.id" :actor="actor" class="actor"/>
        </div>
      </div>
      
    </div>


    <!-- 영화 한줄 평 (container2는 임시로 넣어둔 것) -->
    <div class="container2">
      <form @submit.prevent="createMovieComment">
        <input type="text" id="content" v-model="movieComment" placeholder="한 줄평을 등록하세요"> 
        <input type="submit" value="등록">
      </form>
      <hr>
      <MovieCommentsList 
        v-for="movieComment in movieComments"
        :key="movieComment.id"
        :movieComment="movieComment"
        :movieId="movieId"
      />
    </div>
  </div>
</template>

<script>
import ActorCard from '@/components/ActorCard.vue'
import MovieCommentsList from '@/components/MovieCommentsList.vue'

import { mapState, mapGetters } from "vuex";

export default {
  name: 'MovieDetailView',
  components:{
    ActorCard,
    MovieCommentsList,
  },
  data() {
    return {
      videos: [],
      movieComment: null,
    };
  },
  mounted() {
    this.getVideos();
  },
  computed: {
    movieId() {
      return this.$route.params.id
    },
    ...mapState({
      movie: state => state.movieDetailModule.movie_detail
    }),
    ...mapState({
      actors: state => state.movieDetailModule.actors
    }),
    ...mapState({
      movieLikeCount: state => state.movieLikeModule.movieLikeCount
    }),
    ...mapGetters(['movieComments']),
  },
  methods: {
    getMovieDetail() {
      this.$store.dispatch('getMovieDetail', this.movieId)
    },
    getMovieActors() {
      this.$store.dispatch('getMovieActors', this.movieId)
    },
    getMovieCommentsList() {
      this.$store.dispatch('getMovieCommentsList', this.movieId)
    },

    // 영화 좋아요
    movieLikes() {
      const movieId = this.$route.params.id
      this.$store.dispatch('movieLikes', movieId)
    },
    
    // 영화 한줄평 생성
    createMovieComment() {
      const movieComment = this.movieComment
      const movieId = this.movieId

      if (!movieComment) {
        alert('내용을 입력해 주세요!')
        return
      } else if (movieComment.length > 20) {
        alert('20자 이하로 작성해 주세요!')
        this.movieComment = null
        return
      }
      const payload = {movieComment, movieId}
      console.log(payload)
      this.$store.dispatch('createMovieComment', payload)
      this.movieComment = null
    }
  },
  created() {
    this.getMovieDetail()
    this.getMovieActors()
    this.getMovieCommentsList()
  },
  
  // ID 변경 시 필요한 작업 수행      
  beforeRouteUpdate(to, from, next) {
    this.$store.dispatch('getMovieDetail', to.params.id)
    this.$store.dispatch('getMovieActors', to.params.id)
    this.$store.dispatch('getMovieCommentsList', to.params.id)
    next();
  },
}
</script>

<style>
.movie-detail-container {
  width: 70%;
  display: flex;
  justify-content: center;
  background-color: rgba(255, 255, 255, 0.4);
  border-radius: 3px;
  padding: auto;
  color: white;
}

.movie-youtube{
  flex: 2;
  margin: 10px 0px 10px 30px;
  z-index: 15;
}

.movie-detail-poster img {
  width: 150px;
  height: auto;
  object-fit: cover;
}

.movie-detail{
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: space-evenly;

  width: 30%;
  background-color: rgb(29, 29, 29);
  padding: 30px;
  margin: 10px 30px 10px;
  /* margin-left: 30px; */
  /* margin-right: 30px; */
}

.movie-info{
  display: flex;
  flex-direction: column;
  color: white;
}

.line{
  border-bottom: 2px solid white;
}

.movie-detail-content{
  display: flex;
  justify-content: space-around;
}

.actor-detail {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.MovieDetailView {
  overflow: auto;
  height: 100vh;
  margin: 0% 10% 0%;
  display: flex;
  flex-direction: column;
  align-items: center;
}
.MovieDetailView::-webkit-scrollbar {
  width: 8px; /* Set the width of the scrollbar */
}
.MovieDetailView::-webkit-scrollbar-thumb {
  background-color: rgba(
    0,
    0,
    0,
    0.5
  ); /* Set the color of the scrollbar thumb */
  border-radius: 4px; /* Round the corners of the thumb */
}
.MovieDetailView::-webkit-scrollbar-track {
  background-color: rgba(
    0,
    0,
    0,
    0.1
  ); /* Set the color of the scrollbar track */
}


.actors {
  display: flex;
}

.actor {
  margin: 1%;
}

iframe {
  width: 100%;
  height: 500px;
}

/* .container {
  width: 70%;
  display: flex;
  margin-left: 300px;
  margin-right: 200px;
} */

/* .container1 {
  width: 70%;
} */
/* .container2 {
  width: 30%;
  background-color: rgb(29, 29, 29);
  padding: 30px;
  margin-left: 30px;
  margin-right: 30px;
} */
/* .poster img {
  width: 150px;
  height: auto;
  object-fit: cover;
} */

/* .info {
  display: flex;
  flex-direction: column;
  color: white;
} */

/* .movie-details1 {
  display: flex;
  justify-content: space-between;
  margin-left: 20px;
  flex: 1;
  order: 1;
} */

.overview {
  color: white;
  display: -webkit-box;
  word-wrap: break-word;
  -webkit-line-clamp: 4;
  -webkit-box-orient: vertical;
  text-overflow: ellipsis;
  overflow: hidden;
}
</style>