<template>
  <div>
    <p>{{movie.title}}</p>
    <router-link 
      :to="{
        name:'MovieDetailView',
        params: {id: movie.id}
        }">
      <img :src="imgSrc" alt="...">
    </router-link>

    <!-- <ul>
      <li v-for="actor in cast" :key="actor.id">{{actor.name}}</li>
    </ul> -->
  </div>
</template>

<script>
// import axios from 'axios'

// const API_KEY = process.env.VUE_APP_TMDB_API_KEY

const IMG_URL = 'http://image.tmdb.org/t/p/'
const POSTER_SIZE = ["w92",  "w154",  "w185",  "w342",  "w500",  "w780",  "original"]


export default {
  name: 'UpComingCard',
  props: {
    movie: Object,
  },
  // data() {
  //   return {
  //     cast: []
  //   }
  // },
  computed: {
    imgSrc() {
      const imgSrc = `${IMG_URL}${POSTER_SIZE[2]}${this.movie.poster_path}`
      return imgSrc
    },
  },
  // created() {
  //   this.castData()
  // },
  // methods: {
  //   castData() {
  //     axios({
  //       url: `https://api.themoviedb.org/3/movie/${this.movie.id}/credits?api_key=${API_KEY}` 
  //     })
  //     .then((res) => {
  //       this.cast = res.data.cast
  //     })
  //   }
  // }
}
</script>

<style>

</style>