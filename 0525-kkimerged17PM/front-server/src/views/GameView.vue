<template>
  <div class="big">
    <h2>공포 영화 추천</h2>
    <button @click="recommendMovie">게임시작</button>

    <div v-if="recommendedMovie">
      <h3>귀신 역할을 맡은 배우일까요 ?: {{ recommendedMovie.title }}</h3>

      <div>
        <img :src="recommendedMovie.imgq" alt="영화이미지" class="gameimg" />
      </div>
      <button @click="handleTrue">True</button>
      <button @click="handleFalse">False</button>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      movies: [
        {
          title: "박지현",
          img: "공포, 스릴러",
          bool: true,
          imgq: require("@/assets/박지현.jpg"),
        },
        {
          title: "디카프리오",
          imgq: require("@/assets/디카프리오.jpg"),
          bool: false,
        },
        {
          title: "아런스",
          imgq: require("@/assets/보니 아런스.jpg"),
          bool: true,
        },
        {
          title: "조승우",
          imgq: require("@/assets/조승우.jpg"),
          bool: false,
        },
        {
          title: "마고로비",
          imgq: require("@/assets/마고로비.png"),
          bool: false,
        },
        {
          title: "아만다",
          imgq: require("@/assets/아만다.jpg"),
          bool: false,
        },
        {
          title: "박소담",
          imgq: require("@/assets/박소담.jpg"),
          bool: true,
        },
        // {
        //   title: "오제키 유우야",
        //   imgq: require("@/assets/토시오1.PNG"),
        //   bool: false,
        // },
      ],
      recommendedMovie: null,
    };
  },
  methods: {
    recommendMovie() {
      const randomIndex = Math.floor(Math.random() * this.movies.length);
      this.recommendedMovie = this.movies[randomIndex];
    },
    handleTrue() {
      if (this.recommendedMovie.bool) {
        const randomIndex = Math.floor(Math.random() * this.movies.length);
        this.recommendedMovie = this.movies[randomIndex];
      } else {
        window.location.href = "http://localhost:8080/4";
      }
    },
    handleFalse() {
      if (!this.recommendedMovie.bool) {
        const randomIndex = Math.floor(Math.random() * this.movies.length);
        this.recommendedMovie = this.movies[randomIndex];
      } else {
        window.location.href = "http://localhost:8080/4";
      }
    },
  },
};
</script>

<style>
.big {
  height: 100vh;
}

.gameimg {
  width: 300px;
  height: 500px;
}
</style>
