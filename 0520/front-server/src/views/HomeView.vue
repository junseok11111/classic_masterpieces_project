<template>
  <div class="home">
    <h3>
      <router-link :to="{ name: 'UpComingView' }">Upcoming</router-link>
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
        <swiper :options="swiperOptions" ref="swiper">
          <template v-for="movie in topRated">
            <swiper-slide :key="movie.id">
              <TopRatedHCard :movie="movie" />
            </swiper-slide>
          </template>
          <div class="swiper-button-next" slot="button-next"></div>
          <div class="swiper-button-prev" slot="button-prev"></div>
        </swiper>
      </div>
    </div>
  </div>
</template>

<script>
// import UpComingHCard from "@/components/UpComingHCard";
import TopRatedHCard from "@/components/TopRatedHCard";
import axios from "axios";
import { mapState, mapGetters } from "vuex";

// import "swiper/dist/css/swiper.css";
import "swiper/swiper-bundle.css";
import { swiper, swiperSlide } from "vue-awesome-swiper";

export default {
  name: "HomeView",
  components: {
    // UpComingHCard,
    TopRatedHCard,

    swiper,
    swiperSlide,
  },

  data() {
    return {
      videos: [],
      swiperOptions: {
        slidesPerView: 6,
        slidesPerGroup: 6,
        spaceBetween: 20,

        loop: true, // 데이터가 끝까지 다읽으면 처음으로 돌아옴
        navigation: {
          nextEl: ".swiper-button-next",
          prevEl: ".swiper-button-prev",
        },
      },
    };
  },
  mounted() {
    this.getVideos();
  },
  computed: {
    ...mapGetters(["topRated"]),
    ...mapState(["top_rated_movies"]),

    // ...mapGetters(["topRated1", "topRated2", "topRated3"]),
    // ...mapGetters(["upComing1", "upComing2", "upComing3"]),
  },
  methods: {
    async getVideos() {
      try {
        const response = await axios.get(
          "https://www.googleapis.com/youtube/v3/videos",
          {
            params: {
              part: "snippet",
              chart: "mostPopular",
              maxResults: 1,
              key: "AIzaSyAV_SvBR49eSF26yQGTJ2E4vFYh5bi1H2o", // Replace with your actual API key
            },
          }
        );

        this.videos = response.data.items;
      } catch (error) {
        console.error(error);
      }
    },
    moveSwiperNext() {
      this.$refs.swiper.swiper.slideNext(1, false);
    },
    moveSwiperPrev() {
      this.$refs.swiper.swiper.slidePrev(1, false);
    },
  },
};
</script>

<style>
/* wrapper */
.home {
  background-color: black;
  width: 100%;
  height: 100%;
}

.contents-container {
  margin-left: 300px;
  margin-right: 300px;
}

.video-container {
  width: 100%;
  height: 700px;
  background: linear-gradient(black, yellow);
}

.card-container {
  display: flex;
  flex-wrap: nowrap;
  overflow-x: auto;
  padding: 0 20px;
  gap: 20px;
}
</style>
