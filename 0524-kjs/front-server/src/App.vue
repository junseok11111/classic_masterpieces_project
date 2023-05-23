<template>
  <div id="app">
    <nav class="navbar-container">
      <div class="nav-left">
        <router-link :to="{name: 'DoorView'}">
          <img src="@/assets/sample_site_logo.png" alt="로고" class="logo">
        </router-link>
      </div>

      <div class="nav-right" v-if="isLogin">
        <router-link :to="{name: 'home'}" class="navbar-link">Home</router-link>
        <router-link :to="{name: 'UpComingView'}" class="navbar-link">Upcoming</router-link>
        <a class="navbar-link" @click="logout">LogOut</a>
      </div>
      <div class="nav-right" v-else>
        <router-link :to="{name: 'LogInView'}" class="navbar-link">LogIn</router-link>
        <router-link :to="{name: 'SignUpView'}" class="navbar-link">SignUp</router-link>
      </div>
    </nav>
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
    ...mapGetters(['isLogin'])
  },
  methods: {
    // Top Rated 영화 정보 요청
    getTopRatedMovies() {
      this.$store.dispatch('getTopRatedMovies')
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
}

nav a.router-link-exact-active {
  color: #42b983;
}

.navbar-container {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin: 0% 10% 0%;
  padding: 0px;
  background-color: black;
}

.nav-left {
  margin: 0.8rem;
  padding: 0;
}

.logo {
  width: 80px; 
  height: auto;
  margin-right: auto;
}

.nav-right {
  display: flex;
  justify-content: space-between;
  align-items: center;
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
/* .navbar {
  position: absolute;
  top: 0px;
  right: 0px;
  left: 0;
  height: 60px;
  z-index: 1;
  background-color: black;
  margin: 0px;
  display: flex;
  justify-content: space-between;  
  align-items: center; 
  padding: 0 10px; 
}

.navbar-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 100%;
}
.navbar-left {
  margin-left: auto;
  display: flex;
  align-items: center;
  flex: 1; 
}

.navbar-right {
  display: flex;
  align-items: center;
    flex: 1; 
  justify-content: flex-end; 
}

.navbar-link {
  margin-left: 10px;
  color: white;
  text-decoration: none;
}

.navbar-link:hover {
  cursor: pointer;
}

.logo {
  width: 80px; 
  height: auto;
  margin-right: auto;
} */
</style>