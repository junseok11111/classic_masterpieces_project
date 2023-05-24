<template>
  <div class="MovieDetailView">
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

    </div>

    <hr>

    <div class="actordetail">
      <h1>영화 배우 정보</h1>
      <div class="actor">
        <ActorCard v-for="actor in actors" :key="actor.id" :actor="actor" />
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
      <!--------------------------------------------- -->
      </div>
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
  }
}
</script>

<style>
.MovieDetailView {
  overflow: auto; /* or overflow: scroll; */
  height: 100vh;
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

.actor {
  display: flex;
  margin-left: 300px;
  color: white;
}
h1 {
  display: flex;
  margin-left: 300px;
  color: white;
}
.container {
  width: 70%;
  display: flex;
  margin-left: 300px;
  margin-right: 200px;
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
  order: 1;
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
</style>
