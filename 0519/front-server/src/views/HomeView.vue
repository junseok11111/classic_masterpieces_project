<template>
  <div class="home">

    <h3>
      <router-link :to="{name: 'UpComingView'}">Upcoming</router-link>
    </h3>

    <div class="contents-container">
      <!-- 유튜브 api 구현 -->
      <div class="video-container" v-for="video in videos" :key="video.id">
        <iframe
          :src="'https://www.youtube.com/embed/' + video.id"
          frameborder="0"
          allowfullscreen
          width="100%"  
          height="100%"  
        ></iframe>
        <p>{{ video.title }}</p>
      </div>

      <!-- top_rated_movie -->
      <div class="wrapper">
        <section id="section1">
          <a href="#section3" class="arrow__btn left-arrow">‹</a>
          <TopRatedHCard v-for="movie in topRated1" :key = movie.id :movie="movie" class="item"/>
          <a href="#section2" class="arrow__btn right-arrow">›</a>
        </section>

        <section id="section2">
          <a href="#section1" class="arrow__btn left-arrow">‹</a>
          <TopRatedHCard v-for="movie in topRated2" :key = movie.id :movie="movie" class="item"/>
          <a href="#section3" class="arrow__btn right-arrow">›</a>
        </section>
        
        <section id="section3">
          <a href="#section2" class="arrow__btn left-arrow">‹</a>
          <TopRatedHCard v-for="movie in topRated3" :key = movie.id :movie="movie" class="item"/>
          <a href="#section1" class="arrow__btn right-arrow">›</a>
        </section>
      </div>

      <!-- upComing_movie -->
      <div class="wrapper">
        <section id="section4">
          <a href="#section6" class="arrow__btn left-arrow">‹</a>
          <UpComingHCard v-for="movie in upComing1" :key = movie.id :movie="movie" class="item"/>
          <a href="#section5" class="arrow__btn right-arrow">›</a>
        </section>

        <section id="section5">
          <a href="#section4" class="arrow__btn left-arrow">‹</a>
          <UpComingHCard v-for="movie in upComing2" :key = movie.id :movie="movie" class="item"/>
          <a href="#section6" class="arrow__btn right-arrow">›</a>
        </section>
        
        <section id="section6">
          <a href="#section5" class="arrow__btn left-arrow">‹</a>
          <UpComingHCard v-for="movie in upComing3" :key = movie.id :movie="movie" class="item"/>
          <a href="#section4" class="arrow__btn right-arrow">›</a>
        </section>
      </div>


    </div>
  </div>

</template>

<script>
import UpComingHCard from '@/components/UpComingHCard'
import TopRatedHCard from '@/components/TopRatedHCard'
import axios from 'axios';
import {mapGetters} from 'vuex'

export default {
  name: 'HomeView',
  components: {
    UpComingHCard,
    TopRatedHCard,
    
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
    ...mapGetters(['topRated1', 'topRated2', 'topRated3']),
    ...mapGetters(['upComing1', 'upComing2', 'upComing3']),
    /* vuex 모듈 분리하여 관리
    topRated1() {return this.$store.getters.topRated1},
    topRated2() {return this.$store.getters.topRated2},
    topRated3() {return this.$store.getters.topRated3},
    upComing1() {return this.$store.getters.upComing1},
    upComing2() {return this.$store.getters.upComing2},
    upComing3() {return this.$store.getters.upComing3},
    */
  },
  methods: {
    async getVideos() {
      try {
        const response = await axios.get('https://www.googleapis.com/youtube/v3/videos', {
          params: {
            part: 'snippet',
            chart: 'mostPopular',
            maxResults: 1,
            key: 'AIzaSyAV_SvBR49eSF26yQGTJ2E4vFYh5bi1H2o' // Replace with your actual API key
          }
        });

        this.videos = response.data.items;
      } catch (error) {
        console.error(error);
      }
    },
  },
  
}
</script>

<style>
/* wrapper */
.home {
  background-color: black;
  width: 100%;
  height: 100%;
}

.wrapper {
  background-color: black;
  display: grid;
  grid-template-columns: repeat(3, 100%);
  overflow: hidden;
  scroll-behavior: smooth;
}
.wrapper section {
  width: 100%;
  position: relative;
  display: grid;
  grid-template-columns: repeat(6, auto);
  margin: 20px 0;
}
.wrapper section .item {
  position: relative;
  padding: 0 2px;
  transition: 250ms all;
}
.wrapper section .item:hover {
  margin: 0 40px;
  transform: scale(1.2);
}
.wrapper section .item .heading {
  position: absolute;
  bottom: 20px;
  left: 20px;
  color: #fff;
}
.wrapper section .item .duration {
  position: absolute;
  bottom: 0;
  left: 20px;
  color: #fff;
}
.wrapper section .arrow__btn {
  position: absolute;
  color: #fff;
  text-decoration: none;
  font-size: 6em;
  width: 80px;
  padding: 20px;
  text-align: center;
  z-index: 1;
  top: 50%;
  transform: translateY(-50%);
}

.card-container {
  display: flex;
  flex-wrap: nowrap;
  overflow-x: auto;
  padding: 0 20px;
  gap: 20px;
}
.wrapper section .left-arrow {
  /* top: 0;
  bottom: 0; */
  left: 0;
  background: linear-gradient(to left, transparent, black 100%);
}
.wrapper section .right-arrow {
  /* top: 0;
  bottom: 0; */
  right: 0;
  background: linear-gradient(to right, transparent, black 100%);

}


.contents-container {
  margin-left : 300px ;
  margin-right : 300px ;
  
}

.video-container {
  width: 100%; /* 화면 전체 너비 */
  height: 700px; /* 화면 전체 높이 */
  background: linear-gradient(black, yellow);
}
</style>