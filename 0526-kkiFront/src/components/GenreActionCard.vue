<template>
  <div>
    <router-link
      :to="{ name: 'MovieDetailView', params: { id: movie.id } }"
      class="genre-movie-card"
    >
      <div>
        <img
          :src="`http://image.tmdb.org/t/p/w500${movie?.poster_path}`"
          alt="..."
          class="Detail-Card-img"
        />
      </div>
      <div class="Detail-Card-Title">
        <p>{{ movieTitle }}</p>
      </div>
    </router-link>
  </div>
</template>

<script>
export default {
  name: "GenreActionCard",
  props: {
    movie: Object,
  },
  computed: {
    movieTitle() {
      return this.movie?.title;
    },
  },
};
</script>

<style>
.Detail-Card-Title {
  color: white;
}
.Detail-Card-img {
  width: 200px;
  transition: all 0.2s linear;
}
.Detail-Card-img:hover {
  transform: scale(1.4);
}
.genre-movie-card {
  text-decoration: none;
}
</style>
