<template>
  <div class="home-container">
    <nav class="navbar"> 
        <div class="navbar-header">
          <div class="navbar-left">
            <img src="../assets/7a57b8e8-4029-4220-8d9f-2b1c89b2c1e5.png" alt="로고" class="logo">
          </div>
          <div class="navbar-right">
            <!-- <router-link :to="{ name: 'UpComingView' }">Upcoming</router-link> | -->
            <router-link :to="{ name: 'SignUpView' }">SignUp</router-link> |
            <router-link :to="{ name: 'LogInView' }">LogIn</router-link> |
          </div>
        </div>
    </nav>


    <div class="contents-container">
      <!-- 유튜브 api 구현 -->
    <div class="image-container">
      <div class="todetail">
        <img src="../assets/86772212622_727.jpg" alt="영화이미지">
        <div class="gradient-overlay"></div>
        <font-awesome-icon :icon="['fal', 'circle-play']" />
        <span class="text">The Nun</span>
        <span class="text">존나무서움</span>
      </div>
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
        speed: 1000, // 넘김 속도 (단위: 밀리초)
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
.text {
  position: absolute;
  top: 50%;
  left: 0; /* 이미지의 오른쪽에 텍스트를 배치합니다. */
  transform: translate(50%, -50%); /* 텍스트를 수직 및 수평으로 가운데로 정렬합니다. */
  color: white;
  font-size: 24px;
  font-weight: bold;
  text-align: center;
}
.home-container {
  background-color: black;
  width: 100%;
  height: 100%;
  margin: 0;
}
h3 {
  background: black;
}
.contents-container {
  margin-left: 300px;
  margin-right: 300px;
  
}

.todetail img {
  width: 100%;
}

.todetail {

  width: 100%;
  height: auto;
  margin-bottom: 100px;
  position: relative;

}

.gradient-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 50%; /* 왼쪽 부분만 적용하므로 너비를 50%로 설정 */
  height: 100%;
  background: linear-gradient(to left, transparent, black 100%);
  
  background-size: cover;
  opacity: 1;

}
.card-container {
  display: flex;
  flex-wrap: nowrap;
  overflow-x: auto;
  padding: 0 20px;
  gap: 20px;
}


.fa-light fa-circle-play{
  width: 1000px;
}
</style>