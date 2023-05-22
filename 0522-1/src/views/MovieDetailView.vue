<template>
  <div class="MovieDetailView">
    <nav class="navbar">
      <div class="navbar-header">
        <div class="navbar-left">
          <img
            src="../assets/7a57b8e8-4029-4220-8d9f-2b1c89b2c1e5.png"
            alt="로고"
            class="logo"
          />
        </div>
        <div class="navbar-right">
          <!-- <router-link :to="{ name: 'UpComingView' }">Upcoming</router-link> | -->
          <router-link :to="{ name: 'home' }">Home</router-link> |
          <router-link :to="{ name: 'LogInView' }">LogIn</router-link> |
        </div>
      </div>
    </nav>

    <h1>MovieDetailView</h1>
    <div v-if="movie" class="container">
      <div v-if="movie" class="container1">
        <div class="youtube">
          <iframe
            :src="`https://www.youtube.com/embed/${movie?.youtube_key}`"
            frameborder="0"
          ></iframe>
        </div>
      </div>

      <div v-if="movie" class="container2">
        <div class="movie-details1">
          <div class="poster">
            <img
              :src="`http://image.tmdb.org/t/p/w154${movie?.poster_path}`"
              alt="..."
            />
          </div>

          <div class="info">
            <h2 class="title">{{ movie?.title }}</h2>
            <p>평점: {{ movie?.vote_average }}</p>
          </div>
        </div>
        <hr />
        <div class="movie-details2">
          <div class="overview">
            <p>{{ movie?.overview }}</p>
          </div>
        </div>
      </div>
    </div>
    <hr />
    <div class="actordetail">
      <h1>영화 배우 정보</h1>
      <div class="actor">
        <ActorCard v-for="actor in actors" :key="actor.id" :actor="actor" />
      </div>
    </div>

    <div>
      <MovieCommentsList
        v-for="movieComment in movieComments"
        :key="movieComment.id"
        :movieComment="movieComment"
      />
    </div>
  </div>
</template>

<script>
import ActorCard from "@/components/ActorCard.vue";
import MovieCommentsList from "@/components/MovieCommentsList.vue";
import { mapState, mapGetters } from "vuex";

export default {
  name: "MovieDetailView",
  components: {
    ActorCard,
    MovieCommentsList,
  },
  data() {
    return {
      videos: [],
    };
  },
  mounted() {
    this.getVideos();
  },
  computed: {
    ...mapState({
      movie: (state) => state.movieDetailModule.movie_detail,
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
      actors: (state) => state.movieDetailModule.actors,
    }),
    ...mapGetters(["movieComments"]),
  },
  methods: {
    getMovieDetail() {
      const movieId = this.$route.params.id;
      this.$store.dispatch("getMovieDetail", movieId);
    },
    getMovieActors() {
      const movieId = this.$route.params.id;
      this.$store.dispatch("getMovieActors", movieId);
    },
    getMovieCommentsList() {
      const movieId = this.$route.params.id;
      this.$store.dispatch("getMovieCommentsList", movieId);
    },
  },
  created() {
    this.getMovieDetail();
    this.getMovieActors();
    this.getMovieCommentsList();
  },
};
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

/* 네비게이션 */

.navbar {
  position: absolute;
  top: 0px;
  right: 0px;
  left: 0;
  height: 60px;
  z-index: 1;
  background-color: rgb(191, 185, 185);
  margin: 0px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 10px;
}

/* .navbar-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 100%;
} */
.navbar-left {
  margin-left: auto;
  display: flex;
  align-items: center;
  flex: 1;
}

.navbar-right {
  display: flex;
  align-items: center;
  flex: 1; /* 수정된 부분 */
  justify-content: flex-end; /* 수정된 부분 */
  margin-left: 100px;
  color: white;
}
</style>
