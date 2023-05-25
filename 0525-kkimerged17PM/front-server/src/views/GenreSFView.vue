<template>
<div class="SFView">
  
    <div class="Genre-SF-Title">
     <h1>SF</h1>
    </div>
  
    <div class="Genre-Card-container">
    <GenreSFCard
      v-for="movie in SFMovies"
      :key="movie.id"
      :movie="movie"
    />
  </div>
 </div>
</template>

<script>
import GenreSFCard from '@/components/GenreSFCard'
import {mapGetters} from 'vuex'

export default {
  name: 'GenreSFView',
  components: {
    GenreSFCard,
  },
  computed: {
    ...mapGetters(["SFMovies"])
  },
  methods: {
    getSFMovies() {
      this.$store.dispatch('getSFMovies')
    },
  },
  created() {
    this.getSFMovies()
  },
}
</script>

<style>
.Genre-SF-Title {
  color: rgb(168, 2, 2);
  font-size: 30px; 
  margin-bottom : 40px;
  margin-left: 5%;
  text-align: left;
}

.SFView {
  height: 100vh;
  overflow-y: auto;
  padding: 20px; /* 화면 좌우 간격을 조절하기 위한 패딩 설정 */
}

.Genre-Card-container {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  grid-gap: 10px;
  padding-bottom: 100px; /* Add bottom padding to ensure the last row is fully visible */
}

@media (max-width: 768px) {
  /* 반응형 디자인을 적용할 화면 크기에 따른 스타일 설정 */
  .Genre-Card-container {
    grid-template-columns: repeat(2, 1fr); /* 화면 크기가 768px 이하일 때 2열로 변경 */
  }
}

/* 스크롤 스타일링 */
.SFView::-webkit-scrollbar {
  width: 0px;
  background-color: #f5f5f5;
}a

.SFView::-webkit-scrollbar-thumb {
  background-color: #888;
}

.SFView::-webkit-scrollbar-thumb:hover {
  background-color: #555;
}
</style>