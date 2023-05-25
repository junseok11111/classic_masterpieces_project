<template>
  <div class="app-container">
    <div class="home-container">
      <div class="contents-container">
        <!-- 이미지 구현 구현 -->
      <div class="swiper-container image-slider">
          <swiper :options="swiperImageOptions" ref="swiperImage">

            <swiper-slide v-for="(image, index) in images" :key="index">
              <div class="todetail">
                <div class="image-wrapper">
                  <img :src="image.src" :alt="image.alt" />
                  <div class="gradient-overlay"></div>
                    <span class="text1" @click="moveGenreView(image.genre)">{{ image.title1 }}</span>
                  <div class="overlay-text" >
                    <span class="text2">{{ image.title2 }}</span>
                  </div>
                </div>
              </div>
            </swiper-slide>

            <div class="swiper-button-next" slot="button-next"></div>
            <div class="swiper-button-prev" slot="button-prev"></div>
          </swiper>
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
      images: [
        {
          src: require("@/assets/home_sample_img3.jpg"),
          alt: "Image 1",
          title1: "스릴러",
          genre: "GenreThrillerView",
        },
        {
          src: require("@/assets/home_sample_img1.jpg"),
          alt: "Image 2",
          title1: "SF",
          genre: "GenreSFView",
        },
        {
          src: require("@/assets/home_sample_img6.png"),
          alt: "Image 2",
          title1: "액션",
          genre: "GenreActionView",
        },
        {
          src: require("@/assets/home_sample_img4.jpg"),
          alt: "Image 2",
          title1: "미스터리",
          genre: "GenreMysteryView",
        },
      ],

      // 이미지 슬라이더 옵션 설정
      swiperImageOptions: {
        slidesPerView: 1,
        spaceBetween: 0,
        loop: true,
        navigation: {
          nextEl: ".swiper-button-next",
          prevEl: ".swiper-button-prev",
        },
        breakpoints: {
        },
        speed: 50,
      },

      swiperOptions: {
        slidesPerView: 6,
        slidesPerGroup: 6,
        spaceBetween: 20,

        loop: true, // 데이터가 끝까지 다읽으면 처음으로 돌아옴
        navigation: {
          nextEl: ".swiper-button-next",
          prevEl: ".swiper-button-prev",
        },
        breakpoints: {
          1400: {
            slidesPerView: 6,
            slidesPerGroup: 6,
          },
          1190: {
            slidesPerView: 5,
            slidesPerGroup: 5,
          },
          980: {
            slidesPerView: 4,
            slidesPerGroup: 4,
          },
          780: {
            slidesPerView: 3,
            slidesPerGroup: 3,
          },
          550: {
            slidesPerView: 2,
            slidesPerGroup: 2,
          },
          150: {
            slidesPerView: 1,
          },
          0: {
            slidesPerView: 1,
          },
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

    // 장르별 영화 view 이동
    moveGenreView(genre) {
      this.$router.push({name: genre})
    }
  },

};
</script>

<style>
/* wrapper */

.app-container {
  width: 100%;

  /* max-width: auto; */
  margin: 0 auto;
  height: 100vh;
  overflow-y: auto;
  overflow-x: hidden;
}
.app-container::-webkit-scrollbar {
  width: 0px; /* Set the width of the scrollbar */

}
.app-container::-webkit-scrollbar-thumb {
  background-color: rgba(
    0,
    0,
    0,
    0.5
  ); /* Set the color of the scrollbar thumb /
  border-radius: 4px; / Round the corners of the thumb */
}
.app-container::-webkit-scrollbar-track {
  background-color: rgba(
    0,
    0,
    0,
    0.1
  );
}

.contents-container {
  margin: 0 20px;
}

.home-container {
  background-color: black;
  width: 100%;
  height: auto;
  margin: 60px;
}

h3 {
  background: black;
}

/* ===============이미지 그리고 그안에 텍스트 들어갈것=========== */

.image-wrapper {
  position: relative;
  width: 100%;
  height: 0;
  padding-bottom: 60%; /* Set the aspect ratio of the image container (adjust as needed) */
  overflow: hidden;
}
.image-wrapper img {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover; /* Maintain the aspect ratio and cover the container */
}
.todetail img {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover; /* Maintain the aspect ratio and cover the container */
}

.todetail {
  width: 100%;
  height: auto;
  margin-bottom: 100px;
  position: relative;
}

.todetail img {
  width: 100%;
}

.text1 {
  position: absolute;
  top: 40%;
  left: 70px; /* 왼쪽으로 이동시킬 위치를 조정하세요 */
  text-align: center;
  font-weight: bold;
  font-size: 5em;
  color: white;
  white-space: nowrap; 
  cursor: pointer;
}
.text1:hover {
  transform: scale(1.2);
  transition-duration: 0.5s;
}

.text2 {
  position: absolute;
  top: 100px;
  left: 0px; /* 왼쪽으로 이동시킬 위치를 조정하세요 */
  font-size: 2em;
  color: white;
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

/*=======카드 */
.card-container {
  display: flex;
  flex-wrap: nowrap;
  overflow-x: auto;
  padding: 0 20px;
  gap: 20px;
}

@media (min-width: 768px) {
  .contents-container {
    margin-left: 50px;
    margin-right: 50px;
  }
}

@media (min-width: 992px) {
  .contents-container {
    margin-left: 300px;
    margin-right: 300px;
  }
}

@media (max-width: 576px) {
  .contents-container {
    margin: 0;
  }
}
</style>