<template>
  <div id="app">
    <nav class="navbar-container">
      <div class="nav-left">
        <router-link :to="{name: 'home'}">
          <img src="@/assets/심야영화해.png" alt="로고" class="logo">
        </router-link>
      </div>

      <div class="nav-right" v-if="isLogin">
        <router-link :to="{name: 'home'}" class="navbar-link">Movie</router-link>
        <router-link :to="{name: 'ArticleView'}" class="navbar-link">Article</router-link>
        <router-link :to="{name: 'GameView'}" class="navbar-link">Game</router-link>
        <a class="navbar-link" @click="logout">LogOut</a>

        <form @submit.prevent="getSearchMovieList" class="search-form">
          <input type="text" v-model="search" placeholder="영화 이름을 검색하세요 ">
          <button><i class="fa-solid fa-magnifying-glass"></i></button>
        </form>

      </div>
      <div class="nav-right" v-else>
        <router-link :to="{name: 'LogInView'}" class="navbar-link">LogIn</router-link>
        <router-link :to="{name: 'SignUpView'}" class="navbar-link">SignUp</router-link>
      </div>
    </nav>


    <div class="modal" v-if="searchMovieList" @click="closeSearchModal">
      <div class="modal-content" @click.stop>

        <!-- 모달 내용 -->
        <div class="modal-body">
          <div v-for="movie in searchMovieList" :key="movie.id">
            <router-link :to="{name:'MovieDetailView', params: {id: movie.id}}" class="modal-link">
              {{movie.title}}
            </router-link>
          </div>
        </div>
        
        <!-- 모달 닫기 버튼 -->
        <button class="modal-close" @click="closeSearchModal"><i class="fa-solid fa-xmark fa-xl"></i></button>

      </div>
    </div>

    <!-- 유령 -->
    <div class="ghost-container">
      <div id="ghost" class="ghost">
        <div class="ghost__head">
          <div class="ghost__eyes"></div>
          <div class="ghost__mouth"></div>
        </div>
        <div class="ghost__tail">
          <div class="ghost__rip"></div>
        </div>
      </div>

      <svg xmlns="http://www.w3.org/2000/svg" version="1.1">
        <defs>
          <filter id="goo">
            <feGaussianBlur
              in="SourceGraphic"
              stdDeviation="10"
              result="ghost-blur" />
            <feColorMatrix
              in="ghost-blur"
              mode="matrix"
              values="
                      1 0 0 0 0
                      0 1 0 0 0
                      0 0 1 0 0
                      0 0 0 16 -7"
              result="ghost-gooey" />
          </filter>
        </defs>
      </svg>
    </div>


    <transition name="fade" mode="out-in">
      <router-view/>
    </transition>
  </div>
</template>

<script>
import {mapGetters} from 'vuex'

export default {
  name: 'AppView',
  computed: {
    ...mapGetters(['isLogin', 'searchMovieList']),
  },
  data() {
    return {
      search: null,
    }
  },
  methods: {
    // Top Rated 영화 정보 요청
    getTopRatedMovies() {
      this.$store.dispatch('getTopRatedMovies')
    },

    // 검색창
    getSearchMovieList() {
      // this.search = e.target.value
      if (this.search.trim().length != 0) {
        this.$store.dispatch('getSearchMovieList', this.search.trim())
        this.search = null
      } 
    },
    closeSearchModal() {
      this.$store.dispatch('closeSearchModal')
    },

    // logout
    logout() {
      this.$store.dispatch('logout')
    },
  },
  created() {
    this.getTopRatedMovies()
  },
}
</script>

<style>
body {
  margin: 0px;
  background-color: black;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
  font-size: 20px;
}

nav a.router-link-exact-active {
  color: red;
}

.navbar-container {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0% 10% 0%;
  background-color: black;
}

.nav-left {
  margin: 0.8rem;
  padding: 0;
}

.logo {
  padding-top: 7px;
  width: 200px;
  height: auto;
  margin-right: auto;
}

.nav-right {
  white-space: nowrap;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.search-form {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: flex-end;
  padding-right: 10px;
}

.search-form input {
  width: 80%;
  padding: 5px;
  border: none;
  border-radius: 3px;
}

.search-form button {
  width: 20%;
  margin-left: 4%;
  padding: 4px;
  background-color: #007bff;
  border: none;
  border-radius: 3px;
  color: #fff;
  cursor: pointer;
  font-size: 15px;
}


.navbar-link {
  margin-right: 10px;
  color: white;
  text-decoration: none;
}

.navbar-link:hover {
  cursor: pointer;
}


.fade-enter-active, .fade-leave-active {
  transition: opacity 0.5s;
}

.fade-enter, .fade-leave-to {
  opacity: 0;
}

/* 모달 스타일 */
.modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  /* background-color: rgba(0, 0, 0, 0.5); */
  z-index: 50;
}

.modal-content {
  position: fixed;
  top: 8%;
  right: 10%;
  background-color: white;
  padding: 20px;
  width: 180px;
  border-radius: 4px;
}

.modal-body {
  text-align: left;
  font-size: 80%;
}

.modal-link {
  text-decoration: none;
}

.modal-close {
  position: absolute;
  top: 10%;
  right: 3%;
  cursor: pointer;
  color: black;
  background-color: white;
  border: none;
}

/* 유령 style */
.ghost-container {
  height: 0vh;
}

#ghost {
  position: absolute;
  z-index: 1;
  transform-origin: center;
  width: 90px;
  margin: 20px 0 0 -45px;
}

.ghost__eyes, .ghost__mouth {
  position: absolute;
  z-index: 1;
  width: 15px;
  height: 15px;
  top: 34px;
  left: 50%;
  transform: translate(-50%);
  border-radius: 50px;
  background: #161616;
  margin-left: -20px;
  transform-origin: center;
}

.ghost__eyes {
  box-shadow: 40px 0 0 #161616;
}

.ghost__mouth {
  margin: 0;
  top: 60px;
  transform: scale(0);
  border-radius: 20px 20px 12px 12px;
  width: 20px;
  transform-origin: center bottom;
  overflow: hidden;
}

.ghost__tail {
  position: absolute;
  z-index: -1;
  top: 82px;
  height: 55px;
  width: 100%;
  filter: url(#goo);
}

.ghost__tail:before {
  content: '';
  background: #fff;
  position: absolute;
  bottom: 35px;
  left: 0;
  height: 100px;
  width: 100%;
  border-radius: 40px 40px 5px 5px;
}

.ghost__rip {
  width: 15px;
  height: 28px;
  background: #fff;
  position: absolute;
  top: 15px;
  left: 0;
  box-shadow: -62px 0 0 #fff, -31px 0 0 #fff, 31px 0 0 #fff, 62px 0 0 #fff, 93px 0 0 #fff;
  border-radius: 50%;
  animation: ghost-rips 1.2s linear infinite;
}

@keyframes ghost-rips {
  0% {
    left: 0;
    top: 12px;
  }
  50%{
    left: 31px;
    top: 20px;
  }
  100%{
    left: 62px;
    top: 12px;
  }
}
</style>